"""
Local knowledge base for the AI Tutor.
Maps question patterns to curated, formatted answers.

Answers are returned as plain text / lightweight markdown suitable for
st.markdown() rendering — no raw # heading symbols will appear to the user.
"""

import re

# ---------------------------------------------------------------------------
# Knowledge base — ordered list of {patterns, answer} entries
# ---------------------------------------------------------------------------

KNOWLEDGE_BASE = [
    # ── Intelligent Agent ───────────────────────────────────────────────────
    {
        "patterns": ["intelligent agent", "what is an agent", "peas description",
                     "sensors actuators", "rational agent"],
        "answer": (
            "**Intelligent Agent**\n\n"
            "An intelligent agent is any entity that:\n"
            "1. **Perceives** its environment through sensors.\n"
            "2. **Acts** upon that environment through actuators.\n"
            "3. Does so **rationally** — choosing actions that maximise expected performance.\n\n"
            "**PEAS Description for the 8-Puzzle:**\n\n"
            "| Component | 8-Puzzle Example |\n"
            "|-----------|------------------|\n"
            "| **P**erformance | Minimum number of moves |\n"
            "| **E**nvironment | The 3×3 tile grid |\n"
            "| **A**ctuators | Slide a tile up / down / left / right |\n"
            "| **S**ensors | Current grid state |\n\n"
            "A **rational** agent selects the action expected to produce the best outcome "
            "given its current knowledge. It does not need to be all-knowing — just rational."
        ),
    },

    # ── 8-Puzzle Problem ────────────────────────────────────────────────────
    {
        "patterns": ["8-puzzle", "eight puzzle", "sliding puzzle",
                     "what is the puzzle", "8 puzzle"],
        "answer": (
            "**The 8-Puzzle Problem**\n\n"
            "The 8-puzzle is a classic AI search problem. It consists of a 3×3 grid "
            "containing tiles numbered 1–8 and one blank space (represented as 0).\n\n"
            "**Goal:** Rearrange the tiles from a scrambled starting configuration to a "
            "target goal state by sliding tiles into the blank space — only horizontally "
            "or vertically adjacent tiles may move.\n\n"
            "```\n"
            "Start state:      Goal state:\n"
            "  1  2  3           1  2  3\n"
            "  4  5  6    →      4  5  6\n"
            "  7  _  8           7  8  _\n"
            "```\n\n"
            "**Why it matters in AI:**\n"
            "- It models real state-space search problems cleanly.\n"
            "- The state space has 9!/2 = 181,440 reachable states.\n"
            "- It clearly demonstrates the trade-offs between search algorithms.\n"
            "- Not all configurations can reach all goals — solvability depends on "
            "inversion parity."
        ),
    },

    # ── State Space ─────────────────────────────────────────────────────────
    {
        "patterns": ["state space", "what is a state", "state representation",
                     "initial state", "goal state", "state-space"],
        "answer": (
            "**State Space**\n\n"
            "A state space is the complete set of all possible configurations a problem "
            "can be in.\n\n"
            "**For the 8-puzzle:**\n"
            "- A **state** is one arrangement of the 9 tiles, e.g. [1, 2, 3, 4, 5, 6, 7, 0, 8].\n"
            "- The **initial state** is the scrambled starting arrangement.\n"
            "- The **goal state** is the target arrangement.\n"
            "- An **action** transitions one state to another by sliding a tile.\n"
            "- A **solution** is a sequence of actions leading from initial to goal.\n\n"
            "**Total states:** 9! = 362,880, but only half (181,440) are reachable "
            "from any given start state.\n\n"
            "Search algorithms systematically explore this state space to find a path "
            "from start to goal. The quality of the search strategy determines how "
            "efficiently this exploration is done."
        ),
    },

    # ── BFS ────────────────────────────────────────────────────────────────
    {
        "patterns": ["breadth-first search", "bfs", "what is bfs",
                     "breadth first", "level by level"],
        "answer": (
            "**Breadth-First Search (BFS)**\n\n"
            "BFS explores the search tree level by level — all nodes at depth d before "
            "any node at depth d+1. It uses a **queue (FIFO)** as its data structure.\n\n"
            "**Algorithm steps:**\n"
            "1. Add the start node to the queue.\n"
            "2. Dequeue a node; if it is the goal → done.\n"
            "3. Add all unvisited neighbours to the queue.\n"
            "4. Repeat until the goal is found or the queue is empty.\n\n"
            "**Properties:**\n\n"
            "| Property | Value |\n"
            "|----------|-------|\n"
            "| Complete | Yes (if branching factor is finite) |\n"
            "| Optimal | Yes (for uniform step costs) |\n"
            "| Time complexity | O(b^d) |\n"
            "| Space complexity | O(b^d) |\n\n"
            "where b = branching factor and d = solution depth.\n\n"
            "**In this project:** BFS guarantees the shortest path (fewest moves) for "
            "the 8-puzzle, but can consume a lot of memory for deep solutions because "
            "it stores all frontier nodes simultaneously."
        ),
    },

    # ── DFS ────────────────────────────────────────────────────────────────
    {
        "patterns": ["depth-first search", "dfs", "what is dfs",
                     "depth first search"],
        "answer": (
            "**Depth-First Search (DFS)**\n\n"
            "DFS explores as deep as possible along each branch before backtracking. "
            "It uses a **stack (LIFO)** as its data structure.\n\n"
            "**Algorithm steps:**\n"
            "1. Push the start node onto the stack.\n"
            "2. Pop a node; if it is the goal → done.\n"
            "3. Push unvisited neighbours onto the stack.\n"
            "4. Repeat.\n\n"
            "**Properties:**\n\n"
            "| Property | Value |\n"
            "|----------|-------|\n"
            "| Complete | No — can loop without a depth limit |\n"
            "| Optimal | No |\n"
            "| Time complexity | O(b^m) |\n"
            "| Space complexity | O(b·m) |\n\n"
            "where m = maximum depth.\n\n"
            "**In this project:** DFS uses a depth limit (default 30) and visited-state "
            "tracking to prevent infinite loops. It uses far less memory than BFS but "
            "may find longer solutions or miss the goal if it is deeper than the limit."
        ),
    },

    # ── A* Search ──────────────────────────────────────────────────────────
    {
        "patterns": ["a* search", "a star", "astar", "what is a*",
                     "a-star", "a star search"],
        "answer": (
            "**A\\* Search**\n\n"
            "A\\* is the most popular informed search algorithm. It uses the evaluation "
            "function:\n\n"
            "**f(n) = g(n) + h(n)**\n\n"
            "- **g(n)** = actual cost from start to node n (moves made so far)\n"
            "- **h(n)** = heuristic estimate of cost from n to goal\n"
            "- **f(n)** = estimated total cost of the best solution through n\n\n"
            "**Properties:**\n\n"
            "| Property | Value |\n"
            "|----------|-------|\n"
            "| Complete | Yes |\n"
            "| Optimal | Yes (if h is admissible) |\n"
            "| Time complexity | O(b^d) in worst case |\n"
            "| Space complexity | O(b^d) |\n\n"
            "**Admissibility:** A heuristic h(n) is admissible if it never overestimates "
            "the true cost to the goal. This guarantees A\\* finds the optimal solution.\n\n"
            "**In this project:** A\\* uses **Manhattan Distance** as the heuristic "
            "(admissible for the 8-puzzle). It typically explores 10–1000× fewer nodes "
            "than BFS while still guaranteeing the optimal solution."
        ),
    },

    # ── Greedy Best-First ──────────────────────────────────────────────────
    {
        "patterns": ["greedy", "greedy best first", "greedy search",
                     "greedy best-first", "greedy best first search"],
        "answer": (
            "**Greedy Best-First Search**\n\n"
            "Greedy Best-First expands the node that appears closest to the goal "
            "using only the heuristic estimate:\n\n"
            "**f(n) = h(n)** (ignores the actual path cost g(n))\n\n"
            "**Properties:**\n\n"
            "| Property | Value |\n"
            "|----------|-------|\n"
            "| Complete | Yes (with cycle detection) |\n"
            "| Optimal | No |\n"
            "| Time complexity | O(b^m) |\n"
            "| Space complexity | O(b^m) |\n\n"
            "**Compared to A\\*:**\n"
            "- Greedy is often faster in practice (fewer nodes on average).\n"
            "- But it can find suboptimal solutions.\n"
            "- A\\* balances past cost g(n) and heuristic h(n) for guaranteed optimality.\n\n"
            "**In this project:** Greedy often reaches the goal quickly but may "
            "require more total moves than the optimal path found by A\\* or BFS."
        ),
    },

    # ── Bidirectional Search ───────────────────────────────────────────────
    {
        "patterns": ["bidirectional search", "bidirectional bfs",
                     "how does bidirectional work", "bidirectional",
                     "two-way search"],
        "answer": (
            "**Bidirectional Search**\n\n"
            "Bidirectional Search runs two simultaneous searches:\n"
            "1. **Forward** — from the start state toward the goal.\n"
            "2. **Backward** — from the goal state toward the start.\n\n"
            "The search terminates when the two frontiers **meet in the middle**.\n\n"
            "**Why it is faster:**\n"
            "- BFS explores O(b^d) nodes.\n"
            "- Bidirectional BFS explores approximately O(2 × b^(d/2)) nodes.\n"
            "- Example: for d=10, b=3 → BFS ≈ 59,049 nodes vs Bidirectional ≈ 486 nodes!\n\n"
            "**Properties:**\n\n"
            "| Property | Value |\n"
            "|----------|-------|\n"
            "| Complete | Yes |\n"
            "| Optimal | Yes |\n"
            "| Time complexity | O(b^(d/2)) |\n"
            "| Space complexity | O(b^(d/2)) |\n\n"
            "**Limitation:** Requires that the reverse of each operation is known. "
            "For the 8-puzzle, every slide is reversible, so bidirectional search "
            "works very well."
        ),
    },

    # ── Uniform Cost Search ────────────────────────────────────────────────
    {
        "patterns": ["uniform cost search", "ucs", "dijkstra",
                     "uniform cost", "lowest cost"],
        "answer": (
            "**Uniform Cost Search (UCS)**\n\n"
            "UCS always expands the node with the **lowest total path cost g(n)** first, "
            "using a priority queue (min-heap).\n\n"
            "**Properties:**\n\n"
            "| Property | Value |\n"
            "|----------|-------|\n"
            "| Complete | Yes |\n"
            "| Optimal | Yes |\n"
            "| Time complexity | O(b^(1 + C*/ε)) |\n"
            "| Space complexity | O(b^(1 + C*/ε)) |\n\n"
            "where C* = optimal solution cost, ε = minimum edge cost.\n\n"
            "**Relationship to BFS:** When all step costs are equal (as in the 8-puzzle), "
            "UCS behaves identically to BFS.\n\n"
            "**Relationship to A\\*:** UCS is A\\* with h(n) = 0. It finds optimal paths "
            "but explores more nodes than A\\* because it has no heuristic guidance to "
            "focus the search toward the goal."
        ),
    },

    # ── Depth-Limited Search ───────────────────────────────────────────────
    {
        "patterns": ["depth limited", "depth-limited", "depth limit search",
                     "dls", "depth limited search"],
        "answer": (
            "**Depth-Limited Search (DLS)**\n\n"
            "DLS is DFS with a preset maximum depth limit L. Nodes deeper than L are "
            "not expanded.\n\n"
            "**Properties:**\n\n"
            "| Property | Value |\n"
            "|----------|-------|\n"
            "| Complete | Only if the solution depth ≤ L |\n"
            "| Optimal | No |\n"
            "| Time complexity | O(b^L) |\n"
            "| Space complexity | O(b·L) |\n\n"
            "**Trade-off:** A smaller L means less memory but risks missing deep solutions. "
            "A larger L explores more nodes.\n\n"
            "**In this project:** The default limit is 30. If no solution is found "
            "within the limit, the algorithm reports failure — it does not guarantee a "
            "solution exists, only that none exists within L steps."
        ),
    },

    # ── IDDFS ──────────────────────────────────────────────────────────────
    {
        "patterns": ["iterative deepening", "iddfs", "iterative deepening dfs",
                     "iterative deepening search", "ids"],
        "answer": (
            "**Iterative Deepening DFS (IDDFS)**\n\n"
            "IDDFS combines the space efficiency of DFS with the completeness and "
            "optimality of BFS.\n\n"
            "**How it works:**\n"
            "1. Run DFS with depth limit = 0. If goal not found...\n"
            "2. Run DFS with depth limit = 1. If goal not found...\n"
            "3. Continue increasing the limit until the goal is found.\n\n"
            "**Properties:**\n\n"
            "| Property | Value |\n"
            "|----------|-------|\n"
            "| Complete | Yes |\n"
            "| Optimal | Yes (uniform step costs) |\n"
            "| Time complexity | O(b^d) |\n"
            "| Space complexity | O(b·d) — like DFS! |\n\n"
            "**Key insight:** Although nodes at shallow depths are re-expanded at each "
            "iteration, this overhead is small because most nodes are at the deepest "
            "level (about 73% in a tree with branching factor 3).\n\n"
            "**In practice:** IDDFS is the preferred uninformed strategy when the "
            "solution depth is unknown and memory is limited."
        ),
    },

    # ── Manhattan Distance / Heuristics ───────────────────────────────────
    {
        "patterns": ["manhattan distance", "heuristic", "h(n)",
                     "what is manhattan", "admissible heuristic",
                     "admissible", "heuristic function"],
        "answer": (
            "**Heuristics and Manhattan Distance**\n\n"
            "A **heuristic** h(n) is an estimate of the remaining cost to reach the "
            "goal from state n. A good heuristic guides the search efficiently.\n\n"
            "**Admissibility:** h(n) is admissible if it **never overestimates** the "
            "true cost. Admissibility guarantees A\\* finds the optimal solution.\n\n"
            "**Manhattan Distance** (used in this project):\n\n"
            "```\n"
            "h(n) = sum of |row_current - row_goal| + |col_current - col_goal|\n"
            "       for each non-blank tile\n"
            "```\n\n"
            "**Example:**\n"
            "```\n"
            "Current:   Goal:\n"
            "1 2 3      1 2 3\n"
            "4 5 6      4 5 6\n"
            "7 _ 8      7 8 _\n"
            "```\n"
            "Tile 8 is at position (row=2, col=2) and needs to reach (row=2, col=1):\n"
            "|2-2| + |2-1| = 1 move.\n\n"
            "**Why Manhattan Distance is admissible:** Tiles can only move one step at "
            "a time in straight lines, so they can never need fewer moves than their "
            "Manhattan distance.\n\n"
            "Manhattan Distance is stronger than simply counting misplaced tiles — "
            "it is always ≥ the misplaced-tiles count."
        ),
    },

    # ── BFS vs DFS ─────────────────────────────────────────────────────────
    {
        "patterns": ["difference between bfs and dfs", "bfs vs dfs",
                     "compare bfs dfs", "bfs and dfs difference"],
        "answer": (
            "**BFS vs DFS — Comparison**\n\n"
            "| Feature | BFS | DFS |\n"
            "|---------|-----|-----|\n"
            "| Data structure | Queue (FIFO) | Stack (LIFO) |\n"
            "| Exploration order | Level by level | Branch by branch |\n"
            "| Finds shortest path | Yes | No |\n"
            "| Memory usage | High (all frontier nodes) | Low (current path only) |\n"
            "| Complete | Yes | Only with depth limit |\n"
            "| Optimal | Yes (uniform cost) | No |\n\n"
            "**In the 8-puzzle:**\n"
            "- BFS always finds the minimum number of moves but can use significant memory.\n"
            "- DFS finds *a* solution quickly using little memory, but the path may be "
            "much longer than optimal."
        ),
    },

    # ── Informed vs Uninformed ────────────────────────────────────────────
    {
        "patterns": ["informed search", "uninformed search",
                     "difference informed uninformed", "blind search",
                     "informed vs uninformed"],
        "answer": (
            "**Informed vs Uninformed Search**\n\n"
            "**Uninformed (Blind) Search**\n"
            "Has no information about how close a state is to the goal. "
            "Explores states systematically without guidance.\n"
            "Examples: BFS, DFS, UCS, IDDFS, DLS\n\n"
            "**Informed (Heuristic) Search**\n"
            "Uses a heuristic function h(n) to estimate the distance to the goal. "
            "Focuses exploration toward promising states.\n"
            "Examples: A\\*, Greedy Best-First Search\n\n"
            "| Aspect | Uninformed | Informed |\n"
            "|--------|-----------|---------|\n"
            "| Uses heuristic | No | Yes |\n"
            "| Efficiency | Lower | Higher |\n"
            "| Explores fewer nodes | No | Usually yes |\n"
            "| Requires domain knowledge | No | Yes |\n\n"
            "A good heuristic can reduce nodes explored by orders of magnitude. "
            "For the 8-puzzle, Manhattan Distance reduces A\\* node expansions to "
            "a tiny fraction of what BFS requires."
        ),
    },

    # ── Why A* is useful ───────────────────────────────────────────────────
    {
        "patterns": ["why a* useful", "a* 8-puzzle", "why use a star",
                     "why is a* good", "a* advantage"],
        "answer": (
            "**Why A\\* is Useful for the 8-Puzzle**\n\n"
            "A\\* combines the completeness and optimality of BFS with the efficiency "
            "of heuristic guidance.\n\n"
            "**Key advantages:**\n"
            "1. **Optimality** — guaranteed to find the shortest solution when using "
            "an admissible heuristic (Manhattan Distance).\n"
            "2. **Efficiency** — explores far fewer nodes than BFS. On hard 20-move "
            "puzzles, BFS might expand ~100,000 nodes while A\\* expands only ~1,000.\n"
            "3. **Admissible heuristic** — Manhattan Distance never overestimates, "
            "so A\\* never misses the optimal path.\n\n"
            "**f(n) = g(n) + h(n)**\n"
            "- g(n) = moves made so far\n"
            "- h(n) = Manhattan Distance to goal\n"
            "- f(n) = estimated total solution length\n\n"
            "A\\* is the recommended algorithm for most 8-puzzle configurations."
        ),
    },

    # ── Completeness and Optimality ────────────────────────────────────────
    {
        "patterns": ["completeness", "optimality", "complete optimal",
                     "what is completeness", "what is optimality"],
        "answer": (
            "**Completeness and Optimality**\n\n"
            "**Completeness** — An algorithm is complete if it is guaranteed to find "
            "a solution whenever one exists.\n\n"
            "**Optimality** — An algorithm is optimal if it always finds the best "
            "(e.g., shortest) solution.\n\n"
            "| Algorithm | Complete | Optimal |\n"
            "|-----------|----------|---------|\n"
            "| BFS | Yes | Yes (uniform cost) |\n"
            "| DFS | Only with depth limit | No |\n"
            "| A\\* | Yes | Yes (admissible h) |\n"
            "| Greedy | Yes (with cycle detection) | No |\n"
            "| UCS | Yes | Yes |\n"
            "| DLS | Only within limit | No |\n"
            "| IDDFS | Yes | Yes (uniform cost) |\n"
            "| Bidirectional | Yes | Yes |\n\n"
            "**Why it matters:** For a puzzle solver, optimality means you get the "
            "shortest possible solution — the fewest number of tile moves. "
            "Completeness ensures the solver does not get stuck or miss solvable puzzles."
        ),
    },

    # ── Water Jug ─────────────────────────────────────────────────────────
    {
        "patterns": ["water jug", "jug problem", "water problem",
                     "jug puzzle"],
        "answer": (
            "**Water Jug Problem**\n\n"
            "**Given:** Two jugs with capacities A and B litres. No measuring marks.\n"
            "**Goal:** Measure exactly T litres using these jugs.\n\n"
            "**State:** (amount_in_A, amount_in_B)\n\n"
            "**Operations:**\n"
            "1. Fill Jug A completely.\n"
            "2. Fill Jug B completely.\n"
            "3. Empty Jug A.\n"
            "4. Empty Jug B.\n"
            "5. Pour A into B (until A is empty or B is full).\n"
            "6. Pour B into A (until B is empty or A is full).\n\n"
            "**Solvability:** A target T is achievable if and only if T is a multiple "
            "of GCD(A, B) and T ≤ max(A, B).\n\n"
            "**Example:** A=4L, B=3L, Target=2L\n"
            "```\n"
            "Step 1: (4, 0) — Fill A\n"
            "Step 2: (1, 3) — Pour A into B\n"
            "Step 3: (1, 0) — Empty B\n"
            "Step 4: (0, 1) — Pour A into B\n"
            "Step 5: (4, 1) — Fill A\n"
            "Step 6: (2, 3) — Pour A into B → 2L in A! Goal reached.\n"
            "```"
        ),
    },

    # ── Graph Search ──────────────────────────────────────────────────────
    {
        "patterns": ["graph search", "graph traversal",
                     "how does graph search work", "graph algorithm"],
        "answer": (
            "**Graph Search**\n\n"
            "Graph search is the process of exploring a graph (nodes connected by edges) "
            "to find a path between a start node and a goal node.\n\n"
            "**Key difference from tree search:**\n"
            "- Tree search may revisit the same state multiple times.\n"
            "- Graph search maintains a **visited/closed set** to avoid revisiting states.\n\n"
            "**Algorithms in this project's Graph Search module:**\n\n"
            "| Algorithm | Strategy | Optimal |\n"
            "|-----------|----------|---------|\n"
            "| BFS | Level by level | Yes (uniform cost) |\n"
            "| DFS | Branch by branch | No |\n"
            "| A\\* | Lowest f(n) = g+h first | Yes (admissible h) |\n"
            "| Greedy | Lowest h(n) first | No |\n"
            "| Bidirectional BFS | From both ends | Yes |\n"
            "| UCS | Lowest g(n) first | Yes |\n"
            "| DLS | DFS with depth limit | No |\n"
            "| IDDFS | Repeated DLS | Yes |\n\n"
            "In this project you can define a custom graph with nodes and edges, "
            "then run any of these eight algorithms to find a path."
        ),
    },

    # ── Solvability ────────────────────────────────────────────────────────
    {
        "patterns": ["solvable", "unsolvable", "how determine solvable",
                     "inversion parity", "inversions", "puzzle solvable"],
        "answer": (
            "**Puzzle Solvability — Inversion Parity**\n\n"
            "Not every 8-puzzle configuration can reach every goal state. "
            "Solvability is determined by **inversion parity**.\n\n"
            "**What is an inversion?**\n"
            "An inversion is a pair of tiles (a, b) where a appears before b in the "
            "current arrangement but after b in the goal arrangement.\n\n"
            "**Rule:** A puzzle is solvable if and only if the number of inversions "
            "relative to the goal is **even**.\n\n"
            "**How this project checks it:**\n"
            "1. Map each tile to its position in the goal state.\n"
            "2. Translate the start state into a sequence of goal-position indices "
            "(excluding the blank tile).\n"
            "3. Count inversions in that sequence.\n"
            "4. Even count → solvable; odd count → unsolvable.\n\n"
            "This relative-parity check works correctly for **any valid goal state**, "
            "not just the standard [1,2,3,4,5,6,7,8,0] goal."
        ),
    },

    # ── Which algorithm to use ─────────────────────────────────────────────
    {
        "patterns": ["which algorithm", "best algorithm",
                     "which should i use", "recommend algorithm",
                     "when to use"],
        "answer": (
            "**Which Algorithm Should You Use?**\n\n"
            "The best algorithm depends on your priorities:\n\n"
            "| Goal | Best Choice |\n"
            "|------|-------------|\n"
            "| Guaranteed shortest path + efficiency | A\\* |\n"
            "| Shortest path, no heuristic | BFS or UCS |\n"
            "| Low memory, any solution | DFS or IDDFS |\n"
            "| Fastest for deep solutions | Bidirectional BFS |\n"
            "| Memory-efficient AND optimal | IDDFS |\n"
            "| Quick approximate solution | Greedy Best-First |\n\n"
            "**General recommendations for the 8-puzzle:**\n"
            "- For puzzles with ≤ 15 moves: Any algorithm works.\n"
            "- For hard puzzles (20+ moves): A\\* is strongly recommended.\n"
            "- For educational comparison: Use the Algorithm Lab to compare them all!\n\n"
            "No single algorithm is universally best — the right choice depends on "
            "the specific problem constraints such as available memory, whether "
            "optimality is required, and whether a good heuristic is available."
        ),
    },

    # ── Problem Formulation ────────────────────────────────────────────────
    {
        "patterns": ["problem formulation", "search problem",
                     "formulate problem", "components of search"],
        "answer": (
            "**Problem Formulation in AI Search**\n\n"
            "A search problem is formally defined by five components:\n\n"
            "1. **Initial State** — the starting configuration.\n"
            "2. **Actions** — the set of operations applicable in each state.\n"
            "3. **Transition Model** — what each action does to the current state.\n"
            "4. **Goal Test** — a function that checks if a state is the goal.\n"
            "5. **Path Cost** — the cumulative cost of a sequence of actions.\n\n"
            "**For the 8-puzzle:**\n"
            "- Initial state: scrambled tile arrangement\n"
            "- Actions: slide left / right / up / down\n"
            "- Transition model: produce a new state after a valid slide\n"
            "- Goal test: does the arrangement match the goal state?\n"
            "- Path cost: number of moves (each move costs 1)\n\n"
            "A well-defined problem formulation is the first step to applying any "
            "AI search algorithm."
        ),
    },

    # ── Time & Space Complexity ────────────────────────────────────────────
    {
        "patterns": ["time complexity", "space complexity",
                     "complexity", "big o", "memory usage"],
        "answer": (
            "**Time and Space Complexity of Search Algorithms**\n\n"
            "| Algorithm | Time | Space |\n"
            "|-----------|------|-------|\n"
            "| BFS | O(b^d) | O(b^d) |\n"
            "| DFS | O(b^m) | O(b·m) |\n"
            "| UCS | O(b^(C*/ε)) | O(b^(C*/ε)) |\n"
            "| DLS | O(b^L) | O(b·L) |\n"
            "| IDDFS | O(b^d) | O(b·d) |\n"
            "| A\\* | O(b^d) worst | O(b^d) |\n"
            "| Greedy | O(b^m) | O(b^m) |\n"
            "| Bidirectional | O(b^(d/2)) | O(b^(d/2)) |\n\n"
            "- b = branching factor (≈3 for 8-puzzle)\n"
            "- d = depth of optimal solution\n"
            "- m = maximum depth\n"
            "- L = depth limit\n"
            "- C\\* = optimal path cost\n"
            "- ε = minimum step cost\n\n"
            "**Key insight:** IDDFS achieves BFS-level optimality with DFS-level memory, "
            "making it especially attractive when memory is the bottleneck."
        ),
    },

    # ── Path Cost ─────────────────────────────────────────────────────────
    {
        "patterns": ["path cost", "cost function", "step cost",
                     "g(n)", "cumulative cost"],
        "answer": (
            "**Path Cost in Search Algorithms**\n\n"
            "The **path cost** g(n) is the total cost of the path from the start state "
            "to node n. It accumulates the step costs of each action along the path.\n\n"
            "**In the 8-puzzle:** Every tile slide has a step cost of 1, so g(n) = "
            "number of moves made so far.\n\n"
            "**How different algorithms use path cost:**\n"
            "- **BFS** — implicitly minimises moves (uniform cost of 1 per step)\n"
            "- **UCS** — explicitly sorts by g(n); generalises BFS to non-uniform costs\n"
            "- **A\\*** — uses f(n) = g(n) + h(n); balances actual cost and estimated future cost\n"
            "- **Greedy** — ignores g(n); only uses h(n) — can find suboptimal paths\n"
            "- **DFS / DLS / IDDFS** — do not track path cost; not optimal\n\n"
            "Algorithms that track and minimise path cost are called **cost-sensitive** "
            "and can guarantee optimal solutions."
        ),
    },

    # ── Algorithm comparison ───────────────────────────────────────────────
    {
        "patterns": ["compare algorithms", "algorithm comparison",
                     "algorithms compared", "comparison table"],
        "answer": (
            "**Search Algorithm Comparison**\n\n"
            "| Algorithm | Type | Complete | Optimal | Time | Space |\n"
            "|-----------|------|----------|---------|------|-------|\n"
            "| BFS | Uninformed | Yes | Yes | O(b^d) | O(b^d) |\n"
            "| DFS | Uninformed | No* | No | O(b^m) | O(b·m) |\n"
            "| UCS | Uninformed | Yes | Yes | O(b^C*) | O(b^C*) |\n"
            "| DLS | Uninformed | No | No | O(b^L) | O(b·L) |\n"
            "| IDDFS | Uninformed | Yes | Yes | O(b^d) | O(b·d) |\n"
            "| A\\* | Informed | Yes | Yes | O(b^d) | O(b^d) |\n"
            "| Greedy | Informed | Yes* | No | O(b^m) | O(b^m) |\n"
            "| Bidirectional | Uninformed | Yes | Yes | O(b^d/2) | O(b^d/2) |\n\n"
            "* DFS complete only with depth limit and cycle detection.\n"
            "* Greedy complete only with cycle detection.\n\n"
            "Use the **Algorithm Lab** in this project to run a real comparison on "
            "benchmark puzzles and see measured execution times and node counts."
        ),
    },

    # ── Algorithms in this Project ─────────────────────────────────────────
    {
        "patterns": ["algorithms in this project", "implemented in this project",
                     "what algorithms are implemented", "algorithms available",
                     "website algorithms", "which algorithms are supported"],
        "answer": (
            "**Algorithms Implemented in this Project**\n\n"
            "This application implements eight distinct search algorithms for solving both the 8-puzzle and custom graphs:\n\n"
            "1. **Breadth-First Search (BFS)** — Explores level by level; guarantees shortest moves.\n"
            "2. **Depth-First Search (DFS)** — Explores branches deeply with linear memory; uses depth limits.\n"
            "3. **A\\* Search** — Optimal informed search combining path cost g(n) and Manhattan heuristic h(n).\n"
            "4. **Greedy Best-First Search** — Fast heuristic search using f(n) = h(n); may be suboptimal.\n"
            "5. **Bidirectional Search** — Searches simultaneously from start and goal; meets in the middle.\n"
            "6. **Uniform Cost Search (UCS)** — Expands lowest path cost g(n); equivalent to Dijkstra.\n"
            "7. **Depth-Limited Search (DLS)** — DFS capped at a configurable depth limit L to avoid infinite loops.\n"
            "8. **Iterative Deepening DFS (IDDFS)** — Combines DFS linear memory with BFS shortest-path optimality.\n\n"
            "All eight algorithms can be tested on the **8-Puzzle Solver**, compared side-by-side in the **Algorithm Lab**, and evaluated on custom graphs in the **Graph Search Solver**."
        ),
    },

    # ── Difference between BFS and UCS ─────────────────────────────────────
    {
        "patterns": ["difference between bfs and ucs", "bfs vs ucs",
                     "bfs and ucs difference", "compare bfs ucs",
                     "bfs vs uniform cost"],
        "answer": (
            "**BFS vs Uniform Cost Search (UCS)**\n\n"
            "| Feature | Breadth-First Search (BFS) | Uniform Cost Search (UCS) |\n"
            "|---------|----------------------------|---------------------------|\n"
            "| **Edge Costs** | Assumes all step costs are equal (cost = 1) | Handles arbitrary non-negative costs (costs >= 0) |\n"
            "| **Frontier** | FIFO Queue | Priority Queue (Min-Heap ordered by g(n)) |\n"
            "| **Goal Test** | At node generation time (early test) | When node is popped from the queue (late test) |\n"
            "| **Optimality** | Optimal for minimum edge count | Optimal for minimum total path cost |\n\n"
            "**Key Insight:** BFS is a special case of UCS when all step costs are equal. When weights vary, BFS finds fewest edges (which may be expensive), while UCS finds the cheapest path."
        ),
    },

    # ── Difference between A* and Greedy ───────────────────────────────────
    {
        "patterns": ["difference between a* and greedy", "a* vs greedy",
                     "a star vs greedy", "compare a* greedy"],
        "answer": (
            "**A\\* Search vs Greedy Best-First Search**\n\n"
            "| Feature | A\\* Search | Greedy Best-First Search |\n"
            "|---------|-------------|--------------------------|\n"
            "| **Evaluation** | f(n) = g(n) + h(n) | f(n) = h(n) |\n"
            "| **Past Cost** | Fully considered via g(n) | Completely ignored |\n"
            "| **Optimality** | Guaranteed optimal (with admissible h) | Suboptimal (can take long detours) |\n"
            "| **Speed** | Balances search; expands only necessary nodes | Often very fast, but prone to false leads |\n\n"
            "**Summary:** Greedy rushes blindly toward the goal using only the heuristic estimate; A\\* balances the distance already traveled with the estimated distance remaining to guarantee the optimal path."
        ),
    },

    # ── Solvability & Inversion Parity ─────────────────────────────────────
    {
        "patterns": ["solvability", "why is puzzle unsolvable", "inversion parity",
                     "how to know if solvable", "odd inversions", "parity check"],
        "answer": (
            "**8-Puzzle Solvability & Inversion Parity**\n\n"
            "A 3×3 sliding puzzle has 9! = 362,880 possible permutations, but only **half (181,440)** can reach any given goal state.\n\n"
            "**The Mathematical Reason:**\n"
            "- An **inversion** is a pair of non-blank tiles (A, B) where A precedes B in the list, but A > B.\n"
            "- Sliding a tile horizontally does not change the relative sequence of non-blank tiles (0 inversions changed).\n"
            "- Sliding a tile vertically moves it past exactly two non-blank tiles in the 1D representation, which changes the inversion count by +2, 0, or -2 (always an **even** change).\n\n"
            "**Solvability Rule:**\n"
            "An initial state can reach a target goal state if and only if the number of inversions relative to the target goal's ordering is **even**.\n"
            "If the relative inversion count is **odd**, it is mathematically impossible to reach that goal state using legal tile slides."
        ),
    },

    # ── Image Upload in 8-Puzzle ───────────────────────────────────────────
    {
        "patterns": ["image upload", "camera", "how to upload image",
                     "photo puzzle", "ocr detection", "detect tiles"],
        "answer": (
            "**How Image Upload & OCR Works**\n\n"
            "The 8-Puzzle Solver includes an image recognition pipeline:\n\n"
            "1. **Upload:** Accepts PNG, JPG, or JPEG images of a 3×3 puzzle board.\n"
            "2. **Board Localization:** Uses computer vision (OpenCV) to detect the 3×3 grid boundary and crop the board.\n"
            "3. **Cell Segmentation:** Divides the board into 9 equal cells (3 rows × 3 columns) and insets each cell to ignore border lines.\n"
            "4. **OCR & Detection:** Runs Tesseract OCR on high-contrast preprocessed cells to detect digits 1–8 and identify the blank tile (0).\n"
            "5. **Preview & Correction:** Displays the detected 3×3 board and provides manual correction boxes so you can verify each tile.\n"
            "6. **Confirm & Solve:** Validates that each digit 0–8 appears exactly once, checks mathematical solvability, and solves with your chosen algorithm."
        ),
    },

    # ── Pseudocode ─────────────────────────────────────────────────────────
    {
        "patterns": ["pseudocode", "algorithm steps", "how to code",
                     "implementation of a*", "pseudocode for bfs"],
        "answer": (
            "**General Search Algorithm Pseudocode**\n\n"
            "```python\n"
            "def search(start_state, goal_state):\n"
            "    frontier = PriorityQueue() # or Queue (BFS) / Stack (DFS)\n"
            "    frontier.push(start_state, priority=0)\n"
            "    explored = set()\n"
            "    came_from = {start_state: None}\n"
            "\n"
            "    while not frontier.is_empty():\n"
            "        current = frontier.pop()\n"
            "        if current == goal_state:\n"
            "            return reconstruct_path(came_from, current)\n"
            "\n"
            "        explored.add(current)\n"
            "        for neighbor in get_neighbors(current):\n"
            "            if neighbor not in explored and neighbor not in frontier:\n"
            "                came_from[neighbor] = current\n"
            "                cost = calculate_priority(neighbor)\n"
            "                frontier.push(neighbor, priority=cost)\n"
            "    return None # No solution found\n"
            "```"
        ),
    },
]

