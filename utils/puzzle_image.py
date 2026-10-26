"""
Robust image-processing pipeline for 8-puzzle board recognition.
Handles PNG, JPG, JPEG with preprocessing, board localization, cell slicing,
and OCR with manual-correction fallback.
"""

import os
import re
import numpy as np
from PIL import Image, ImageOps, ImageEnhance

try:
    import cv2
    CV2_AVAILABLE = True
except ImportError:
    CV2_AVAILABLE = False

try:
    import pytesseract
    TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    if os.path.exists(TESSERACT_PATH):
        pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
    TESSERACT_AVAILABLE = True
except ImportError:
    TESSERACT_AVAILABLE = False


def preprocess_and_crop_board(pil_img):
    """
    Locate and crop the 3x3 puzzle board using OpenCV contour analysis.
    If board borders or perspective distortion exist, crop to the board quadrilateral.
    Falls back to a centered square crop if contour detection fails.
    """
    if not CV2_AVAILABLE:
        # Simple square crop centered
        w, h = pil_img.size
        side = min(w, h)
        left = (w - side) // 2
        top = (h - side) // 2
        return pil_img.crop((left, top, left + side, top + side))

    open_cv_image = np.array(pil_img.convert("RGB"))
    gray = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection & thresholding
    thresh = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_area = gray.shape[0] * gray.shape[1]
    best_rect = None
    max_area = 0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 0.15 * img_area:
            continue
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        if len(approx) == 4 and area > max_area:
            # Check aspect ratio
            x, y, w, h = cv2.boundingRect(approx)
            aspect = float(w) / max(h, 1)
            if 0.75 <= aspect <= 1.35:
                max_area = area
                best_rect = (x, y, w, h)

    if best_rect is not None:
        x, y, w, h = best_rect
        # Slight margin inset to avoid external border lines
        margin = int(min(w, h) * 0.02)
        x1 = max(0, x + margin)
        y1 = max(0, y + margin)
        x2 = min(gray.shape[1], x + w - margin)
        y2 = min(gray.shape[0], y + h - margin)
        cropped_cv = open_cv_image[y1:y2, x1:x2]
        return Image.fromarray(cropped_cv)

    # Fallback: square crop around center
    w, h = pil_img.size
    side = int(min(w, h) * 0.95)
    left = (w - side) // 2
    top = (h - side) // 2
    return pil_img.crop((left, top, left + side, top + side))


def ocr_single_cell(cell_img):
    """
    Recognize a single tile digit (1-8) or determine if it is blank (0).
    Uses multi-pass thresholding and Tesseract PSM modes.
    """
    if not TESSERACT_AVAILABLE:
        return None

    # Inset cell to avoid grid borders
    w, h = cell_img.size
    mx = int(w * 0.15)
    my = int(h * 0.15)
    if w > 2 * mx and h > 2 * my:
        cell_core = cell_img.crop((mx, my, w - mx, h - my))
    else:
        cell_core = cell_img

    gray = ImageOps.grayscale(cell_core)
    gray = ImageOps.autocontrast(gray)

    # Check if cell is blank based on pixel intensity variance
    np_gray = np.array(gray)
    std_dev = np.std(np_gray)
    if std_dev < 14:  # Almost solid/uniform color -> blank tile
        return 0

    # Resize for OCR readability (ideal height ~80-120px)
    target_h = 100
    ratio = target_h / max(gray.height, 1)
    target_w = max(int(gray.width * ratio), 10)
    resized = gray.resize((target_w, target_h), Image.Resampling.LANCZOS)

    candidates = []

    # Attempt 1: Standard high contrast
    thresh1 = resized.point(lambda p: 255 if p > 130 else 0)
    for psm in [10, 6, 7]:
        txt = pytesseract.image_to_string(
            thresh1, config=f"--psm {psm} -c tessedit_char_whitelist=12345678"
        )
        found = re.findall(r"[1-8]", txt)
        if found:
            candidates.append(int(found[0]))
            break

    # Attempt 2: Inverted (if dark theme / white text on dark background)
    if not candidates:
        inv = ImageOps.invert(thresh1)
        for psm in [10, 6]:
            txt = pytesseract.image_to_string(
                inv, config=f"--psm {psm} -c tessedit_char_whitelist=12345678"
            )
            found = re.findall(r"[1-8]", txt)
            if found:
                candidates.append(int(found[0]))
                break

    # Attempt 3: Grayscale directly
    if not candidates:
        txt = pytesseract.image_to_string(
            resized, config="--psm 10 -c tessedit_char_whitelist=12345678"
        )
        found = re.findall(r"[1-8]", txt)
        if found:
            candidates.append(int(found[0]))

    if candidates:
        return candidates[0]

    # If no digit could be recognized and std dev is moderately low, treat as blank
    if std_dev < 25:
        return 0

    return None


def extract_puzzle_from_image(uploaded_file):
    """
    Extract 3x3 puzzle board from uploaded image.
    Returns:
        detected_tiles: list of 9 ints (0 for blank, 1-8 for digits)
        is_exact: True if exactly all 0-8 were found without conflict
        message: Explanatory text for the user
    """
    try:
        if isinstance(uploaded_file, Image.Image):
            raw_img = uploaded_file.convert("RGB")
        else:
            raw_img = Image.open(uploaded_file).convert("RGB")
    except Exception as e:
        raise ValueError(f"Could not open image file: {e}")

    board_img = preprocess_and_crop_board(raw_img)
    bw, bh = board_img.size

    tiles = []
    for r in range(3):
        for c in range(3):
            x1 = c * bw // 3
            y1 = r * bh // 3
            x2 = (c + 1) * bw // 3
            y2 = (r + 1) * bh // 3
            cell = board_img.crop((x1, y1, x2, y2))
            val = ocr_single_cell(cell)
            tiles.append(val)

    # Count identified values
    identified = [t for t in tiles if t is not None]
    
    # If some tiles couldn't be recognized, fill with 0 or leave for user correction
    detected = [t if t is not None else 0 for t in tiles]

    # Solvability / validity check
    is_exact = sorted(detected) == list(range(9))
    if is_exact:
        msg = "Board successfully recognized with all 9 tiles!"
    else:
        missing = [d for d in range(9) if d not in detected]
        dupes = [d for d in range(9) if detected.count(d) > 1]
        msg = f"Recognition preview ready. Please verify each tile below (Missing: {missing}, Duplicates: {dupes})."

    return detected, is_exact, msg
