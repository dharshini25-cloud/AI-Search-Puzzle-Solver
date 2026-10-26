"""
AI-Based Search & Puzzle Solver — Main Streamlit Application
============================================================
Multi-page app with sidebar navigation covering:
  1. Home Dashboard
  2. 8-Puzzle Solver
  3. Algorithm Lab
  4. AI Tutor
  5. AI Quiz
  6. Graph Search
  7. Water Jug Solver
  8. Solution History & Reports
  9. About
"""

import os
import re
import time
import json
import random
import math
import io

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

from PIL import Image, ImageOps

try:
    import pytesseract
    TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    if os.path.exists(TESSERACT_PATH):
        pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
    TESSERACT_AVAILABLE = True
except ImportError:
    TESSERACT_AVAILABLE = False

# ── Algorithm imports (preserve existing) ────────────────────────────────────
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.astar import astar
from algorithms.greedy import greedy
from algorithms.bidirectional import bidirectional
from algorithms.uniform_cost import uniform_cost
from algorithms.depth_limited import depth_limited
from algorithms.iddfs import iddfs
from algorithms.graph_search import (
    bfs_graph, dfs_graph, astar_graph, greedy_graph,
    bidirectional_graph, ucs_graph, depth_limited_graph, iddfs_graph,
    parse_edges, run_graph_algorithm,
)
from algorithms.water_jug import solve_water_jug

from utils.puzzle import validate_puzzle, is_solvable, explain_unsolvable
from utils.puzzle_image import extract_puzzle_from_image
from utils.styles import GLOBAL_CSS
from utils.tutor_kb import answer_question, SUGGESTED_QUESTIONS
from utils.quiz_data import QUIZ_QUESTIONS
from utils.db import record_solve, record_quiz, get_solve_history, get_quiz_scores, get_stats

# ─────────────────────────────────────────────────────────────────────────────
# Page configuration
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Search & Puzzle Solver",
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────────────────────────────────────
DEFAULT_PUZZLE = [1, 2, 3, 4, 5, 6, 7, 0, 8]
DEFAULT_GOAL   = [1, 2, 3, 4, 5, 6, 7, 8, 0]

ALGORITHMS = {
    "A* Search":                  astar,
    "Breadth-First Search (BFS)": bfs,
    "Depth-First Search (DFS)":   dfs,
    "Greedy Best-First Search":   greedy,
    "Bidirectional Search":       bidirectional,
    "Uniform Cost Search":        uniform_cost,
    "Depth-Limited Search":       depth_limited,
    "Iterative Deepening DFS":    iddfs,
}

ALGO_INFO = {
    "A* Search":                  {"complete": True,  "optimal": True,  "time": "O(b^d)", "space": "O(b^d)", "note": "Best choice: optimal + efficient with Manhattan Distance heuristic."},
    "Breadth-First Search (BFS)": {"complete": True,  "optimal": True,  "time": "O(b^d)", "space": "O(b^d)", "note": "Guarantees shortest path; memory-intensive for deep solutions."},
    "Depth-First Search (DFS)":   {"complete": False, "optimal": False, "time": "O(b^m)", "space": "O(b·m)", "note": "Low memory; may not find optimal path. Uses depth limit."},
    "Greedy Best-First Search":   {"complete": True,  "optimal": False, "time": "O(b^m)", "space": "O(b^m)", "note": "Fast but not guaranteed optimal. Uses Manhattan heuristic."},
    "Bidirectional Search":       {"complete": True,  "optimal": True,  "time": "O(b^d/2)", "space": "O(b^d/2)", "note": "Searches from both ends; very efficient for hard puzzles."},
    "Uniform Cost Search":        {"complete": True,  "optimal": True,  "time": "O(b^(C*/ε))", "space": "O(b^(C*/ε))", "note": "Equivalent to BFS for uniform-cost puzzles."},
    "Depth-Limited Search":       {"complete": False, "optimal": False, "time": "O(b^L)", "space": "O(b·L)", "note": "DFS with depth cap L=30. May miss deeper solutions."},
    "Iterative Deepening DFS":    {"complete": True,  "optimal": True,  "time": "O(b^d)", "space": "O(b·d)", "note": "Optimal memory use with BFS-level optimality."},
}

