"""
Shared CSS theme for the AI Search & Puzzle Solver Streamlit app.
High-contrast, professional academic design with dark, legible text on light backgrounds
and high-contrast text on dark accent elements.
"""

GLOBAL_CSS = """
<style>
/* ─── Google Fonts ─────────────────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800;900&display=swap');

/* ─── Root Variables ────────────────────────────────────────────────────── */
:root {
    --bg-page: #f8fafc;
    --bg-card: #ffffff;
    --bg-card-secondary: #f1f5f9;
    --border: #e2e8f0;
    --border-strong: #cbd5e1;
    
    /* High-contrast typography colors per requirements */
    --text-heading: #111827;      /* Strong near-black for headings */
    --text-body: #1f2937;         /* Dark charcoal for main body text */
    --text-muted: #374151;        /* Darker, easy-to-read captions & labels */
    --text-dim: #4b5563;          /* Secondary description text */
    
    /* Brand Accents */
    --blue-primary: #2563eb;
    --blue-dark: #1d4ed8;
    --purple-primary: #7c3aed;
    --purple-dark: #6d28d9;
    --green-success: #059669;
    --red-error: #dc2626;
    --amber-warning: #d97706;
    
    --radius: 12px;
    --radius-sm: 8px;
    --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.08), 0 1px 2px rgba(0, 0, 0, 0.04);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -1px rgba(0, 0, 0, 0.04);
}

/* ─── Global Reset & Body Typography ────────────────────────────────────── */
html, body, [class*="css"], [data-testid="stAppViewContainer"], .stApp {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
    color: var(--text-body) !important;
    background-color: var(--bg-page) !important;
}

p, span, div, li {
    color: var(--text-body);
}

/* ─── Headings ───────────────────────────────────────────────────────────── */
h1, h2, h3, h4, h5, h6,
[data-testid="stHeading"],
[data-testid="stHeader"] {
    font-family: 'Outfit', sans-serif !important;
    color: var(--text-heading) !important;
    letter-spacing: -0.02em !important;
    font-weight: 700 !important;
}

h1 { font-size: 2.2rem !important; font-weight: 800 !important; color: #111827 !important; }
h2 { font-size: 1.5rem !important; font-weight: 700 !important; color: #111827 !important; margin-top: 1rem !important; }
h3 { font-size: 1.2rem !important; font-weight: 600 !important; color: #111827 !important; }

/* Page title gradient */
.page-title {
    color: #111827 !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 800 !important;
    font-size: 2.1rem !important;
    margin-bottom: 0.35rem !important;
    display: inline-block !important;
}

/* ─── Labels, Captions & Descriptions ───────────────────────────────────── */
label,
[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span {
    color: var(--text-heading) !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
}

.stCaption,
[data-testid="stCaptionContainer"],
small,
caption,
.caption-dark {
    color: var(--text-muted) !important;
    font-size: 0.88rem !important;
    font-weight: 500 !important;
    line-height: 1.5 !important;
}

/* ─── Sidebar Navigation ────────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background-color: #ffffff !important;
    border-right: 1.5px solid var(--border) !important;
}

[data-testid="stSidebar"] * {
    color: var(--text-body);
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: var(--text-heading) !important;
}

[data-testid="stSidebar"] .stButton > button {
    background-color: #ffffff !important;
    color: var(--text-heading) !important;
    font-weight: 600 !important;
    border: 1.5px solid #e2e8f0 !important;
    text-align: left !important;
    justify-content: flex-start !important;
    box-shadow: none !important;
    padding: 0.55rem 0.9rem !important;
    border-radius: var(--radius-sm) !important;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background-color: #f1f5f9 !important;
    border-color: #cbd5e1 !important;
    color: #1d4ed8 !important;
}

/* ─── Input Fields (Text, Number, Area, Selectbox) ───────────────────────── */
/* Requirement 4: dark text (#111827) with light background (#FFFFFF) */
.stTextInput input,
.stNumberInput input,
.stTextArea textarea,
[data-baseweb="input"] input,
[data-baseweb="base-input"] input,
[data-baseweb="textarea"] textarea {
    background-color: #ffffff !important;
    color: #111827 !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    border: 1.5px solid var(--border-strong) !important;
    border-radius: var(--radius-sm) !important;
}

.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus,
[data-baseweb="input"]:focus-within {
    border-color: var(--blue-primary) !important;
    box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2) !important;
    color: #111827 !important;
}

/* Dropdowns & Selectboxes */
.stSelectbox [data-baseweb="select"],
.stSelectbox > div > div {
    background-color: #ffffff !important;
    border: 1.5px solid var(--border-strong) !important;
    border-radius: var(--radius-sm) !important;
    color: #111827 !important;
}

.stSelectbox [data-baseweb="select"] * {
    color: #111827 !important;
    font-weight: 600 !important;
}

[data-baseweb="popover"],
[data-baseweb="menu"],
[data-baseweb="menu"] ul,
[data-baseweb="menu"] li {
    background-color: #ffffff !important;
    color: #111827 !important;
    font-weight: 500 !important;
}

[data-baseweb="menu"] li:hover,
[aria-selected="true"] {
    background-color: #eff6ff !important;
    color: #1d4ed8 !important;
}

/* Radio buttons */
[data-testid="stRadio"] label,
[data-testid="stRadio"] label p,
[data-testid="stRadio"] label span {
    color: var(--text-body) !important;
    font-weight: 500 !important;
}

/* ─── Buttons ───────────────────────────────────────────────────────────── */
/* Requirement 5: strong contrast in normal, hover, active, disabled */
.stButton > button {
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    border-radius: var(--radius-sm) !important;
    padding: 0.5rem 1rem !important;
    transition: all 0.2s ease !important;
}

/* Primary Button */
.stButton > button[kind="primary"],
.stButton > button[data-testid="baseButton-primary"] {
    background-color: #1d4ed8 !important;
    background-image: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
    color: #ffffff !important;
    border: 1px solid #1e40af !important;
    box-shadow: 0 2px 4px rgba(29, 78, 216, 0.25) !important;
}

.stButton > button[kind="primary"]:hover,
.stButton > button[data-testid="baseButton-primary"]:hover {
    background-color: #1e40af !important;
    background-image: none !important;
    color: #ffffff !important;
    box-shadow: 0 4px 8px rgba(29, 78, 216, 0.35) !important;
    transform: translateY(-1px) !important;
}

/* Secondary / Default Button */
.stButton > button:not([kind="primary"]):not([data-testid="baseButton-primary"]) {
    background-color: #ffffff !important;
    color: #111827 !important;
    border: 1.5px solid #cbd5e1 !important;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05) !important;
}

.stButton > button:not([kind="primary"]):not([data-testid="baseButton-primary"]):hover {
    background-color: #f8fafc !important;
    border-color: #94a3b8 !important;
    color: #1d4ed8 !important;
    transform: translateY(-1px) !important;
}

.stButton > button:disabled {
    background-color: #e2e8f0 !important;
    color: #64748b !important;
    border-color: #cbd5e1 !important;
    cursor: not-allowed !important;
    transform: none !important;
}

/* ─── Metric Cards ──────────────────────────────────────────────────────── */
[data-testid="stMetric"] {
    background-color: #ffffff !important;
    border: 1.5px solid var(--border) !important;
    border-radius: var(--radius) !important;
    padding: 1rem 1.25rem !important;
    box-shadow: var(--shadow-sm) !important;
}

[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] p {
    color: var(--text-muted) !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
}

[data-testid="stMetricValue"],
[data-testid="stMetricValue"] div {
    font-family: 'Outfit', sans-serif !important;
    font-weight: 800 !important;
    font-size: 1.85rem !important;
    color: #111827 !important;
    background: none !important;
    -webkit-text-fill-color: #111827 !important;
}

/* ─── 8-Puzzle Tiles ────────────────────────────────────────────────────── */
/* Requirement 6: Make 8-puzzle numbers, tile labels highly visible */
.puzzle-tile {
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 800 !important;
    border-radius: 10px;
    margin: 3px;
    transition: all 0.2s ease;
    user-select: none;
}

.puzzle-tile-filled {
    background-color: #ffffff !important;
    border: 2.5px solid #2563eb !important;
    color: #1e3a8a !important;
    font-size: 1.85rem !important;
    box-shadow: 0 3px 8px rgba(37, 99, 235, 0.18) !important;
}

.puzzle-tile-blank {
    background-color: #f1f5f9 !important;
    border: 2px dashed #94a3b8 !important;
    color: transparent !important;
}

.puzzle-tile-moved {
    background-color: #7c3aed !important;
    border: 2.5px solid #5b21b6 !important;
    color: #ffffff !important;
    font-size: 1.85rem !important;
    box-shadow: 0 4px 12px rgba(124, 58, 237, 0.35) !important;
    transform: scale(1.05);
}

/* ─── Cards & Feature Containers ────────────────────────────────────────── */
/* Requirement 8: Darken table text, column headers, card descriptions */
.feature-card {
    background-color: #ffffff !important;
    border: 1.5px solid var(--border) !important;
    border-radius: var(--radius) !important;
    padding: 1.4rem 1.2rem !important;
    text-align: center !important;
    transition: all 0.25s ease !important;
    box-shadow: var(--shadow-sm) !important;
    height: 100% !important;
}

.feature-card:hover {
    border-color: #93c5fd !important;
    box-shadow: var(--shadow-md) !important;
    transform: translateY(-2px) !important;
}

.feature-card .icon {
    font-size: 2.2rem;
    margin-bottom: 0.6rem;
    display: block;
}

.feature-card h3 {
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    color: #111827 !important;
    margin-bottom: 0.4rem !important;
}

.feature-card p {
    font-size: 0.88rem !important;
    color: var(--text-muted) !important;
    line-height: 1.5 !important;
    font-weight: 400 !important;
}

/* ─── Chat Bubbles (AI Tutor) ───────────────────────────────────────────── */
.chat-user {
    background-color: #2563eb !important;
    color: #ffffff !important;
    font-weight: 500 !important;
    padding: 0.75rem 1.1rem !important;
    border-radius: 14px 14px 4px 14px !important;
    margin: 0.45rem 0 !important;
    max-width: 85% !important;
    margin-left: auto !important;
    font-size: 0.95rem !important;
    box-shadow: 0 2px 4px rgba(37, 99, 235, 0.2) !important;
}

.chat-user * {
    color: #ffffff !important;
}

.chat-bot {
    background-color: #ffffff !important;
    border: 1.5px solid #e2e8f0 !important;
    color: var(--text-body) !important;
    padding: 1rem 1.2rem !important;
    border-radius: 4px 14px 14px 14px !important;
    margin: 0.45rem 0 !important;
    max-width: 92% !important;
    font-size: 0.95rem !important;
    line-height: 1.65 !important;
    box-shadow: var(--shadow-sm) !important;
}

.chat-bot h1, .chat-bot h2, .chat-bot h3, .chat-bot strong, .chat-bot b {
    color: #111827 !important;
}

/* ─── Stat Badges & Tags ────────────────────────────────────────────────── */
.stat-badge {
    display: inline-block;
    background-color: #eff6ff !important;
    border: 1px solid #bfdbfe !important;
    border-radius: 100px;
    padding: 0.35rem 0.9rem !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    color: #1d4ed8 !important;
    margin: 0.15rem;
}

.algo-tag {
    display: inline-block;
    padding: 0.25rem 0.65rem;
    border-radius: 6px;
    font-size: 0.76rem;
    font-weight: 700;
    margin: 0.1rem;
}
.algo-tag-complete { background-color: #ecfdf5 !important; color: #065f46 !important; border: 1px solid #a7f3d0 !important; }
.algo-tag-incomplete { background-color: #fffbeb !important; color: #92400e !important; border: 1px solid #fde68a !important; }
.algo-tag-optimal { background-color: #eef2ff !important; color: #3730a3 !important; border: 1px solid #c7d2fe !important; }

/* ─── Expanders ─────────────────────────────────────────────────────────── */
details[data-testid="stExpander"] {
    background-color: #ffffff !important;
    border: 1.5px solid var(--border) !important;
    border-radius: var(--radius) !important;
    box-shadow: var(--shadow-sm) !important;
}

details[data-testid="stExpander"] summary {
    color: var(--text-heading) !important;
    font-weight: 600 !important;
}

details[data-testid="stExpander"] summary:hover {
    color: var(--blue-primary) !important;
}

/* ─── Tables & DataFrames ───────────────────────────────────────────────── */
.stDataFrame,
[data-testid="stDataFrame"] {
    background-color: #ffffff !important;
    border: 1.5px solid var(--border) !important;
    border-radius: var(--radius) !important;
    box-shadow: var(--shadow-sm) !important;
}

/* ─── Tabs ──────────────────────────────────────────────────────────────── */
[data-testid="stTab"] {
    font-weight: 600 !important;
    color: var(--text-muted) !important;
    font-size: 0.95rem !important;
}

[data-testid="stTab"][aria-selected="true"] {
    color: var(--blue-primary) !important;
    border-bottom: 2px solid var(--blue-primary) !important;
}

/* ─── Water Jug Graphic ─────────────────────────────────────────────────── */
.jug-bar-outer {
    background-color: #f1f5f9 !important;
    border: 2px solid #94a3b8 !important;
    border-radius: 10px;
    overflow: hidden;
    height: 140px;
    width: 65px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
}

.jug-bar-fill {
    background: linear-gradient(180deg, #3b82f6, #1d4ed8) !important;
    border-radius: 0 0 8px 8px;
    transition: height 0.5s ease;
}

/* ─── Progress Bar ──────────────────────────────────────────────────────── */
.quiz-progress {
    background-color: #e2e8f0 !important;
    border-radius: 100px;
    height: 8px;
    overflow: hidden;
    margin: 0.6rem 0 1rem;
}

.quiz-progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #2563eb, #7c3aed) !important;
    border-radius: 100px;
    transition: width 0.3s ease;
}

/* ─── Dividers ──────────────────────────────────────────────────────────── */
hr {
    border-color: #e2e8f0 !important;
    margin: 1.5rem 0 !important;
}
</style>
"""