FALLBACK = (
    "I don't have a specific answer for that question in my knowledge base.\n\n"
    "**Topics I can help with:**\n"
    "- AI fundamentals: agents, PEAS, state spaces, problem formulation\n"
    "- Search algorithms: BFS, DFS, A\\*, Greedy, UCS, Bidirectional, IDDFS, DLS\n"
    "- Heuristic functions: Manhattan distance, admissibility, consistency\n"
    "- The 8-puzzle problem and solvability\n"
    "- The Water Jug problem\n"
    "- Graph search\n"
    "- Completeness, optimality, time and space complexity\n"
    "- Algorithm comparisons\n\n"
    "Try rephrasing your question or click one of the **suggested questions** above!"
)


def sanitize_answer(text: str) -> str:
    """
    Ensure no raw Markdown heading symbols (#, ##, ###) appear in displayed answers.
    Converts headings to bold text while preserving readability.
    """
    lines = []
    for line in text.splitlines():
        # Match lines starting with 1 to 6 '#'
        m = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
        if m:
            lines.append(f"**{m.group(2)}**")
        else:
            lines.append(line)
    return "\n".join(lines)


# Topic keywords used to resolve follow-up questions
TOPIC_KEYWORDS = {
    "a*": ["a*", "a star", "astar"],
    "bfs": ["bfs", "breadth-first", "breadth first"],
    "dfs": ["dfs", "depth-first", "depth first"],
    "greedy": ["greedy", "best-first"],
    "bidirectional": ["bidirectional"],
    "ucs": ["uniform cost", "ucs", "dijkstra"],
    "dls": ["depth-limited", "depth limit", "dls"],
    "iddfs": ["iterative deepening", "iddfs"],
    "water jug": ["water jug", "jugs", "water"],
    "8-puzzle": ["8-puzzle", "puzzle", "sliding tile", "tiles"],
    "manhattan": ["manhattan", "heuristic", "admissibility", "consistency"],
    "solvability": ["solvability", "inversion", "parity"],
    "agent": ["intelligent agent", "peas", "rational agent"],
}


