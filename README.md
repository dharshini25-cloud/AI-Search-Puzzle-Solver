# 🧩 AI-Based Search & Puzzle Solver

An interactive, educational web application for exploring and comparing Artificial Intelligence search algorithms through hands-on puzzle solving, state-space exploration, graph pathfinding, quizzes, and guided tutoring.

---

## 🌟 Modules & Features

| Module | Description |
|---|---|
| 🧩 **8-Puzzle Solver** | Solve arbitrary 3×3 sliding puzzles with all 8 search algorithms. Features real-time tile validation, exact relative inversion parity solvability analysis, custom arbitrary initial and goal configurations, side-by-side board previews, step-by-step visual animation controls (Step 0 to N), and full solution step table. |
| 📷 **Puzzle Image OCR** | Upload PNG/JPG/JPEG images of puzzle boards. Uses computer vision (OpenCV) for board cropping and Tesseract OCR for tile recognition. Features a **Preview Detected Board** button, 3×3 manual correction grid with live duplicate/missing validation, and a **Confirm and Solve** button. |
| ⚗️ **Algorithm Lab** | Compare all 8 search algorithms on standardized built-in benchmark puzzle cases (Trivial, Easy, Medium, Hard). Eliminates manual tile entry for fair, consistent evaluations. Displays execution times, explored node counts, move lengths, interactive Plotly charts, and performance metric explanations. |
| 🤖 **AI Tutor** | Conversational tutor answering questions on AI concepts, intelligent agents, state-space formulations, all 8 algorithms, heuristics, Manhattan distance, Water Jug, and project architecture. Supports context-aware follow-up questions and renders clean, student-friendly formatting without raw Markdown `#` symbols. |
| 📝 **AI Quiz** | Comprehensive question bank of **262 verified multiple-choice questions** across all 8 search algorithms (exactly 10 Beginner, 10 Intermediate, and 10 Advanced questions each = 240 search questions) plus General AI topics. Features category/difficulty filters, question count selection, instant feedback, scoring, and an interactive **Review Incorrect Answers** review expander. |
| 🕸️ **Graph Search Solver** | Full support for **all 8 search algorithms** (BFS, DFS, A*, Greedy Best-First, Bidirectional Search, Uniform Cost Search, Depth-Limited Search, IDDFS). Includes graph presets (Romania Arad-Bucharest, Weighted Network, Binary Tree, Disconnected Graph), manual edge/weight editing, heuristic inputs, Plotly graph visualization, and an interactive step-by-step traversal playback slider. |
| 🪣 **Water Jug Solver** | Solves the classic two-jug Diophantine problem using BFS state-space search with dynamic visual jug fill levels and transition tables. |
| 📊 **History & Reports** | SQLite-backed solution tracking and quiz score logs with search, filtering, and CSV download capabilities. |
| ℹ️ **About** | Academic writeup covering problem formulation, search strategies, mathematical theorems (parity check), and algorithmic complexity. |

---

## ⚙️ Algorithms Implemented

| Algorithm | Type | Complete? | Optimal? | Time Complexity | Space Complexity |
|---|---|:---:|:---:|:---:|:---:|
| **Breadth-First Search (BFS)** | Uninformed | Yes | Yes (unit cost) | $O(b^d)$ | $O(b^d)$ |
| **Depth-First Search (DFS)** | Uninformed | No (in finite: with cycle check) | No | $O(b^m)$ | $O(b \cdot m)$ |
| **A\* Search** | Informed | Yes | Yes (admissible $h$) | $O(b^d)$ | $O(b^d)$ |
| **Greedy Best-First Search** | Informed | No | No | $O(b^m)$ | $O(b^m)$ |
| **Bidirectional Search** | Uninformed | Yes | Yes (unit cost) | $O(b^{d/2})$ | $O(b^{d/2})$ |
| **Uniform Cost Search (UCS)** | Uninformed | Yes | Yes | $O(b^{1 + \lfloor C^*/\epsilon \rfloor})$ | $O(b^{1 + \lfloor C^*/\epsilon \rfloor})$ |
| **Depth-Limited Search (DLS)** | Uninformed | No (if $d > L$) | No | $O(b^L)$ | $O(b \cdot L)$ |
| **Iterative Deepening DFS (IDDFS)** | Uninformed | Yes | Yes (unit cost) | $O(b^d)$ | $O(b \cdot d)$ |

---

## 🚀 Setup & Run Instructions

### Prerequisites
- **Python 3.10+** (tested on Python 3.11, 3.13, 3.14)
- **Tesseract OCR** (optional, recommended for puzzle image recognition)
  - Windows default path: `C:\Program Files\Tesseract-OCR\tesseract.exe`

### Installation
```powershell
# 1. Clone or navigate to the project directory
cd "C:\Users\dharshini\OneDrive\Desktop\AI_Search_Puzzle_Solver"

# 2. Install required Python packages
pip install -r requirements.txt
```

### Running the Application
```powershell
streamlit run app.py
```
The application will launch and open in your default browser at `http://localhost:8501`.

### Running the Test Suite
```powershell
py tests/test_comprehensive.py
```

---

## 📂 Project Structure