# ─────────────────────────────────────────────────────────────────────────────
# Session-state initialisation
# ─────────────────────────────────────────────────────────────────────────────
def _init_session():
    """Initialise all session state keys once."""
    defaults = {
        "page": "Home Dashboard",
        "puzzle_initialized": False,
        "chat_history": [],
        "quiz_active": False,
        "quiz_questions": [],
        "quiz_index": 0,
        "quiz_score": 0,
        "quiz_answered": False,
        "quiz_difficulty": "Beginner",
        "solve_history_local": [],
        "anim_step": 0,
        "anim_path": None,
        "anim_goal": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

    if not st.session_state.puzzle_initialized:
        for i, v in enumerate(DEFAULT_PUZZLE):
            st.session_state[f"tile_{i}"] = v
        for i, v in enumerate(DEFAULT_GOAL):
            st.session_state[f"goal_{i}"] = v
        st.session_state.puzzle_initialized = True

_init_session()

# ─────────────────────────────────────────────────────────────────────────────
# Helpers — Puzzle
# ─────────────────────────────────────────────────────────────────────────────
def reset_initial():
    for i, v in enumerate(DEFAULT_PUZZLE):
        st.session_state[f"tile_{i}"] = v

def reset_goal():
    for i, v in enumerate(DEFAULT_GOAL):
        st.session_state[f"goal_{i}"] = v

def shuffle_puzzle():
    goal = get_state_from_session("goal")
    if not validate_puzzle(goal):
        goal = DEFAULT_GOAL
    nums = list(range(9))
    random.shuffle(nums)
    while not is_solvable(nums, goal):
        random.shuffle(nums)
    for i, v in enumerate(nums):
        st.session_state[f"tile_{i}"] = v

def get_state_from_session(prefix):
    return [int(st.session_state[f"{prefix}_{i}"]) for i in range(9)]

def render_tile(value, moved=False, size=72):
    if value == 0:
        cls = "puzzle-tile puzzle-tile-blank"
        text = ""
    elif moved:
        cls = "puzzle-tile puzzle-tile-moved"
        text = str(value)
    else:
        cls = "puzzle-tile puzzle-tile-filled"
        text = str(value)
    return (
        f'<div class="{cls}" style="height:{size}px;font-size:{int(size*0.38)}px;">'
        f'{text}</div>'
    )

def display_board_html(state, moved_tile=None, size=72):
    """Render a 3×3 board as styled HTML."""
    html = '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:4px;max-width:240px;">'
    for i, v in enumerate(state):
        html += render_tile(v, moved=(v == moved_tile and v != 0), size=size)
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

def find_moved_tile(prev, curr):
    """Return the tile value that moved between two consecutive states."""
    prev, curr = list(prev), list(curr)
    blank_prev = prev.index(0)
    blank_curr = curr.index(0)
    if blank_prev != blank_curr:
        return prev[blank_curr]  # the tile that filled the old blank
    return None

def run_solver(algorithm_name, start_state, goal_state):
    """Run one algorithm and return (path, nodes, elapsed). path=None on failure."""
    solver = ALGORITHMS[algorithm_name]
    start = time.perf_counter()
    try:
        if algorithm_name == "Depth-Limited Search":
            result = solver(start_state, goal_state, limit=30)
        elif algorithm_name == "Depth-First Search (DFS)":
            result = solver(start_state, goal_state, max_depth=30)
        elif algorithm_name == "Iterative Deepening DFS":
            result = solver(start_state, goal_state, max_depth=50)
        else:
            result = solver(start_state, goal_state)
        elapsed = time.perf_counter() - start
        path, nodes = result
        if path is not None:
            path = [tuple(s) for s in path]
        return path, nodes, elapsed
    except Exception as e:
        elapsed = time.perf_counter() - start
        return None, 0, elapsed

def read_puzzle_image(uploaded_file):
    """OCR a puzzle image into a 9-element list."""
    image = Image.open(uploaded_file).convert("RGB")
    w, h = image.size
    tiles = []
    for row in range(3):
        for col in range(3):
            cell = image.crop((col*w//3, row*h//3, (col+1)*w//3, (row+1)*h//3))
            mx, my = int(cell.width*0.18), int(cell.height*0.18)
            if cell.width > 2*mx and cell.height > 2*my:
                cell = cell.crop((mx, my, cell.width-mx, cell.height-my))
            cell = ImageOps.autocontrast(ImageOps.grayscale(cell))
            cell = cell.resize((cell.width*3, cell.height*3))
            text = pytesseract.image_to_string(
                cell, config="--psm 10 -c tessedit_char_whitelist=012345678"
            )
            found = re.findall(r"[0-8]", text)
            if len(found) == 0:
                tiles.append(0)
            elif len(found) == 1:
                tiles.append(int(found[0]))
            else:
                raise ValueError(f"Ambiguous OCR at row {row+1}, col {col+1}.")
    if not validate_puzzle(tiles):
        raise ValueError("OCR did not detect 0–8 each exactly once. Please correct manually.")
    return tiles

# ─────────────────────────────────────────────────────────────────────────────
# Sidebar navigation
# ─────────────────────────────────────────────────────────────────────────────
NAV_PAGES = [
    ("🏠", "Home Dashboard"),
    ("🧩", "8-Puzzle Solver"),
    ("⚗️", "Algorithm Lab"),
    ("🤖", "AI Tutor"),
    ("📝", "AI Quiz"),
    ("🕸️", "Graph Search"),
    ("🪣", "Water Jug Solver"),
    ("📊", "History & Reports"),
    ("ℹ️", "About"),
]

with st.sidebar:
    st.markdown(
        '<div style="text-align:center;padding:0.75rem 0 1.25rem;">'
        '<span style="font-family:Outfit,sans-serif;font-weight:800;font-size:1.25rem;'
        'color:#111827;">'
        '🧩 AI Puzzle Solver</span></div>',
        unsafe_allow_html=True,
    )

    for icon, label in NAV_PAGES:
        is_active = st.session_state.page == label
        btn_type = "primary" if is_active else "secondary"
        if st.button(
            f"{icon}  {label}",
            key=f"nav_{label}",
            type=btn_type,
            use_container_width=True,
        ):
            st.session_state.page = label
            st.rerun()

    st.markdown("---")
    st.caption("Academic Project · AI Search")

# ─────────────────────────────────────────────────────────────────────────────
# PAGE 1 — Home Dashboard
# ─────────────────────────────────────────────────────────────────────────────
def page_home():
    st.markdown('<div class="page-title">🧩 AI-Based Search & Puzzle Solver</div>', unsafe_allow_html=True)
    st.markdown(
        '<p style="color:#374151;font-size:1.05rem;font-weight:500;margin-bottom:1.5rem;">'
        'An interactive educational platform for exploring AI search algorithms '
        'through hands-on puzzle solving, visualisation, and quizzes.</p>',
        unsafe_allow_html=True,
    )

    # CTA buttons
    c1, c2, c3 = st.columns([1, 1, 2])
    with c1:
        if st.button("🧩 Start Solving", type="primary", use_container_width=True):
            st.session_state.page = "8-Puzzle Solver"
            st.rerun()
    with c2:
        if st.button("📚 Learn AI Algorithms", use_container_width=True):
            st.session_state.page = "AI Tutor"
            st.rerun()

    st.markdown("---")

    # Stats
    stats = get_stats()
    s1, s2, s3 = st.columns(3)
    s1.metric("Puzzles Solved", stats["puzzles_solved"])
    s2.metric("Algorithms Tested", stats["algorithms_tested"])
    s3.metric("Quiz Attempts", stats["quiz_attempts"])

    st.markdown("---")

    # Feature cards
    st.subheader("What Can You Do Here?")
    features = [
        ("🧩", "8-Puzzle Solver", "Solve the classic 3×3 sliding puzzle with 8 different AI search algorithms. Upload an image or enter manually.", "8-Puzzle Solver"),
        ("⚗️", "Algorithm Lab", "Run multiple algorithms on the same puzzle and compare execution time, nodes expanded, and solution length.", "Algorithm Lab"),
        ("🤖", "AI Tutor", "Ask any question about AI search algorithms and get clear, educational answers with examples and tables.", "AI Tutor"),
        ("📝", "AI Quiz", "Test your knowledge with 25 verified multiple-choice questions across beginner, intermediate, and advanced levels.", "AI Quiz"),
        ("🕸️", "Graph Search", "Define your own graph with nodes and edges, then visualise BFS, DFS, or A* traversal step by step.", "Graph Search"),
        ("🪣", "Water Jug Solver", "Solve the classic water jug problem with BFS and visualise every fill, pour, and empty operation.", "Water Jug Solver"),
    ]

    cols = st.columns(3)
    for idx, (icon, title, desc, target) in enumerate(features):
        with cols[idx % 3]:
            card_html = (
                f'<div class="feature-card">'
                f'<span class="icon">{icon}</span>'
                f'<h3>{title}</h3>'
                f'<p>{desc}</p>'
                f'</div>'
            )
            st.markdown(card_html, unsafe_allow_html=True)
            if st.button(f"Open {title}", key=f"card_btn_{idx}", use_container_width=True):
                st.session_state.page = target
                st.rerun()

    st.markdown("---")

    # How it works
    st.subheader("How It Works")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown(
            '<div class="feature-card"><span class="icon">1️⃣</span><h3>Set Up the Puzzle</h3>'
            '<p>Enter a start state manually, shuffle randomly, or upload an image for OCR detection.</p></div>',
            unsafe_allow_html=True,
        )
    with col_b:
        st.markdown(
            '<div class="feature-card"><span class="icon">2️⃣</span><h3>Choose an Algorithm</h3>'
            '<p>Select one of 8 AI search algorithms. Each has different properties, strengths, and trade-offs.</p></div>',
            unsafe_allow_html=True,
        )
    with col_c:
        st.markdown(
            '<div class="feature-card"><span class="icon">3️⃣</span><h3>Visualise the Solution</h3>'
            '<p>Step through the solution move by move with animated tile highlighting and statistics.</p></div>',
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.subheader("Technologies Used")
    tech_cols = st.columns(5)
    techs = ["🐍 Python 3.13", "🎯 Streamlit", "📊 Plotly", "🖼️ Pillow/OCR", "🗄️ SQLite"]
    for i, t in enumerate(techs):
        with tech_cols[i]:
            st.markdown(f'<div style="text-align:center;padding:.65rem;background:#ffffff;border:1.5px solid #cbd5e1;border-radius:10px;font-size:.9rem;font-weight:600;color:#111827;box-shadow:0 1px 3px rgba(0,0,0,0.05);">{t}</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 2 — 8-Puzzle Solver
# ─────────────────────────────────────────────────────────────────────────────
def page_puzzle():
    st.markdown('<div class="page-title">🧩 8-Puzzle Solver</div>', unsafe_allow_html=True)
    st.caption("Enter or upload your puzzle, choose a goal and algorithm, then solve and step through the solution.")

    # ── Algorithm selection (Simplified: single clean dropdown, no duplicate info cards) ───
    algorithm_name = st.selectbox(
        "🔬 Search Algorithm",
        list(ALGORITHMS.keys()),
        key="selected_algo",
    )

    st.markdown("---")

    tab_manual, tab_image = st.tabs(["✏️ Manual Input", "📷 Image Upload"])

    # ── Manual Input ─────────────────────────────────────────────────────────
    with tab_manual:
        col_init, col_goal = st.columns(2)

        with col_init:
            st.subheader("Initial State")
            for row in range(3):
                cols = st.columns(3)
                for col in range(3):
                    i = row * 3 + col
                    with cols[col]:
                        st.number_input(
                            f"T{i+1}",
                            min_value=0, max_value=8, step=1,
                            key=f"tile_{i}", label_visibility="collapsed",
                        )
            
            # Live validation for initial state
            init_vals = [int(st.session_state.get(f"tile_{i}", DEFAULT_PUZZLE[i])) for i in range(9)]
            if validate_puzzle(init_vals):
                st.markdown('<span style="color:#10b981;font-size:0.85rem;font-weight:600;">✅ Valid 3×3 state (0–8 each once)</span>', unsafe_allow_html=True)
            else:
                missing = [n for n in range(9) if n not in init_vals]
                dupes = [n for n in range(9) if init_vals.count(n) > 1]
                st.markdown(f'<span style="color:#ef4444;font-size:0.85rem;font-weight:600;">⚠️ Invalid: Missing {missing}, Duplicates {dupes}</span>', unsafe_allow_html=True)

            btn_row = st.columns(2)
            with btn_row[0]:
                st.button("↩️ Reset Initial", on_click=reset_initial, use_container_width=True)
            with btn_row[1]:
                st.button("🎲 Shuffle", on_click=shuffle_puzzle, use_container_width=True)

        with col_goal:
            st.subheader("Goal State")
            for row in range(3):
                cols = st.columns(3)
                for col in range(3):
                    i = row * 3 + col
                    with cols[col]:
                        st.number_input(
                            f"G{i+1}",
                            min_value=0, max_value=8, step=1,
                            key=f"goal_{i}", label_visibility="collapsed",
                        )
            
            # Live validation for goal state
            goal_vals = [int(st.session_state.get(f"goal_{i}", DEFAULT_GOAL[i])) for i in range(9)]
            if validate_puzzle(goal_vals):
                st.markdown('<span style="color:#10b981;font-size:0.85rem;font-weight:600;">✅ Valid 3×3 state (0–8 each once)</span>', unsafe_allow_html=True)
            else:
                missing_g = [n for n in range(9) if n not in goal_vals]
                dupes_g = [n for n in range(9) if goal_vals.count(n) > 1]
                st.markdown(f'<span style="color:#ef4444;font-size:0.85rem;font-weight:600;">⚠️ Invalid: Missing {missing_g}, Duplicates {dupes_g}</span>', unsafe_allow_html=True)

            st.button("↩️ Reset Goal", on_click=reset_goal, use_container_width=True)

        # Preview boards side-by-side
        prev_col, goal_col = st.columns(2)
        with prev_col:
            st.caption("Preview — Initial Board")
            display_board_html(get_state_from_session("tile"))
        with goal_col:
            st.caption("Preview — Selected Goal Board")
            display_board_html(get_state_from_session("goal"))

        # Solvability indicator
        if validate_puzzle(init_vals) and validate_puzzle(goal_vals):
            if is_solvable(init_vals, goal_vals):
                st.info("💡 Solvability check: **Solvable** (even relative inversion parity). Ready to solve!")
            else:
                st.warning("⚠️ Solvability check: **Unsolvable** (odd relative inversion parity). This initial state cannot reach the selected goal state.")

    # ── Image Upload ─────────────────────────────────────────────────────────
    with tab_image:
        st.markdown("Upload a PNG, JPG, or JPEG photo or screenshot of a 3×3 8-puzzle board. The detector will localize the grid and recognize digits 1–8 with 0 as blank.")
        uploaded = st.file_uploader(
            "Upload puzzle image",
            type=["png", "jpg", "jpeg"],
            key="puzzle_img",
        )

        if uploaded:
            col_img, col_btn = st.columns([1, 2])
            with col_img:
                st.image(uploaded, caption="Uploaded image", width=200)
            with col_btn:
                st.markdown(
                    "**How it works:**\n"
                    "1. Click **📷 Preview Detected Board** to analyze tiles.\n"
                    "2. Review the detected values and correct any mistakes.\n"
                    "3. Click **🚀 Confirm and Solve** or **📥 Load into Manual Input**."
                )
                if st.button("📷 Preview Detected Board", key="preview_detected_btn", type="secondary"):
                    with st.spinner("Analyzing image grid and detecting tiles..."):
                        try:
                            detected, is_exact, msg = extract_puzzle_from_image(uploaded)
                            st.session_state["img_detected"] = detected
                            st.session_state["img_msg"] = msg
                            st.session_state["img_exact"] = is_exact
                        except Exception as e:
                            st.error(f"Detection failed: {e}")
                            st.session_state["img_detected"] = [0]*9
                            st.session_state["img_msg"] = str(e)
                            st.session_state["img_exact"] = False

        if "img_detected" in st.session_state and st.session_state["img_detected"] is not None:
            st.markdown("---")
            st.subheader("Detected Board & Manual Tile Correction")
            if st.session_state.get("img_msg"):
                if st.session_state.get("img_exact", False):
                    st.success(f"✅ {st.session_state['img_msg']}")
                else:
                    st.info(f"ℹ️ {st.session_state['img_msg']}")

            prev_det_col, corr_grid_col = st.columns([1, 2])
            with prev_det_col:
                st.caption("Visual Preview")
                display_board_html(st.session_state["img_detected"], size=64)

            with corr_grid_col:
                st.caption("Verify and correct each tile (0 = blank space):")
                corr_vals = []
                for row in range(3):
                    cols = st.columns(3)
                    for col in range(3):
                        i = row * 3 + col
                        cur_v = int(st.session_state["img_detected"][i])
                        with cols[col]:
                            v = st.number_input(
                                f"T({row+1},{col+1})",
                                min_value=0, max_value=8, step=1,
                                value=cur_v,
                                key=f"corr_{i}",
                                label_visibility="collapsed",
                            )
                            corr_vals.append(int(v))

            if validate_puzzle(corr_vals):
                st.success("✅ Valid board (each digit 0–8 appears exactly once).")
                c_btn1, c_btn2 = st.columns(2)
                with c_btn1:
                    if st.button("🚀 Confirm and Solve", type="primary", key="confirm_and_solve_img", use_container_width=True):
                        for i, v in enumerate(corr_vals):
                            st.session_state[f"tile_{i}"] = v
                        st.session_state["img_detected"] = None
                        st.session_state["trigger_solve"] = True
                        st.rerun()
                with c_btn2:
                    if st.button("📥 Load into Manual Input", key="load_to_manual_btn", use_container_width=True):
                        for i, v in enumerate(corr_vals):
                            st.session_state[f"tile_{i}"] = v
                        st.session_state["img_detected"] = None
                        st.success("Board loaded into Manual Input tab!")
                        st.rerun()
            else:
                missing = [n for n in range(9) if n not in corr_vals]
                dupes = [n for n in range(9) if corr_vals.count(n) > 1]
                st.error(f"⚠️ Board incomplete: Missing {missing}, Duplicates {dupes}. Each digit 0–8 must appear exactly once.")

    st.markdown("---")

    # ── Solve ─────────────────────────────────────────────────────────────────
    should_solve = st.button("🚀 Solve Puzzle", type="primary", use_container_width=True, key="solve_btn")
    if st.session_state.get("trigger_solve", False):
        should_solve = True
        st.session_state["trigger_solve"] = False

    if should_solve:
        start_state = get_state_from_session("tile")
        goal_state  = get_state_from_session("goal")

        if not validate_puzzle(start_state):
            missing = [n for n in range(9) if n not in start_state]
            dupes = [n for n in range(9) if start_state.count(n) > 1]
            st.error(f"Invalid initial puzzle. Each number 0–8 must appear exactly once. Missing: {missing}, Duplicates: {dupes}.")
        elif not validate_puzzle(goal_state):
            missing_g = [n for n in range(9) if n not in goal_state]
            dupes_g = [n for n in range(9) if goal_state.count(n) > 1]
            st.error(f"Invalid goal state. Each number 0–8 must appear exactly once. Missing: {missing_g}, Duplicates: {dupes_g}.")
        elif not is_solvable(start_state, goal_state):
            st.error(explain_unsolvable(start_state, goal_state))
        else:
            with st.spinner(f"Running {algorithm_name} on your puzzle…"):
                path, nodes, elapsed = run_solver(algorithm_name, start_state, goal_state)

            if path is None:
                st.warning(
                    f"{algorithm_name} did not find a solution within its exploration limits. "
                    "Try A* Search, BFS, or a puzzle with a shorter path."
                )
                record_solve(algorithm_name, start_state, goal_state, None, nodes, elapsed, False)
            elif tuple(path[0]) != tuple(start_state) or tuple(path[-1]) != tuple(goal_state):
                st.error("Internal verification error: solution path does not match start or goal state.")
            else:
                moves = len(path) - 1
                st.success(f"✅ Solved in **{moves} moves** using **{algorithm_name}**!")

                m1, m2, m3 = st.columns(3)
                m1.metric("Total Moves", moves)
                m2.metric("Nodes Explored", f"{nodes:,}")
                m3.metric("Execution Time", f"{elapsed:.4f}s")

                record_solve(algorithm_name, start_state, goal_state, moves, nodes, elapsed, True)

                # Store for animation and step sequence
                st.session_state.anim_path = path
                st.session_state.anim_start = start_state
                st.session_state.anim_goal = goal_state
                st.session_state.anim_step = 0

    # ── Step-by-Step Solution & Animation ─────────────────────────────────────
    if st.session_state.anim_path:
        path = st.session_state.anim_path
        start = st.session_state.get("anim_start", path[0])
        goal = st.session_state.get("anim_goal", path[-1])
        total = len(path) - 1

        st.markdown("---")
        st.subheader("🎬 Complete Step-by-Step Solution")

        # Initial and Goal boards side by side
        overview_col1, overview_col2 = st.columns(2)
        with overview_col1:
            st.caption("📌 Initial Board (Step 0)")
            display_board_html(start, size=60)
        with overview_col2:
            st.caption("🎯 Target Goal Board")
            display_board_html(goal, size=60)

        step = st.session_state.anim_step
        speed = st.slider("Animation Speed", 0.2, 2.0, 0.8, 0.1, key="anim_speed",
                          help="Seconds between auto-advance steps")

        ctrl1, ctrl2, ctrl3, ctrl4, ctrl5 = st.columns(5)
        with ctrl1:
            if st.button("⏮ First / Reset"):
                st.session_state.anim_step = 0
                st.rerun()
        with ctrl2:
            if st.button("◀ Prev Step") and step > 0:
                st.session_state.anim_step -= 1
                st.rerun()
        with ctrl3:
            if st.button("▶ Next Step") and step < total:
                st.session_state.anim_step += 1
                st.rerun()
        with ctrl4:
            if st.button("⏭ Last Step"):
                st.session_state.anim_step = total
                st.rerun()
        with ctrl5:
            if st.button("▶️ Play Animation"):
                for s in range(step, total + 1):
                    st.session_state.anim_step = s
                    time.sleep(speed)
                    st.rerun()

        # Progress bar
        pct = int(step / max(total, 1) * 100)
        st.markdown(
            f'<div class="quiz-progress"><div class="quiz-progress-fill" style="width:{pct}%"></div></div>',
            unsafe_allow_html=True,
        )

        cur_state = path[step]
        moved = find_moved_tile(path[step-1], cur_state) if step > 0 else None
        label = "Initial State" if step == 0 else ("Goal State Reached! 🎉" if step == total else f"Move {step}")

        board_col, info_col = st.columns([1, 1])
        with board_col:
            st.markdown(f"**Step {step} of {total}** — {label}")
            display_board_html(cur_state, moved_tile=moved, size=80)
        with info_col:
            st.markdown(f"**Board state:** `{list(cur_state)}`")
            if moved:
                st.markdown(f"**Tile moved:** `{moved}` into blank")
            st.markdown(f"**Moves remaining:** {total - step}")
            if step == total:
                st.balloons()

        # Full sequence overview expander
        with st.expander("📋 View Complete Step Sequence (Steps 0 to N)", expanded=False):
            st.caption("Browse all transitions from the initial state to the selected goal state:")
            # Display steps in groups of 4 per row
            for s_idx in range(0, len(path), 4):
                cols = st.columns(min(4, len(path) - s_idx))
                for c_idx, col in enumerate(cols):
                    cur_s = s_idx + c_idx
                    if cur_s < len(path):
                        with col:
                            m_tile = find_moved_tile(path[cur_s-1], path[cur_s]) if cur_s > 0 else None
                            step_title = "Step 0 (Start)" if cur_s == 0 else (f"Step {cur_s} (Goal)" if cur_s == total else f"Step {cur_s}")
                            st.caption(step_title)
                            display_board_html(path[cur_s], moved_tile=m_tile, size=48)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 3 — Algorithm Lab
# ─────────────────────────────────────────────────────────────────────────────
# ── Built-in benchmark puzzles for the Algorithm Lab ──────────────────────────
BENCHMARK_PUZZLES = [
    {
        "name": "Easy (2 moves)",
        "start": [1, 2, 3, 4, 5, 6, 7, 0, 8],
        "goal":  [1, 2, 3, 4, 5, 6, 7, 8, 0],
        "description": "Nearly solved — one tile out of place.",
    },
    {
        "name": "Medium (8 moves)",
        "start": [1, 2, 3, 4, 0, 6, 7, 5, 8],
        "goal":  [1, 2, 3, 4, 5, 6, 7, 8, 0],
        "description": "Moderate difficulty — a few tiles displaced.",
    },
    {
        "name": "Hard (16 moves)",
        "start": [5, 1, 2, 4, 0, 3, 7, 8, 6],
        "goal":  [1, 2, 3, 4, 5, 6, 7, 8, 0],
        "description": "Harder puzzle requiring planning ahead.",
    },
    {
        "name": "Very Hard (20+ moves)",
        "start": [8, 6, 7, 2, 5, 4, 3, 0, 1],
        "goal":  [1, 2, 3, 4, 5, 6, 7, 8, 0],
        "description": "Challenging puzzle — tests algorithm efficiency.",
    },
    {
        "name": "Classic Goal B",
        "start": [1, 2, 3, 4, 5, 6, 0, 7, 8],
        "goal":  [1, 2, 3, 4, 5, 6, 7, 8, 0],
        "description": "Standard benchmark with alternate goal layout.",
    },
]


def page_algo_lab():
    st.markdown('<div class="page-title">⚗️ Algorithm Lab</div>', unsafe_allow_html=True)
    st.caption("Compare any combination of search algorithms on the same built-in benchmark puzzle. All algorithms are tested on identical cases for a fair comparison.")

    # ── Benchmark selector ─────────────────────────────────────────────────
    st.subheader("📐 Select Benchmark Puzzle")
    bench_names = [b["name"] for b in BENCHMARK_PUZZLES]
    selected_bench = st.selectbox(
        "Choose a benchmark:",
        bench_names,
        key="lab_benchmark",
    )
    bench = next(b for b in BENCHMARK_PUZZLES if b["name"] == selected_bench)
    start = bench["start"]
    goal  = bench["goal"]

    # Preview the benchmark
    bcol1, bcol2, bcol3 = st.columns([1, 1, 2])
    with bcol1:
        st.caption("Start State")
        display_board_html(start, size=60)
    with bcol2:
        st.caption("Goal State")
        display_board_html(goal, size=60)
    with bcol3:
        st.info(
            f"**{bench['name']}**\n\n"
            f"{bench['description']}\n\n"
            f"Start: `{start}`\n\nGoal: `{goal}`"
        )

    # ── Algorithm selector ─────────────────────────────────────────────────
    st.markdown("---")
    st.subheader("🔬 Select Algorithms to Compare")
    algo_choices = st.multiselect(
        "Choose one or more algorithms:",
        list(ALGORITHMS.keys()),
        default=["A* Search", "Breadth-First Search (BFS)", "Greedy Best-First Search"],
        key="lab_algo_choices",
    )

    if st.button("🚀 Compare Algorithms", type="primary", use_container_width=True, key="lab_run"):
        if not algo_choices:
            st.warning("Please select at least one algorithm.")
            return
        if not is_solvable(start, goal):
            st.error("Internal error: benchmark puzzle is unsolvable. Please report this.")
            return

        results = []
        prog = st.progress(0)
        for idx, algo in enumerate(algo_choices):
            with st.spinner(f"Running {algo}…"):
                path, nodes, elapsed = run_solver(algo, start, goal)
            results.append({
                "Algorithm": algo,
                "Solved": "✅" if path else "❌",
                "Moves": len(path) - 1 if path else "—",
                "Nodes Explored": nodes,
                "Time (s)": round(elapsed, 4),
                "Optimal": "✅" if ALGO_INFO[algo]["optimal"] else "❌",
                "Complete": "✅" if ALGO_INFO[algo]["complete"] else "⚠️",
            })
            prog.progress(int((idx + 1) / len(algo_choices) * 100))

        prog.empty()
        st.markdown("---")
        st.subheader("📊 Comparison Results")
        st.caption(f"Benchmark: **{bench['name']}** · All algorithms ran on the same start/goal pair.")
        df = pd.DataFrame(results)
        st.dataframe(df, use_container_width=True, hide_index=True)

        # ── Charts ───────────────────────────────────────────────────────────
        solved_df = df[df["Solved"] == "✅"].copy()
        if not solved_df.empty:
            solved_df["Moves"] = pd.to_numeric(solved_df["Moves"], errors="coerce")

            chart_col1, chart_col2 = st.columns(2)
            with chart_col1:
                fig = px.bar(
                    solved_df, x="Algorithm", y="Time (s)",
                    title="Execution Time (seconds)",
                    color="Time (s)",
                    color_continuous_scale=["#2563eb", "#7c3aed"],
                    template="plotly_white",
                )
                fig.update_layout(
                    plot_bgcolor="#ffffff", paper_bgcolor="#ffffff",
                    font_color="#111827", showlegend=False,
                    title_font=dict(size=15, color="#111827", family="Outfit"),
                    xaxis=dict(tickangle=-30, tickfont=dict(color="#111827", size=11), title_font=dict(color="#111827")),
                    yaxis=dict(tickfont=dict(color="#111827", size=11), title_font=dict(color="#111827")),
                )
                st.plotly_chart(fig, use_container_width=True)

            with chart_col2:
                fig2 = px.bar(
                    solved_df, x="Algorithm", y="Nodes Explored",
                    title="Nodes Explored",
                    color="Nodes Explored",
                    color_continuous_scale=["#0284c7", "#7c3aed"],
                    template="plotly_white",
                )
                fig2.update_layout(
                    plot_bgcolor="#ffffff", paper_bgcolor="#ffffff",
                    font_color="#111827", showlegend=False,
                    title_font=dict(size=15, color="#111827", family="Outfit"),
                    xaxis=dict(tickangle=-30, tickfont=dict(color="#111827", size=11), title_font=dict(color="#111827")),
                    yaxis=dict(tickfont=dict(color="#111827", size=11), title_font=dict(color="#111827")),
                )
                st.plotly_chart(fig2, use_container_width=True)

            if not solved_df["Moves"].isna().all():
                fig3 = px.bar(
                    solved_df.dropna(subset=["Moves"]),
                    x="Algorithm", y="Moves",
                    title="Solution Length (Moves)",
                    color="Moves",
                    color_continuous_scale=["#059669", "#d97706"],
                    template="plotly_white",
                )
                fig3.update_layout(
                    plot_bgcolor="#ffffff", paper_bgcolor="#ffffff",
                    font_color="#111827", showlegend=False,
                    title_font=dict(size=15, color="#111827", family="Outfit"),
                    xaxis=dict(tickangle=-30, tickfont=dict(color="#111827", size=11), title_font=dict(color="#111827")),
                    yaxis=dict(tickfont=dict(color="#111827", size=11), title_font=dict(color="#111827")),
                )
                st.plotly_chart(fig3, use_container_width=True)

            # ── Summary ──────────────────────────────────────────────────────
            st.subheader("🏆 Results Summary")
            fastest = solved_df.loc[solved_df["Time (s)"].idxmin(), "Algorithm"]
            fewest_nodes = solved_df.loc[solved_df["Nodes Explored"].idxmin(), "Algorithm"]
            fewest_moves_df = solved_df.dropna(subset=["Moves"])
            fewest_moves = (
                fewest_moves_df.loc[fewest_moves_df["Moves"].idxmin(), "Algorithm"]
                if not fewest_moves_df.empty else "N/A"
            )
            st.info(
                f"**Fastest execution:** {fastest}  \n"
                f"**Fewest nodes explored:** {fewest_nodes}  \n"
                f"**Shortest solution (optimal path):** {fewest_moves}  \n\n"
                "Note — 'best' depends on your priority. "
                "A\\* balances optimality and efficiency. "
                "IDDFS uses the least memory. "
                "Bidirectional BFS is fastest on hard puzzles."
            )
        else:
            failed = ", ".join(df[df["Solved"] == "❌"]["Algorithm"].tolist())
            st.warning(
                f"None of the selected algorithms found a solution for this benchmark.\n\n"
                f"Failed algorithms: **{failed}**\n\n"
                "This may happen if DFS or DLS reach their depth limit on a hard puzzle. "
                "Try selecting A* or BFS."
            )

    # ── Algorithm reference table ─────────────────────────────────────────
    st.markdown("---")
    st.subheader("📚 Algorithm Reference")
    ref = []
    for name, info in ALGO_INFO.items():
        ref.append({
            "Algorithm": name,
            "Complete": "✅" if info["complete"] else "⚠️",
            "Optimal": "✅" if info["optimal"] else "❌",
            "Time": info["time"],
            "Space": info["space"],
            "Note": info["note"],
        })
    st.dataframe(pd.DataFrame(ref), use_container_width=True, hide_index=True)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 4 — AI Tutor
# ─────────────────────────────────────────────────────────────────────────────
def page_tutor():
    st.markdown('<div class="page-title">🤖 AI Tutor</div>', unsafe_allow_html=True)
    st.caption("Ask any question about AI search algorithms. Powered by a curated knowledge base.")

    # Suggested question chips
    st.markdown("**Suggested Questions:**")
    chip_cols = st.columns(3)
    for idx, q in enumerate(SUGGESTED_QUESTIONS[:9]):
        with chip_cols[idx % 3]:
            if st.button(q, key=f"chip_{idx}", use_container_width=True):
                st.session_state.chat_history.append({"role": "user", "content": q})
                bot_ans = answer_question(q, chat_history=st.session_state.chat_history)
                st.session_state.chat_history.append({"role": "bot", "content": bot_ans})
                st.rerun()

    with st.expander("More suggested questions"):
        more_cols = st.columns(3)
        for idx, q in enumerate(SUGGESTED_QUESTIONS[9:]):
            with more_cols[idx % 3]:
                if st.button(q, key=f"chip_more_{idx}", use_container_width=True):
                    st.session_state.chat_history.append({"role": "user", "content": q})
                    bot_ans = answer_question(q, chat_history=st.session_state.chat_history)
                    st.session_state.chat_history.append({"role": "bot", "content": bot_ans})
                    st.rerun()

    st.markdown("---")
    st.subheader("💬 Conversation")

    if st.session_state.chat_history:
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                st.markdown(
                    f'<div class="chat-user">🧑 {msg["content"]}</div>',
                    unsafe_allow_html=True,
                )
            else:
                with st.container():
                    st.markdown(
                        '<div style="background:#ffffff;border:1.5px solid #cbd5e1;'
                        'border-radius:10px;padding:1rem 1.25rem;margin:0.5rem 0;box-shadow:0 1px 3px rgba(0,0,0,0.06);">'
                        '<div style="font-weight:800;color:#1e40af;font-size:1.05rem;margin-bottom:0.5rem;">🤖 AI Tutor</div>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(msg['content'])
                    st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("Ask any question below or click one of the suggested questions above to get started.")

    # Input area
    st.markdown("---")
    q_col, send_col, clear_col = st.columns([5, 1, 1])
    with q_col:
        user_q = st.text_input("Your question:", placeholder="e.g. What is A* Search? How does Manhattan distance work?", key="tutor_input", label_visibility="collapsed")
    with send_col:
        if st.button("Send", type="primary", use_container_width=True):
            if user_q.strip():
                st.session_state.chat_history.append({"role": "user", "content": user_q.strip()})
                bot_ans = answer_question(user_q.strip(), chat_history=st.session_state.chat_history)
                st.session_state.chat_history.append({"role": "bot", "content": bot_ans})
                st.rerun()
    with clear_col:
        if st.button("Clear", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 5 — AI Quiz
# ─────────────────────────────────────────────────────────────────────────────
def page_quiz():
    st.markdown('<div class="page-title">📝 AI Learning Quiz</div>', unsafe_allow_html=True)
    st.caption(f"Test your knowledge of AI search algorithms with our comprehensive {len(QUIZ_QUESTIONS)}-question bank.")

    if not st.session_state.quiz_active:
        # Quiz setup
        st.subheader("Quiz Settings")
        c_set1, c_set2 = st.columns(2)
        with c_set1:
            difficulty = st.selectbox(
                "Difficulty Level",
                ["All Levels", "Beginner", "Intermediate", "Advanced"],
                key="quiz_diff_sel",
            )
        with c_set2:
            category = st.selectbox(
                "Algorithm / Topic Category",
                ["All Categories"] + sorted(set(q["category"] for q in QUIZ_QUESTIONS)),
                key="quiz_cat_sel",
            )

        pool = QUIZ_QUESTIONS.copy()
        if difficulty != "All Levels":
            pool = [q for q in pool if q["difficulty"] == difficulty]
        if category != "All Categories":
            pool = [q for q in pool if q["category"] == category]

        if not pool:
            st.warning("No questions match your selection. Try 'All Levels' or 'All Categories'.")
            return

        q_count_options = [5, 10, 15, 20, "All"]
        valid_q_opts = [opt for opt in q_count_options if opt == "All" or (isinstance(opt, int) and opt <= len(pool))]
        if not valid_q_opts:
            valid_q_opts = ["All"]
        q_limit = st.select_slider(
            "Number of Questions in this Quiz",
            options=valid_q_opts,
            value=valid_q_opts[min(1, len(valid_q_opts)-1)],
            key="quiz_limit_sel",
        )

        st.info(f"📚 {len(pool)} verified questions available for your selection.")

        if st.button("🚀 Start Quiz", type="primary", use_container_width=True):
            shuffled = pool.copy()
            random.shuffle(shuffled)
            if q_limit != "All" and isinstance(q_limit, int):
                shuffled = shuffled[:q_limit]
            st.session_state.quiz_questions = shuffled
            st.session_state.quiz_index = 0
            st.session_state.quiz_score = 0
            st.session_state.quiz_answered = False
            st.session_state.quiz_active = True
            st.session_state.quiz_difficulty = difficulty
            # Clear previous answers
            for k in list(st.session_state.keys()):
                if k.startswith("quiz_correct_") or k.startswith("quiz_user_choice_"):
                    del st.session_state[k]
            st.rerun()

        # Previous scores
        scores = get_quiz_scores(10)
        if scores:
            st.markdown("---")
            st.subheader("📈 Recent Quiz Scores")
            df = pd.DataFrame(scores)[["timestamp", "difficulty", "score", "total", "pct"]]
            df.columns = ["Date", "Difficulty", "Score", "Total", "Score %"]
            st.dataframe(df, use_container_width=True, hide_index=True)

    else:
        questions = st.session_state.quiz_questions
        idx = st.session_state.quiz_index
        total = len(questions)

        if idx >= total:
            # Quiz complete
            score = st.session_state.quiz_score
            pct = round(score / max(total, 1) * 100, 1)
            record_quiz(st.session_state.quiz_difficulty, score, total)

            st.balloons()
            st.subheader("🎉 Quiz Complete!")
            c1, c2, c3 = st.columns(3)
            c1.metric("Final Score", f"{score} / {total}")
            c2.metric("Percentage", f"{pct}%")
            grade = "🌟 Excellent Master" if pct >= 80 else ("👍 Good Effort" if pct >= 60 else "📖 Keep Studying")
            c3.metric("Result Grade", grade)

            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=pct,
                domain={"x": [0, 1], "y": [0, 1]},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "#3b82f6"},
                    "steps": [
                        {"range": [0, 60], "color": "#1e1b4b"},
                        {"range": [60, 80], "color": "#1e3a5f"},
                        {"range": [80, 100], "color": "#1a3a2a"},
                    ],
                    "threshold": {"value": 80, "line": {"color": "#10b981", "width": 3}},
                },
                title={"text": "Score %"},
                number={"suffix": "%"},
            ))
            fig.update_layout(
                height=260, paper_bgcolor="rgba(0,0,0,0)", font_color="#e2e8f0",
                margin=dict(l=20, r=20, t=30, b=20),
            )
            st.plotly_chart(fig, use_container_width=True)

            # Review of incorrect answers
            incorrect = [
                (i, q, st.session_state.get(f"quiz_user_choice_{i}", "None"))
                for i, q in enumerate(questions)
                if not st.session_state.get(f"quiz_correct_{i}", False)
            ]

            if incorrect:
                with st.expander(f"🔍 Review Incorrect Answers ({len(incorrect)} question{'s' if len(incorrect)>1 else ''})", expanded=True):
                    for i, q, user_choice in incorrect:
                        st.markdown(f"**Question {i+1}: {q['question']}**")
                        st.markdown(f"- ❌ **Your answer:** <span style='color:#ef4444;'>{user_choice}</span>", unsafe_allow_html=True)
                        st.markdown(f"- ✅ **Correct answer:** <span style='color:#10b981;font-weight:600;'>{q['options'][q['answer_index']]}</span>", unsafe_allow_html=True)
                        st.info(f"💡 **Explanation:** {q['explanation']}")
                        st.markdown("---")
            else:
                st.success("🎉 Perfect Score! You answered all questions correctly with zero errors.")

            if st.button("🔄 Restart Quiz", type="primary", use_container_width=True):
                st.session_state.quiz_active = False
                st.rerun()
        else:
            q = questions[idx]
            answered = st.session_state.quiz_answered

            # Progress
            pct = int(idx / total * 100)
            st.markdown(f"**Question {idx + 1} of {total}**  ·  Current Score: **{st.session_state.quiz_score}**")
            st.markdown(
                f'<div class="quiz-progress"><div class="quiz-progress-fill" style="width:{pct}%"></div></div>',
                unsafe_allow_html=True,
            )

            diff_color = {"Beginner": "#10b981", "Intermediate": "#f59e0b", "Advanced": "#ef4444"}.get(q["difficulty"], "#94a3b8")
            st.markdown(
                f'<span class="stat-badge" style="color:{diff_color};border-color:{diff_color}40;">'
                f'{q["difficulty"]}</span> '
                f'<span class="stat-badge">{q["category"]}</span>',
                unsafe_allow_html=True,
            )
            st.markdown(f"### {q['question']}")

            selected = st.radio(
                "Choose your answer:",
                q["options"],
                key=f"quiz_radio_{idx}",
                disabled=answered,
            )

            if not answered:
                if st.button("✅ Submit Answer", type="primary"):
                    chosen_idx = q["options"].index(selected)
                    correct = chosen_idx == q["answer_index"]
                    if correct:
                        st.session_state.quiz_score += 1
                    st.session_state.quiz_answered = True
                    st.session_state[f"quiz_correct_{idx}"] = correct
                    st.session_state[f"quiz_user_choice_{idx}"] = selected
                    st.rerun()
            else:
                correct = st.session_state.get(f"quiz_correct_{idx}", False)
                if correct:
                    st.success("✅ Correct!")
                else:
                    st.error(f"❌ Incorrect. The correct answer is: **{q['options'][q['answer_index']]}**")
                st.info(f"**Explanation:** {q['explanation']}")

                if st.button("➡️ Next Question", type="primary"):
                    st.session_state.quiz_index += 1
                    st.session_state.quiz_answered = False
                    st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 6 — Graph Search  (full 8-algorithm version)
# ─────────────────────────────────────────────────────────────────────────────

GRAPH_ALGO_OPTIONS = [
    "Breadth-First Search (BFS)",
    "Depth-First Search (DFS)",
    "A* Search",
    "Greedy Best-First Search",
    "Bidirectional Search",
    "Uniform Cost Search",
    "Depth-Limited Search",
    "Iterative Deepening DFS (IDDFS)",
]
HEURISTIC_ALGOS = {"A* Search", "Greedy Best-First Search"}

GRAPH_PRESETS = {
    "Weighted Network (Default)": {
        "edges": "A B 1\nA C 4\nB D 2\nB E 5\nC F 3\nD G 2\nE G 1\nF H 4\nG H 1",
        "start": "A",
        "goal": "H",
        "h": "A 7\nB 6\nC 5\nD 4\nE 3\nF 2\nG 1\nH 0",
    },
    "Romania Subgraph (Arad -> Bucharest)": {
        "edges": "Arad Zerind 75\nArad Sibiu 140\nArad Timisoara 118\nZerind Oradea 71\nOradea Sibiu 151\nTimisoara Lugoj 111\nLugoj Mehadia 70\nMehadia Drobeta 75\nDrobeta Craiova 120\nSibiu Fagaras 99\nSibiu Rimnicu_Vilcea 80\nRimnicu_Vilcea Craiova 146\nRimnicu_Vilcea Pitesti 97\nCraiova Pitesti 138\nFagaras Bucharest 211\nPitesti Bucharest 101",
        "start": "ARAD",
        "goal": "BUCHAREST",
        "h": "Arad 366\nZerind 374\nOradea 380\nTimisoara 329\nLugoj 244\nMehadia 241\nDrobeta 242\nCraiova 160\nSibiu 253\nRimnicu_Vilcea 193\nFagaras 176\nPitesti 100\nBucharest 0",
    },
    "Binary Tree (Depth 3)": {
        "edges": "1 2 1\n1 3 1\n2 4 1\n2 5 1\n3 6 1\n3 7 1",
        "start": "1",
        "goal": "7",
        "h": "1 2\n2 2\n3 1\n4 3\n5 3\n6 2\n7 0",
    },
    "Disconnected Graph (Unreachable Goal)": {
        "edges": "A B 2\nB C 3\nC A 1\nX Y 4\nY Z 2",
        "start": "A",
        "goal": "Z",
        "h": "A 10\nB 8\nC 9\nX 3\nY 2\nZ 0",
    },
}


def _run_graph_algo(algo_name, graph, edge_costs, heuristic, start, goal, limit, max_depth):
    kw = dict(graph=graph, start=start, goal=goal,
              edge_costs=edge_costs, heuristic=heuristic, directed=False)
    if "BFS" in algo_name and "Bidirectional" not in algo_name:
        return bfs_graph(**kw)
    elif "DFS" in algo_name and "IDDFS" not in algo_name and "Depth-Limited" not in algo_name:
        return dfs_graph(**kw)
    elif "A*" in algo_name:
        return astar_graph(**kw)
    elif "Greedy" in algo_name:
        return greedy_graph(**kw)
    elif "Bidirectional" in algo_name:
        return bidirectional_graph(**kw)
    elif "Uniform Cost" in algo_name or "UCS" in algo_name:
        return ucs_graph(**kw)
    elif "Depth-Limited" in algo_name:
        return depth_limited_graph(graph=graph, start=start, goal=goal, limit=limit)
    elif "IDDFS" in algo_name:
        return iddfs_graph(graph=graph, start=start, goal=goal, max_depth=max_depth)
    else:
        raise ValueError(f"Unknown algorithm: {algo_name}")


def page_graph():
    st.markdown('<div class="page-title">🕸️ Graph Search Solver</div>', unsafe_allow_html=True)
    st.caption(
        "Define a graph with nodes and edges, choose start and goal nodes, "
        "pick one of **all 8 AI search algorithms**, and inspect the traversal and solution path step by step."
    )

    # Preset selector
    c_preset, c_load = st.columns([4, 1])
    with c_preset:
        preset_choice = st.selectbox("📂 Graph Presets", list(GRAPH_PRESETS.keys()), key="graph_preset_select")
    with c_load:
        st.write("")
        st.write("")
        if st.button("Apply Preset", use_container_width=True):
            data = GRAPH_PRESETS[preset_choice]
            st.session_state.graph_edges = data["edges"]
            st.session_state.graph_start = data["start"]
            st.session_state.graph_goal = data["goal"]
            st.session_state.graph_heuristic = data["h"]
            st.session_state.graph_result = None
            st.rerun()

    init_edges = st.session_state.get("graph_edges", GRAPH_PRESETS["Weighted Network (Default)"]["edges"])
    init_start = st.session_state.get("graph_start", "A")
    init_goal = st.session_state.get("graph_goal", "H")
    init_h = st.session_state.get("graph_heuristic", GRAPH_PRESETS["Weighted Network (Default)"]["h"])

    st.subheader("Graph Definition & Parameters")
    st.caption("Format: `NodeA NodeB` (weight=1) or `NodeA NodeB cost`. One edge per line.")
    edge_text = st.text_area("Edges", value=init_edges, height=140, key="graph_edges")

    c1, c2, c3 = st.columns(3)
    with c1:
        start_node = st.text_input("Start Node", value=init_start, key="graph_start").strip().upper()
    with c2:
        goal_node = st.text_input("Goal Node", value=init_goal, key="graph_goal").strip().upper()
    with c3:
        graph_algo = st.selectbox("Algorithm (All 8 Supported)", GRAPH_ALGO_OPTIONS, key="graph_algo")

    depth_limit = 10
    max_depth = 20
    heuristic = {}

    if graph_algo in HEURISTIC_ALGOS:
        with st.expander("🎯 Heuristic Values h(n) — for Informed Search", expanded=True):
            st.caption(
                "Enter estimated distances to goal (one per line: `Node value`). "
                "If omitted, h(n)=0 is used (A* reduces to UCS; Greedy searches purely by unweighted tie-break)."
            )
            h_text = st.text_area("Heuristic Values", value=init_h, height=110, key="graph_heuristic")
            for line in h_text.strip().splitlines():
                parts = line.strip().split()
                if len(parts) >= 2:
                    try:
                        heuristic[parts[0].upper()] = float(parts[1])
                    except ValueError:
                        pass

    if graph_algo == "Depth-Limited Search":
        depth_limit = st.slider("Depth Limit (L)", min_value=1, max_value=50, value=10, key="graph_dls_limit")
    elif graph_algo == "Iterative Deepening DFS (IDDFS)":
        max_depth = st.slider("Maximum Depth for IDDFS", min_value=1, max_value=50, value=20, key="graph_iddfs_max")

    if st.button("🔍 Search Graph", type="primary", use_container_width=True, key="graph_search_btn"):
        try:
            graph, edge_costs = parse_edges(edge_text)
        except Exception as e:
            st.error(f"Could not parse edges: {e}")
            return

        if not graph:
            st.error("No valid edges found in graph definition.")
            return
        if start_node not in graph:
            st.error(f"Start node '{start_node}' not found in the graph.")
            return
        if goal_node not in graph:
            st.error(f"Goal node '{goal_node}' not found in the graph.")
            return

        start_t = time.perf_counter()
        try:
            path, traversal, nodes = _run_graph_algo(
                graph_algo, graph, edge_costs, heuristic,
                start_node, goal_node, depth_limit, max_depth,
            )
        except Exception as e:
            st.error(f"Algorithm error: {e}")
            return
        elapsed = time.perf_counter() - start_t

        st.session_state.graph_result = {
            "path": path,
            "traversal": traversal,
            "nodes": nodes,
            "elapsed": elapsed,
            "edge_costs": edge_costs,
            "graph": graph,
            "start_node": start_node,
            "goal_node": goal_node,
            "algo": graph_algo,
            "edge_text": edge_text,
            "depth_limit": depth_limit,
            "max_depth": max_depth,
        }

    # Render results if available
    res = st.session_state.get("graph_result")
    if res and res.get("graph"):
        path = res["path"]
        traversal = res["traversal"]
        nodes = res["nodes"]
        elapsed = res["elapsed"]
        edge_costs = res["edge_costs"]
        s_node = res["start_node"]
        g_node = res["goal_node"]
        cur_algo = res["algo"]

        st.markdown("---")
        st.subheader("Search Results")

        has_weights = any(v != 1.0 for v in edge_costs.values())
        if has_weights and "Breadth-First Search" in cur_algo:
            st.warning(
                "⚠️ **Algorithm Property Note**: BFS treats all edges with equal unit cost (weight = 1). "
                "It finds the path with the fewest edges, which may not be the path of minimum total cost. "
                "Use **Uniform Cost Search** or **A\\*** for cost-optimal paths on weighted graphs."
            )

        r1, r2, r3, r4 = st.columns(4)
        r1.metric("Path Length (Edges)", len(path) - 1 if path else "None")
        if path:
            cost_val = sum(
                edge_costs.get((path[i], path[i+1]), edge_costs.get((path[i+1], path[i]), 1.0))
                for i in range(len(path) - 1)
            )
            r2.metric("Total Path Cost", f"{cost_val:.2f}" if cost_val != int(cost_val) else str(int(cost_val)))
        else:
            r2.metric("Total Path Cost", "—")
        r3.metric("Nodes Explored", nodes)
        r4.metric("Execution Time", f"{elapsed*1000:.2f} ms")

        if path:
            st.success(f"✅ **Solution Path Found ({len(path)} nodes):** {' ➔ '.join(path)}")
        else:
            if "Depth-Limited" in cur_algo:
                st.error(f"❌ No path found from **{s_node}** to **{g_node}** within depth limit {res.get('depth_limit', 10)}. Try increasing the depth limit.")
            elif "IDDFS" in cur_algo:
                st.error(f"❌ No path found from **{s_node}** to **{g_node}** within max depth {res.get('max_depth', 20)}.")
            else:
                st.error(f"❌ No path exists between **{s_node}** and **{g_node}** in this graph.")

        if traversal:
            st.markdown(f"**Traversal Order ({len(traversal)} steps):** " + " ➔ ".join([f"`{n}`" for n in traversal]))

        # Step-by-step traversal playback
        st.subheader("Step-by-Step Traversal Inspection & Visualisation")
        if traversal:
            step_idx = st.slider(
                "Inspect search traversal up to step:",
                min_value=1,
                max_value=len(traversal),
                value=len(traversal),
                help="Slide to see the graph state at each step of node expansion",
                key="graph_traversal_step_slider"
            )
            cur_visited = set(traversal[:step_idx])
            active_node = traversal[step_idx - 1]
            st.caption(f"📍 **Step {step_idx} of {len(traversal)}:** Exploring Node **`{active_node}`** · Visited {len(cur_visited)} unique node(s) so far")
        else:
            cur_visited = set()
            active_node = None

        # Visualise graph using NetworkX and Plotly
        try:
            import networkx as nx
            G = nx.Graph()
            for line in res["edge_text"].strip().splitlines():
                parts = line.strip().split()
                if len(parts) >= 2:
                    a, b = parts[0].upper(), parts[1].upper()
                    w = float(parts[2]) if len(parts) >= 3 else 1.0
                    G.add_edge(a, b, weight=w)

            pos = nx.spring_layout(G, seed=42)
            node_path = set(path) if (path and (not traversal or step_idx == len(traversal))) else set()
            edge_path_set = set()
            if path and (not traversal or step_idx == len(traversal)):
                for i in range(len(path) - 1):
                    edge_path_set.add((path[i], path[i+1]))
                    edge_path_set.add((path[i+1], path[i]))

            edge_traces = []
            for u, v, d in G.edges(data=True):
                x0, y0 = pos[u]
                x1, y1 = pos[v]
                on_path = (u, v) in edge_path_set
                c = "#8b5cf6" if on_path else "rgba(148, 163, 184, 0.25)"
                w_line = 4.0 if on_path else 1.5
                edge_traces.append(go.Scatter(
                    x=[x0, x1, None], y=[y0, y1, None],
                    mode="lines",
                    line=dict(color=c, width=w_line),
                    hoverinfo="none",
                ))
                if has_weights:
                    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
                    wt = d.get("weight", 1)
                    wt_str = str(int(wt)) if wt == int(wt) else f"{wt:.1f}"
                    edge_traces.append(go.Scatter(
                        x=[mx], y=[my], mode="text",
                        text=[wt_str],
                        textfont=dict(color="#0f172a", size=12, family="Inter, monospace", weight="bold"),
                        hoverinfo="none",
                    ))

            node_x, node_y, node_text, node_color, node_size = [], [], [], [], []
            for node in G.nodes():
                x, y = pos[node]
                node_x.append(x)
                node_y.append(y)
                node_text.append(node)
                if node == active_node:
                    node_color.append("#d97706")  # Amber gold for currently active node
                    node_size.append(34)
                elif node == s_node:
                    node_color.append("#059669")  # Emerald green for start
                    node_size.append(30)
                elif node == g_node:
                    node_color.append("#dc2626")  # Ruby red for goal
                    node_size.append(30)
                elif node in node_path:
                    node_color.append("#7c3aed")  # Vivid purple for solution path
                    node_size.append(28)
                elif node in cur_visited:
                    node_color.append("#ea580c")  # Orange for explored nodes
                    node_size.append(24)
                else:
                    node_color.append("#2563eb")  # Royal blue for unvisited
                    node_size.append(22)

            node_trace = go.Scatter(
                x=node_x, y=node_y, mode="markers+text",
                text=node_text, textposition="top center",
                marker=dict(size=node_size, color=node_color, line=dict(width=2, color="#ffffff")),
                textfont=dict(color="#111827", size=13, family="Outfit, sans-serif", weight="bold"),
                hoverinfo="text",
            )
            fig = go.Figure(data=edge_traces + [node_trace])
            fig.update_layout(
                showlegend=False,
                paper_bgcolor="#ffffff",
                plot_bgcolor="#f8fafc",
                font_color="#111827",
                height=460,
                margin=dict(l=15, r=15, t=30, b=15),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            )
            st.plotly_chart(fig, use_container_width=True)
            st.caption(
                "🟢 **Start**  ·  🔴 **Goal**  ·  🟡 **Current Active Node**  ·  🟠 **Visited**  ·  🟣 **Solution Path**  ·  🔵 **Unvisited**"
            )
        except ImportError:
            st.info("Install networkx for interactive graph visualization: `pip install networkx`")


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 7 — Water Jug Solver
# ─────────────────────────────────────────────────────────────────────────────
def page_water_jug():
    st.markdown('<div class="page-title">🪣 Water Jug Solver</div>', unsafe_allow_html=True)
    st.caption("Solve the classic water jug problem using BFS state-space search.")

    c1, c2, c3 = st.columns(3)
    with c1:
        cap_a = st.number_input("Capacity of Jug A (L)", min_value=1, max_value=50, value=4, key="wj_a")
    with c2:
        cap_b = st.number_input("Capacity of Jug B (L)", min_value=1, max_value=50, value=3, key="wj_b")
    with c3:
        target = st.number_input("Target Amount (L)", min_value=1, max_value=50, value=2, key="wj_target")

    # Solvability hint
    from math import gcd
    g = gcd(int(cap_a), int(cap_b))
    if int(target) % g != 0 or int(target) > max(int(cap_a), int(cap_b)):
        st.warning(
            f"Note: target {int(target)}L may be impossible. "
            f"GCD({int(cap_a)},{int(cap_b)})={g}. Target must be a multiple of {g} and ≤ {max(int(cap_a), int(cap_b))}."
        )

    if st.button("🔍 Solve Water Jug", type="primary", use_container_width=True):
        with st.spinner("Searching…"):
            steps, nodes = solve_water_jug(int(cap_a), int(cap_b), int(target))

        if steps is None:
            st.error(
                f"No solution found. The target {int(target)}L cannot be measured with "
                f"jugs of {int(cap_a)}L and {int(cap_b)}L."
            )
        else:
            st.success(f"✅ Solved in **{len(steps)-1} operations**!")
            s1, s2 = st.columns(2)
            s1.metric("Steps", len(steps) - 1)
            s2.metric("Nodes Explored", nodes)

            st.markdown("---")
            st.subheader("Step-by-Step Solution")

            for i, step in enumerate(steps):
                a_pct = step["a"] / int(cap_a) * 100 if int(cap_a) > 0 else 0
                b_pct = step["b"] / int(cap_b) * 100 if int(cap_b) > 0 else 0

                with st.expander(f"Step {i}: {step['action']}", expanded=(i == 0 or i == len(steps)-1)):
                    j1, j2, j3 = st.columns([2, 2, 3])
                    with j1:
                        st.markdown(
                            f'<div style="text-align:center;">'
                            f'<div class="jug-bar-outer">'
                            f'<div class="jug-bar-fill" style="height:{a_pct}%;"></div>'
                            f'</div>'
                            f'<b>Jug A</b><br>{step["a"]}L / {int(cap_a)}L'
                            f'</div>',
                            unsafe_allow_html=True,
                        )
                    with j2:
                        st.markdown(
                            f'<div style="text-align:center;">'
                            f'<div class="jug-bar-outer">'
                            f'<div class="jug-bar-fill" style="height:{b_pct}%;"></div>'
                            f'</div>'
                            f'<b>Jug B</b><br>{step["b"]}L / {int(cap_b)}L'
                            f'</div>',
                            unsafe_allow_html=True,
                        )
                    with j3:
                        st.markdown(f"**Action:** {step['action']}")
                        st.markdown(f"**State:** ({step['a']}, {step['b']})")
                        if step["a"] == int(target) or step["b"] == int(target):
                            st.success("🎯 Target achieved!")


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 8 — History & Reports
# ─────────────────────────────────────────────────────────────────────────────
def page_history():
    st.markdown('<div class="page-title">📊 History & Reports</div>', unsafe_allow_html=True)
    st.caption("Review your puzzle-solving and quiz history. All data is stored locally.")

    tab_solve, tab_quiz = st.tabs(["🧩 Solve History", "📝 Quiz Scores"])

    with tab_solve:
        history = get_solve_history(200)
        if not history:
            st.info("No solve history yet. Solve a puzzle to record results.")
        else:
            df = pd.DataFrame(history)
            df["success"] = df["success"].map({1: "✅", 0: "❌"})
            df = df[["timestamp", "algorithm", "start_state", "goal_state", "moves", "nodes", "elapsed", "success"]]
            df.columns = ["Time", "Algorithm", "Start", "Goal", "Moves", "Nodes", "Time (s)", "Success"]

            # Filters
            fc1, fc2 = st.columns(2)
            with fc1:
                algo_filter = st.multiselect("Filter by Algorithm", df["Algorithm"].unique().tolist())
            with fc2:
                success_filter = st.selectbox("Filter by Result", ["All", "✅ Solved", "❌ Failed"])

            if algo_filter:
                df = df[df["Algorithm"].isin(algo_filter)]
            if success_filter == "✅ Solved":
                df = df[df["Success"] == "✅"]
            elif success_filter == "❌ Failed":
                df = df[df["Success"] == "❌"]

            st.dataframe(df, use_container_width=True, hide_index=True)

            # Download CSV
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("📥 Download CSV", csv, "solve_history.csv", "text/csv")

            # Algorithm usage chart
            if len(df) > 1:
                algo_counts = df["Algorithm"].value_counts().reset_index()
                algo_counts.columns = ["Algorithm", "Count"]
                fig = px.pie(
                    algo_counts, names="Algorithm", values="Count",
                    title="Algorithm Usage", template="plotly_white",
                    color_discrete_sequence=px.colors.sequential.Tealgrn,
                )
                fig.update_layout(
                    paper_bgcolor="#ffffff", font_color="#111827", height=320,
                    title_font=dict(color="#111827", size=14, family="Outfit"),
                )
                st.plotly_chart(fig, use_container_width=True)

    with tab_quiz:
        scores = get_quiz_scores(100)
        if not scores:
            st.info("No quiz scores yet. Take the quiz to record your performance.")
        else:
            df_q = pd.DataFrame(scores)[["timestamp", "difficulty", "score", "total", "pct"]]
            df_q.columns = ["Date", "Difficulty", "Score", "Total", "Score %"]
            st.dataframe(df_q, use_container_width=True, hide_index=True)

            fig = px.line(
                df_q.iloc[::-1], x="Date", y="Score %",
                title="Quiz Score Trend", template="plotly_white",
                color="Difficulty",
                markers=True,
            )
            fig.update_layout(
                paper_bgcolor="#ffffff", font_color="#111827", height=300,
                title_font=dict(color="#111827", size=14, family="Outfit"),
                xaxis=dict(tickfont=dict(color="#111827")),
                yaxis=dict(tickfont=dict(color="#111827")),
            )
            st.plotly_chart(fig, use_container_width=True)

            csv_q = df_q.to_csv(index=False).encode("utf-8")
            st.download_button("📥 Download Quiz CSV", csv_q, "quiz_scores.csv", "text/csv")


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 9 — About
# ─────────────────────────────────────────────────────────────────────────────
def page_about():
    st.markdown('<div class="page-title">ℹ️ About This Project</div>', unsafe_allow_html=True)

    st.markdown("""
## Project Title
**AI-Based Search & Puzzle Solver**

## Problem Statement
Classical search problems such as the 8-puzzle provide an ideal testbed for comparing AI search algorithms.
This project implements, visualises, and compares eight search strategies, making abstract algorithmic
concepts tangible through interactive demonstrations.

## Motivation
Students learning Artificial Intelligence often struggle to understand why different search algorithms
produce different results. This application bridges that gap by letting users experiment with real
puzzles and observe how algorithm design choices affect performance.

## Objectives
- Implement and compare 8 AI search algorithms on the 8-puzzle.
- Provide image-based puzzle input via OCR.
- Enable user-defined start and goal states.
- Visualise the solution step-by-step.
- Educate users through an AI tutor and interactive quiz.
- Extend learning to Graph Search and the Water Jug problem.
- Record and report solve history and quiz scores.

## System Workflow
1. **Input** — User enters a puzzle manually, shuffles randomly, or uploads an image.
2. **Validation** — The application checks for valid tile sets and solvability (inversion parity).
3. **Search** — The selected algorithm explores the state space and returns a solution path.
4. **Visualisation** — The solution is animated step-by-step with tile highlighting.
5. **Statistics** — Execution time, nodes explored, and move count are displayed.
6. **Storage** — Results are recorded in a local SQLite database.
""")

    st.markdown("---")
    st.subheader("Algorithms Implemented")
    for name, info in ALGO_INFO.items():
        with st.expander(name):
            st.markdown(
                f"- **Complete:** {'Yes' if info['complete'] else 'No (with depth limit)'}  \n"
                f"- **Optimal:** {'Yes' if info['optimal'] else 'No'}  \n"
                f"- **Time complexity:** {info['time']}  \n"
                f"- **Space complexity:** {info['space']}  \n"
                f"- {info['note']}"
            )

    st.markdown("---")
    st.subheader("Technologies Used")
    st.markdown("""
| Technology | Purpose |
|-----------|---------|
| Python 3.13 | Core programming language |
| Streamlit 1.65 | Web UI framework |
| Plotly 7 | Interactive charts |
| Pillow 12 | Image processing |
| pytesseract | OCR tile recognition |
| SQLite | Local result storage |
| NetworkX | Graph visualisation |
| pandas | Data handling and reports |
""")

    st.markdown("---")
    st.subheader("Limitations")
    st.markdown("""
- **OCR accuracy** depends on image quality. A clear, well-cropped image is required.
- **DFS and DLS** may not find optimal solutions; they use depth limits of 30/50.
- **IDDFS** can be slow on very hard puzzles due to repeated node re-expansion.
- The AI Tutor uses a local knowledge base; it does not use a generative AI model.
- Graph A* requires manually supplied heuristic values.
""")

    st.markdown("---")
    st.subheader("Future Enhancements")
    st.markdown("""
- Integration with an optional LLM API for the AI Tutor.
- Support for larger (15-puzzle, 24-puzzle) configurations.
- Pattern database heuristics for stronger A* performance.
- Automated test generation and CI/CD pipeline.
- Mobile-responsive improvements.
- PDF report export with full solution diagrams.
""")

    st.markdown("---")
    st.caption("Academic Project | Artificial Intelligence | 8-Puzzle Solver with Search Algorithms")


# ─────────────────────────────────────────────────────────────────────────────
# Router
# ─────────────────────────────────────────────────────────────────────────────
PAGE_MAP = {
    "Home Dashboard":   page_home,
    "8-Puzzle Solver":  page_puzzle,
    "Algorithm Lab":    page_algo_lab,
    "AI Tutor":         page_tutor,
    "AI Quiz":          page_quiz,
    "Graph Search":     page_graph,
    "Water Jug Solver": page_water_jug,
    "History & Reports": page_history,
    "About":            page_about,
}

current_page = st.session_state.get("page", "Home Dashboard")
if current_page in PAGE_MAP:
    PAGE_MAP[current_page]()
else:
    page_home()