def _extract_recent_topic(chat_history):
    """Scan recent chat history to identify the last discussed subject."""
    if not chat_history:
        return ""
    for msg in reversed(chat_history):
        content = msg.get("content", "").lower()
        for topic, aliases in TOPIC_KEYWORDS.items():
            if any(alias in content for alias in aliases):
                return topic
    return ""


def answer_question(question: str, chat_history=None) -> str:
    """
    Return the best matching answer for a user question.
    Supports follow-up queries using chat_history context and sanitizes output.
    """
    q = question.lower().strip()

    # Check for follow-up phrasing (e.g. 'what about its time complexity?', 'is it optimal?', 'why?')
    is_follow_up = any(q.startswith(phrase) or phrase in q for phrase in [
        "what about", "is it", "does it", "its time", "its space", "how does it",
        "why", "can you explain", "give an example", "what is its", "is that", "show pseudocode"
    ])

    if is_follow_up and chat_history:
        recent_topic = _extract_recent_topic(chat_history)
        if recent_topic:
            q = f"{recent_topic} {q}"

    best_match = None
    best_count = 0

    for entry in KNOWLEDGE_BASE:
        count = sum(1 for p in entry["patterns"] if p in q)
        if count > best_count:
            best_count = count
            best_match = entry

    if best_match and best_count > 0:
        return sanitize_answer(best_match["answer"])

    # Looser keyword match fallback
    for entry in KNOWLEDGE_BASE:
        for p in entry["patterns"]:
            words = p.split()
            if any(w in q for w in words if len(w) > 3):
                return sanitize_answer(entry["answer"])

    return sanitize_answer(FALLBACK)


SUGGESTED_QUESTIONS = [
    "What is an intelligent agent?",
    "What is the 8-puzzle problem?",
    "What is a state space?",
    "What is Breadth-First Search?",
    "What is Depth-First Search?",
    "What is A* Search?",
    "What is Manhattan Distance?",
    "What is the difference between BFS and DFS?",
    "What is the difference between informed and uninformed search?",
    "Why is A* useful for solving the 8-puzzle?",
    "What are completeness and optimality?",
    "How does Bidirectional Search work?",
    "What is Uniform Cost Search?",
    "What is Iterative Deepening DFS?",
    "What is the Water Jug problem?",
    "How does graph search work?",
    "Which algorithm should I use?",
    "How is puzzle solvability determined?",
    "What is time and space complexity?",
    "What is path cost?",
    "How do I compare all search algorithms?",
    "What is Greedy Best-First Search?",
    "What is Depth-Limited Search?",
    "What is a problem formulation?",
    "What algorithms are implemented in this project?",
    "What is the difference between BFS and UCS?",
    "What is the difference between A* and Greedy?",
]