```
AI_Search_Puzzle_Solver/
├── app.py                     # Streamlit multi-page application
├── requirements.txt           # Python dependencies
├── history.db                 # SQLite database for run history and quiz results
├── README.md                  # Project documentation
│
├── algorithms/
│   ├── __init__.py
│   ├── bfs.py                 # Breadth-First Search (8-puzzle)
│   ├── dfs.py                 # Depth-First Search (8-puzzle)
│   ├── astar.py               # A* Search with Manhattan Distance (8-puzzle)
│   ├── greedy.py              # Greedy Best-First Search (8-puzzle)
│   ├── bidirectional.py       # Bidirectional BFS (8-puzzle)
│   ├── uniform_cost.py        # Uniform Cost Search (8-puzzle)
│   ├── depth_limited.py       # Depth-Limited Search (8-puzzle)
│   ├── iddfs.py               # Iterative Deepening DFS (8-puzzle)
│   ├── graph_search.py        # All 8 search algorithms on arbitrary graphs
│   └── water_jug.py           # Water Jug state-space BFS solver
│
├── utils/
│   ├── __init__.py
│   ├── puzzle.py              # Relative inversion parity & arbitrary solvability
│   ├── puzzle_image.py        # OpenCV board cropping & Tesseract OCR pipeline
│   ├── tutor_kb.py            # AI Tutor knowledge base & follow-up resolver
│   ├── quiz_data.py           # 262-question quiz bank (8 algos x 3 diffs + AI)
│   ├── styles.py              # Custom CSS styling tokens
│   └── db.py                  # SQLite database helpers
│
└── tests/
    ├── test_comprehensive.py  # Full unit test suite (16 test cases)
    ├── test_astar.py          # Standalone A* runner
    ├── test_bfs.py            # Standalone BFS runner
    ├── test_bidirectional.py  # Standalone Bidirectional runner
    ├── test_depth_limited.py  # Standalone DLS runner
    ├── test_dfs.py            # Standalone DFS runner
    ├── test_greedy.py         # Standalone Greedy runner
    ├── test_iddfs.py          # Standalone IDDFS runner
    └── test_uniform_cost.py   # Standalone UCS runner
```

---

## 🔍 Detailed Module Documentation

### 1. 8-Puzzle Solver
- **Arbitrary Initial and Goal States:** Enter any permutation of numbers $0$ through $8$.
- **Mathematical Solvability:** Solvability between any two arbitrary configurations is checked via relative inversion parity $\sum_{i < j} [pos(tile_i) > pos(tile_j)] \pmod 2$. If the parity count is odd, the application explains why the configuration cannot reach the goal and prevents running futile searches.
- **Step-by-Step Visualization:** After solving, users can inspect each step numbered starting from Step 0 up to Step $N$, with controls for First Step, Previous Step, Next Step, Last Step, Auto-Play animation, and an expandable full board sequence table.
- **Moved Tile Highlighting:** The tile that moved in each transition is visually highlighted in purple.

### 2. Image Upload & OCR
- **Pre-processing:** Uses OpenCV adaptive thresholding and contour detection to crop the 3×3 puzzle grid, segment individual cells, and filter noise.
- **OCR Engine:** Uses Tesseract OCR configured with digit-specific page segmentation modes.
- **Preview & Verification:** Provides a **Preview Detected Board** button followed by an interactive 3×3 editable input grid with real-time validation to verify and correct tiles before solving.

### 3. Algorithm Lab
- **Fixed Benchmarks:** Evaluates algorithms against standard built-in test puzzles (Trivial, Easy, Medium, Hard) to ensure fair, reproducible benchmarking without manual data entry.
- **Comparison Metrics:** Measures execution time (seconds/milliseconds), total nodes explored, and path move cost.
- **Charts:** Visualizes relative performance using Plotly bar charts.

### 4. AI Tutor
- **Topic Coverage:** Answers questions on AI definitions, intelligent agents, state-space graphs, BFS, DFS, A*, Greedy Best-First, Bidirectional Search, Uniform Cost Search, Depth-Limited Search, IDDFS, heuristics (Manhattan vs Misplaced Tiles), Water Jug, and project architecture.
- **Context-Aware Follow-Ups:** Tracks recent conversation history to resolve follow-up inquiries such as *"Is it complete and optimal?"* or *"What is its time complexity?"*.
- **Clean Formatting:** Strips raw Markdown `#` heading symbols and renders clean bold headers and monospace code blocks.

### 5. AI Quiz
- **Question Bank:** Contains 262 verified questions. Each of the 8 algorithms contains exactly 10 Beginner, 10 Intermediate, and 10 Advanced questions (240 algorithm questions total), plus 22 General AI questions.
- **Interactivity:** Allows filtering by category and difficulty, selecting question counts, scoring progress, immediate answer explanations, and reviewing incorrect answers at the end of the quiz.

### 6. Graph Search Solver
- **All 8 Search Algorithms:** Full implementation and selection for BFS, DFS, A*, Greedy Best-First, Bidirectional, UCS, DLS, and IDDFS.
- **Presets & Custom Graphs:** Includes ready-to-test graphs (Weighted Network, Romania Arad-to-Bucharest route, Binary Tree, Disconnected Graph) or accepts arbitrary user-defined edges.
- **Step-by-Step Traversal:** Interactive slider enables step-by-step playback of node expansions, highlighting visited nodes, current node, and final path.

---

## ⚠️ Known Limitations

1. **DFS / DLS Search Depth:** Uninformed DFS and Depth-Limited Search impose recursion/depth limits to prevent stack overflow and infinite loops on cyclic graphs.
2. **Heuristic Requirement:** In the Graph Search Solver, A* and Greedy Best-First Search require heuristic values $h(n)$ for informed decisions; if left empty, $h(n)=0$ is used by default.
3. **Image OCR:** Poor lighting, extreme perspective tilt, or handwritten non-standard digits may require manual confirmation in the 3×3 correction grid before solving.
4. **AI Tutor Knowledge Base:** The AI Tutor operates using an extensive local rule-based semantic knowledge base rather than an external paid cloud LLM, ensuring 100% offline functionality.
