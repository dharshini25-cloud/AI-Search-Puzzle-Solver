"""
Quiz question bank for the AI Learning Quiz.
Comprehensive coverage of all eight search algorithms across three difficulty levels
(Beginner, Intermediate, Advanced), plus General AI, State Space, Heuristics,
Water Jug, and Graph Search.

Total Questions: 262
Each question has:
  - question (str)
  - options (list of 4 strings)
  - answer_index (0-3)
  - explanation (str)
  - difficulty ("Beginner", "Intermediate", "Advanced")
  - category (str)
"""

QUIZ_QUESTIONS = [
    {
        "question": "Which data structure is primarily used to implement Breadth-First Search?",
        "options": [
            "Queue (FIFO)",
            "Stack (LIFO)",
            "Priority Queue",
            "Binary Search Tree"
        ],
        "answer_index": 0,
        "explanation": "BFS visits nodes in order of their discovery level, requiring a First-In-First-Out (FIFO) queue.",
        "difficulty": "Beginner",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "How does Breadth-First Search traverse a search tree?",
        "options": [
            "Level by level, exploring all nodes at depth d before depth d+1",
            "Branch by branch, exploring to the maximum depth first",
            "By prioritizing nodes with the lowest heuristic value",
            "Randomly picking unvisited nodes"
        ],
        "answer_index": 0,
        "explanation": "BFS systematically explores all nodes at the current depth level before proceeding to nodes at the next depth.",
        "difficulty": "Beginner",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "Is Breadth-First Search an informed or uninformed search algorithm?",
        "options": [
            "Uninformed (Blind)",
            "Informed (Heuristic)",
            "Adversarial",
            "Metaheuristic"
        ],
        "answer_index": 0,
        "explanation": "BFS does not use problem-specific heuristic information about how close a state is to the goal, making it an uninformed search.",
        "difficulty": "Beginner",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "In an unweighted graph where every step cost is 1, BFS is guaranteed to find:",
        "options": [
            "The shortest path (fewest edges) to the goal",
            "A path with the most edges",
            "The path with the highest heuristic",
            "Any random path"
        ],
        "answer_index": 0,
        "explanation": "Because BFS explores level-by-level, the first time it reaches the goal node it has found a path with the fewest edges.",
        "difficulty": "Beginner",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "What is the main practical drawback of Breadth-First Search?",
        "options": [
            "High memory consumption because all frontier nodes are stored",
            "It gets stuck in infinite loops on finite trees",
            "It cannot find a solution even if one exists",
            "It requires computing complex heuristic distances"
        ],
        "answer_index": 0,
        "explanation": "Because BFS stores every node on the frontier, its space requirement grows exponentially with depth, often exhausting RAM.",
        "difficulty": "Beginner",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "What happens when the goal node is the root node in BFS?",
        "options": [
            "BFS terminates immediately with 0 moves",
            "BFS must explore the entire tree",
            "BFS reports no solution",
            "BFS crashes"
        ],
        "answer_index": 0,
        "explanation": "The initial goal test succeeds immediately at the start node, returning a path of length 0.",
        "difficulty": "Beginner",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "In standard BFS, when is the goal test typically applied to be most efficient?",
        "options": [
            "As soon as a child node is generated",
            "When a node is popped from the queue",
            "After the queue becomes empty",
            "Only at leaf nodes"
        ],
        "answer_index": 0,
        "explanation": "In uninformed BFS with unit costs, goal-testing child nodes at generation time saves expanding an entire additional tree level.",
        "difficulty": "Beginner",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "For a search tree with branching factor b and solution depth d, what is the space complexity of BFS?",
        "options": [
            "O(b^d)",
            "O(b * d)",
            "O(d)",
            "O(1)"
        ],
        "answer_index": 0,
        "explanation": "BFS holds all leaf nodes of the search tree at depth d in memory, yielding O(b^d) space complexity.",
        "difficulty": "Beginner",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "How does BFS avoid revisiting already explored states in graph search?",
        "options": [
            "By maintaining an explored / visited set",
            "By limiting recursion depth to 10",
            "By sorting the frontier",
            "By clearing the queue every step"
        ],
        "answer_index": 0,
        "explanation": "A visited set prevents BFS from expanding the same state multiple times, avoiding infinite cycles in graphs.",
        "difficulty": "Beginner",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "In the 8-puzzle, if BFS is run from a solvable start state, will it find the optimal solution?",
        "options": [
            "Yes, because each tile slide has an identical step cost of 1",
            "No, BFS never finds optimal solutions",
            "Only if Manhattan distance is enabled",
            "Only if the blank is in the center"
        ],
        "answer_index": 0,
        "explanation": "For the 8-puzzle where every move has step cost 1, the path with the fewest edges is optimal, which BFS guarantees.",
        "difficulty": "Beginner",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "If a tree has branching factor b = 10 and each node takes 100 bytes, approximately how much memory does BFS require at depth d = 5?",
        "options": [
            "~10 Megabytes (100,000 nodes * 100 bytes)",
            "~100 Kilobytes",
            "~10 Gigabytes",
            "~1 Kilobyte"
        ],
        "answer_index": 0,
        "explanation": "At depth 5, the frontier contains b^d = 10^5 = 100,000 nodes. 100,000 * 100 bytes = 10 MB.",
        "difficulty": "Intermediate",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "Why is BFS considered complete on graphs with finite branching factor?",
        "options": [
            "It systematically explores all finite depths in sequence until reaching depth d",
            "It uses a heuristic that never overestimates",
            "It backtracks when depth limit L is reached",
            "It searches from start and goal simultaneously"
        ],
        "answer_index": 0,
        "explanation": "If a solution exists at finite depth d and the branching factor b is finite, BFS must reach and explore depth d in a finite number of steps.",
        "difficulty": "Intermediate",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "What occurs if BFS is applied to a graph with non-uniform (varying) positive edge costs?",
        "options": [
            "It finds the path with the fewest edges, which may not have the lowest total cost",
            "It automatically adjusts and finds the minimum-cost path",
            "It fails to terminate",
            "It behaves exactly like A*"
        ],
        "answer_index": 0,
        "explanation": "BFS measures depth by number of steps, not edge weights. For non-uniform costs, Uniform Cost Search (UCS) is required for optimality.",
        "difficulty": "Intermediate",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "In graph search BFS, when should an unvisited node be added to the visited set?",
        "options": [
            "Immediately upon generation and enqueueing",
            "Only after all its children are generated",
            "Only when popped from the queue",
            "Never"
        ],
        "answer_index": 0,
        "explanation": "Marking a node visited at generation time prevents duplicate copies from being added to the queue by other nodes on the same level.",
        "difficulty": "Intermediate",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "What is the time complexity of BFS in big-O notation, where b is branching factor and d is solution depth?",
        "options": [
            "O(b^d)",
            "O(b * d)",
            "O(d^b)",
            "O(log(b^d))"
        ],
        "answer_index": 0,
        "explanation": "BFS explores 1 + b + b^2 + ... + b^d nodes, which is dominated by the last level b^d, giving O(b^d).",
        "difficulty": "Intermediate",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "Compared to Depth-First Search (DFS), BFS is advantageous because:",
        "options": [
            "It cannot get trapped in an infinite-depth path",
            "It requires significantly less memory",
            "It runs in O(1) space",
            "It uses a heuristic evaluation function"
        ],
        "answer_index": 0,
        "explanation": "DFS can follow an infinite path without ever backtracking, whereas BFS explores breadth-wise and guarantees finding shallow solutions.",
        "difficulty": "Intermediate",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "If two goals exist at depths 3 and 7 in an unweighted tree, which one will BFS return?",
        "options": [
            "The goal at depth 3",
            "The goal at depth 7",
            "Both goals simultaneously",
            "Neither, BFS errors on multiple goals"
        ],
        "answer_index": 0,
        "explanation": "BFS visits all nodes at depth 3 before any node at depth 4, 5, 6, or 7, so it discovers and returns the shallower goal first.",
        "difficulty": "Intermediate",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "How is the actual solution path reconstructed once BFS reaches the goal?",
        "options": [
            "By following parent pointers backward from the goal to the root",
            "By re-running BFS in reverse",
            "By sorting the visited set",
            "By inspecting the elements remaining in the queue"
        ],
        "answer_index": 0,
        "explanation": "Each node stores a reference to its parent; backtracking from the goal node to the root constructs the solution sequence.",
        "difficulty": "Intermediate",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "What is the memory ratio of space required by BFS compared to IDDFS at depth d?",
        "options": [
            "BFS requires O(b^d) memory, while IDDFS requires only O(b * d)",
            "Both require identical O(b^d) memory",
            "BFS requires O(b * d), while IDDFS requires O(b^d)",
            "IDDFS requires twice the memory of BFS"
        ],
        "answer_index": 0,
        "explanation": "IDDFS re-expands nodes rather than storing them, cutting memory from exponential O(b^d) down to linear O(b * d).",
        "difficulty": "Intermediate",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "In the 8-puzzle state space, the maximum possible shortest solution depth is:",
        "options": [
            "31 moves",
            "12 moves",
            "80 moves",
            "181,440 moves"
        ],
        "answer_index": 0,
        "explanation": "The 'God's Number' for the standard 8-puzzle is 31 moves; BFS can theoretically solve any solvable 8-puzzle in at most 31 steps.",
        "difficulty": "Intermediate",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "Why is early goal testing (at generation) valid for BFS with unit step costs, but invalid for Uniform Cost Search?",
        "options": [
            "In UCS, an enqueued node with lower cost might still be discovered later via another path",
            "In UCS, nodes are not stored in memory",
            "In BFS, step costs can be negative",
            "In UCS, the branching factor is infinite"
        ],
        "answer_index": 0,
        "explanation": "UCS must wait until a node is popped from the priority queue to guarantee that no cheaper path exists to that node.",
        "difficulty": "Advanced",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "If the branching factor b is large (e.g. b=100) and solution depth d=4, what percentage of total nodes generated by BFS are in the final level?",
        "options": [
            "Over 99%",
            "About 50%",
            "About 25%",
            "Less than 10%"
        ],
        "answer_index": 0,
        "explanation": "At b=100, b^4 = 100,000,000 while the sum of all previous levels is ~1,010,101, meaning >99% of nodes reside at the deepest level.",
        "difficulty": "Advanced",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "In a graph containing directed cycles, what happens if standard tree-search BFS (without an explored set) is executed?",
        "options": [
            "It enters an infinite loop generating redundant states",
            "It automatically converts cycles into undirected trees",
            "It raises an immediate recursion overflow error",
            "It terminates with an incorrect path cost of 0"
        ],
        "answer_index": 0,
        "explanation": "Tree search does not track visited states; upon encountering a cycle, it endlessly enqueues already-visited states.",
        "difficulty": "Advanced",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "How does bidirectional BFS improve upon standard unidirectional BFS asymptotically?",
        "options": [
            "It reduces time and space from O(b^d) to O(b^(d/2))",
            "It eliminates the branching factor completely",
            "It converts exponential space into logarithmic space",
            "It guarantees optimality on negative edge weights"
        ],
        "answer_index": 0,
        "explanation": "Two searches meeting at depth d/2 explore roughly 2 * b^(d/2) nodes, which is exponentially smaller than b^d for large d.",
        "difficulty": "Advanced",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "When comparing BFS and Dijkstra's algorithm on a graph where all edges have identical weight w > 0:",
        "options": [
            "BFS produces the exact same shortest path and node exploration order as Dijkstra's algorithm",
            "Dijkstra expands exponentially fewer nodes than BFS",
            "BFS fails to find the shortest path",
            "Dijkstra does not terminate on uniform weights"
        ],
        "answer_index": 0,
        "explanation": "When all edge weights are identical, Dijkstra's priority queue behaves exactly like a standard FIFO queue, matching BFS exploration.",
        "difficulty": "Advanced",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "Suppose state space memory is constrained to 4 GB. At approximately what solution depth does BFS become infeasible for b=3 (8-puzzle) assuming 32 bytes per node?",
        "options": [
            "Depth ~17 (3^17 * 32 bytes \u2248 4.1 GB)",
            "Depth ~5",
            "Depth ~50",
            "Depth ~100"
        ],
        "answer_index": 0,
        "explanation": "At d=17, 3^17 \u2248 129 million nodes * 32 bytes \u2248 4.1 GB, making BFS impossible without external memory or heuristic pruning.",
        "difficulty": "Advanced",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "What is the relationship between BFS and Uniform Cost Search (UCS)?",
        "options": [
            "BFS is a special case of UCS where all step costs are equal constants",
            "UCS is a special case of BFS where heuristics are used",
            "BFS and UCS are completely unrelated search paradigms",
            "UCS is always faster than BFS on unweighted graphs"
        ],
        "answer_index": 0,
        "explanation": "When step cost c(n, a, n') = 1 for all transitions, g(n) = depth(n), so priority ordering by g(n) is identical to FIFO queueing.",
        "difficulty": "Advanced",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "In 8-puzzle graph search BFS, what is the maximum size of the visited set across the entire state space?",
        "options": [
            "181,440 states (the size of one reachable component, 9!/2)",
            "362,880 states",
            "9! * 2 states",
            "Infinite states"
        ],
        "answer_index": 0,
        "explanation": "The 8-puzzle state space is divided into two disjoint reachable components of 9!/2 = 181,440 states each; graph search visits at most one component.",
        "difficulty": "Advanced",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "Why does BFS guarantee optimality even when the search tree has multiple paths to the goal?",
        "options": [
            "Because all paths of length k are checked before any path of length k+1",
            "Because it sorts the queue by edge weights",
            "Because it uses an admissible heuristic",
            "Because it performs depth-first backtracking"
        ],
        "answer_index": 0,
        "explanation": "Exploring strictly in increasing order of path length ensures the first encountered goal path has the minimal number of steps.",
        "difficulty": "Advanced",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "If a state space has infinite depth but finite branching factor and no solution exists, how does BFS behave?",
        "options": [
            "It runs indefinitely without terminating, expanding increasingly deep levels",
            "It detects that no solution exists within finite time",
            "It raises a Python RecursionError",
            "It backtracks to the root and reports failure"
        ],
        "answer_index": 0,
        "explanation": "Without a solution and with an infinite state space, BFS will continuously expand levels until memory is exhausted.",
        "difficulty": "Advanced",
        "category": "Breadth-First Search (BFS)"
    },
    {
        "question": "Which data structure is primarily used to implement Depth-First Search?",
        "options": [
            "Stack (LIFO)",
            "Queue (FIFO)",
            "Priority Queue",
            "Hash Map"
        ],
        "answer_index": 0,
        "explanation": "DFS explores down the deepest path first, which corresponds to Last-In-First-Out (LIFO) stack behavior.",
        "difficulty": "Beginner",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "How does Depth-First Search traverse a search space?",
        "options": [
            "By exploring as deep as possible along each branch before backtracking",
            "By checking all nodes level-by-level",
            "By choosing nodes with the lowest estimated distance to goal",
            "By expanding from the goal backward to the start"
        ],
        "answer_index": 0,
        "explanation": "DFS dives down a single branch until a dead end or depth limit is reached, then backtracks to explore alternatives.",
        "difficulty": "Beginner",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "What is the primary memory advantage of DFS over BFS?",
        "options": [
            "DFS only needs to store nodes along the current path and unexpanded siblings (linear space)",
            "DFS does not require any memory at all",
            "DFS uses a priority queue which compresses states",
            "DFS explores the entire graph in O(1) time"
        ],
        "answer_index": 0,
        "explanation": "The space complexity of DFS is O(b * m), which is linear with respect to maximum depth, unlike BFS's exponential O(b^d).",
        "difficulty": "Beginner",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "Is standard Depth-First Search guaranteed to find the shortest path to a goal?",
        "options": [
            "No, it returns the first path found, which may be very long or suboptimal",
            "Yes, DFS always finds the optimal path",
            "Yes, as long as edge costs are positive",
            "Only if the graph has no cycles"
        ],
        "answer_index": 0,
        "explanation": "DFS follows whatever branch it encounters first; if that branch leads to a goal, it returns that path regardless of length.",
        "difficulty": "Beginner",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "What can happen to standard DFS on an infinite search tree or a graph with cycles?",
        "options": [
            "It can get trapped in an infinite loop or infinite path and never terminate",
            "It automatically switches to BFS",
            "It immediately outputs the optimal path",
            "It resets the search tree to the root"
        ],
        "answer_index": 0,
        "explanation": "Without cycle detection or a depth limit, DFS will continue diving infinitely down a cyclic or unbounded branch.",
        "difficulty": "Beginner",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "What does 'backtracking' mean in Depth-First Search?",
        "options": [
            "Returning to the most recent predecessor node with unexplored branches when a dead end is reached",
            "Restarting the entire search from the root",
            "Reversing the direction of edges in the graph",
            "Deleting all visited states from memory"
        ],
        "answer_index": 0,
        "explanation": "When DFS hits a dead end (no valid successor), it pops the current node from the stack and backtracks to its parent.",
        "difficulty": "Beginner",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "What is the space complexity of DFS on a tree with branching factor b and maximum depth m?",
        "options": [
            "O(b * m)",
            "O(b^m)",
            "O(m^b)",
            "O(1)"
        ],
        "answer_index": 0,
        "explanation": "DFS stores only the current path of length m plus unexpanded sibling nodes at each depth level, giving O(b * m) space.",
        "difficulty": "Beginner",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "How is DFS commonly implemented in Python without an explicit stack data structure?",
        "options": [
            "Using recursive function calls (call stack)",
            "Using a while loop with a deque",
            "Using heapq",
            "Using SQLite"
        ],
        "answer_index": 0,
        "explanation": "Recursive function execution utilizes the system call stack, naturally providing LIFO depth-first traversal.",
        "difficulty": "Beginner",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "In the 8-Puzzle Solver of this project, why is DFS configured with a maximum depth limit (e.g. 30)?",
        "options": [
            "To prevent the search from diving into excessively deep paths or cycles",
            "Because the 8-puzzle cannot have solutions deeper than 10",
            "To make DFS calculate Manhattan distance",
            "To force DFS to behave as a heuristic search"
        ],
        "answer_index": 0,
        "explanation": "A depth cap restricts DFS exploration depth so it backtracks rather than wandering endlessly into deep loops.",
        "difficulty": "Beginner",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "Is Depth-First Search an informed or uninformed search algorithm?",
        "options": [
            "Uninformed (blind)",
            "Informed (heuristic)",
            "Adversarial",
            "Probabilistic"
        ],
        "answer_index": 0,
        "explanation": "DFS explores branches based solely on graph structure without estimating remaining distance to the goal.",
        "difficulty": "Beginner",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "What is the time complexity of DFS in the worst case, where b is branching factor and m is maximum depth?",
        "options": [
            "O(b^m)",
            "O(b * m)",
            "O(m)",
            "O(log(b))"
        ],
        "answer_index": 0,
        "explanation": "In the worst case, DFS may have to explore every single node in a tree of depth m before reaching the goal, giving O(b^m).",
        "difficulty": "Intermediate",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "If a goal state exists at depth 2 on the right branch of the root, but the left branch descends to depth 100 before dead-ending, what does DFS do?",
        "options": [
            "Explores the entire left branch to depth 100 before backtracking and finding the goal at depth 2",
            "Instantly jumps to the shallow goal at depth 2",
            "Switches to BFS automatically",
            "Reports failure immediately"
        ],
        "answer_index": 0,
        "explanation": "DFS rigidly explores the left subtree first; it must exhaust that entire deep branch before exploring the right branch.",
        "difficulty": "Intermediate",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "What data structure change converts a BFS implementation into a DFS implementation?",
        "options": [
            "Changing the FIFO queue (popleft) to a LIFO stack (pop)",
            "Changing a list to a dictionary",
            "Adding a heuristic priority calculation",
            "Replacing integers with floats"
        ],
        "answer_index": 0,
        "explanation": "Both algorithms follow the same general search loop; using a stack yields DFS, while a queue yields BFS.",
        "difficulty": "Intermediate",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "How does Graph-Search DFS avoid looping infinitely in cyclic graphs?",
        "options": [
            "By tracking visited nodes in a set and refusing to push or expand visited nodes",
            "By sorting nodes alphabetically",
            "By calculating edge weights",
            "By using multiple threads"
        ],
        "answer_index": 0,
        "explanation": "An explored/visited set ensures no state already expanded in the current or previous branches is re-expanded.",
        "difficulty": "Intermediate",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "Why is DFS often preferred in game search (like chess) over BFS?",
        "options": [
            "The tree depth is large and memory is limited; DFS uses far less memory than BFS",
            "DFS is guaranteed to find the shortest checkmate",
            "DFS requires no evaluation function",
            "DFS never needs to backtrack"
        ],
        "answer_index": 0,
        "explanation": "Game trees have vast branching factors; BFS memory would explode within seconds, whereas DFS explores deep paths in linear memory.",
        "difficulty": "Intermediate",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "In topological sorting of a Directed Acyclic Graph (DAG), which search algorithm is standardly used?",
        "options": [
            "Depth-First Search (DFS)",
            "Breadth-First Search (BFS)",
            "Greedy Best-First Search",
            "Water Jug Search"
        ],
        "answer_index": 0,
        "explanation": "DFS finish times naturally yield a reverse topological order of vertices in a DAG.",
        "difficulty": "Intermediate",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "If the maximum depth m of a state space is much larger than the optimal solution depth d (m >> d), DFS will typically:",
        "options": [
            "Perform poorly, potentially exploring huge irrelevant subtrees before finding the shallow goal",
            "Always beat BFS in time and moves",
            "Find the solution in exactly d steps",
            "Find the optimal solution on the first try"
        ],
        "answer_index": 0,
        "explanation": "When m >> d, DFS may wander deep into wrong paths, exploring up to O(b^m) nodes while the goal was sitting at depth d.",
        "difficulty": "Intermediate",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "What is the difference between node expansion order when children are pushed in order [A, B, C] onto a stack versus enqueued in a queue?",
        "options": [
            "Stack pops C first (reverse order), while queue dequeues A first (natural order)",
            "Both expand A first",
            "Stack expands B first",
            "Queue expands C first"
        ],
        "answer_index": 0,
        "explanation": "A LIFO stack pops the most recently pushed element first (C), whereas a FIFO queue serves the oldest element first (A).",
        "difficulty": "Intermediate",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "In Python, recursive DFS may crash with `RecursionError: maximum recursion depth exceeded`. What causes this?",
        "options": [
            "The search path exceeded Python's default stack limit (usually 1000 frames)",
            "The CPU ran out of arithmetic registers",
            "Streamlit ran out of session state keys",
            "The goal state had an odd number of inversions"
        ],
        "answer_index": 0,
        "explanation": "Python sets `sys.getrecursionlimit()` to prevent C-level stack overflow; deep recursive DFS paths easily exceed this limit.",
        "difficulty": "Intermediate",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "Can DFS be complete in a state space with finite states if graph cycle detection is enabled?",
        "options": [
            "Yes, because there are only finitely many distinct states to visit",
            "No, DFS is never complete under any circumstances",
            "Only if all edge weights are 1",
            "Only if an admissible heuristic is supplied"
        ],
        "answer_index": 0,
        "explanation": "In a finite state space, cycle detection ensures every state is visited at most once, guaranteeing termination and completeness.",
        "difficulty": "Intermediate",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "In an adversarial game tree search (Minimax), why is depth-first search preferred over breadth-first search?",
        "options": [
            "DFS allows alpha-beta pruning to prune entire subtrees based on values found along deep paths",
            "DFS evaluates every leaf simultaneously",
            "BFS cannot evaluate win/loss positions",
            "BFS uses too much CPU time for arithmetic"
        ],
        "answer_index": 0,
        "explanation": "Alpha-beta pruning requires bounds from completed subtrees deep in the tree to prune sibling branches; DFS enables this in minimal memory.",
        "difficulty": "Advanced",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "Why is path-checking (checking if a child is on the current ancestor path) different from full visited-set graph search in DFS?",
        "options": [
            "Path-checking uses O(m) memory but may re-explore the same state reached via different branches; full visited set uses O(V) memory",
            "Path-checking uses O(V) memory while visited set uses O(1) memory",
            "Path-checking makes DFS optimal",
            "They are completely identical in both time and space"
        ],
        "answer_index": 0,
        "explanation": "Checking only ancestor nodes preserves linear O(m) space, but risks exponential re-exploration of states reached via separate paths.",
        "difficulty": "Advanced",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "Suppose a graph has N nodes and M edges. What is the exact time complexity of graph-search DFS with an adjacency list and boolean visited array?",
        "options": [
            "O(N + M)",
            "O(N * M)",
            "O(N^2)",
            "O(M^2)"
        ],
        "answer_index": 0,
        "explanation": "Every vertex is visited once and every edge is traversed at most twice (or once for directed), yielding O(V + E) = O(N + M).",
        "difficulty": "Advanced",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "In the 8-puzzle, why does unconstrained DFS frequently produce solutions with dozens or hundreds of moves for a puzzle solvable in 6 moves?",
        "options": [
            "Because it dives deep into valid but tortuous paths, returning the first path reaching the goal without comparing length",
            "Because of numerical rounding errors in tile coordinates",
            "Because the Manhattan distance of DFS is inverted",
            "Because the blank tile cannot move backward in DFS"
        ],
        "answer_index": 0,
        "explanation": "DFS doesn't consider path cost; it happily wanders through 30+ moves of convoluted sliding before happening upon the goal state.",
        "difficulty": "Advanced",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "What is the chromatic property of DFS tree edges, back edges, forward edges, and cross edges in a directed graph?",
        "options": [
            "A back edge leads from a node to an ancestor in the DFS tree, indicating a directed cycle",
            "A forward edge indicates an infinite loop",
            "Cross edges only occur in undirected graphs",
            "Tree edges always have negative weights"
        ],
        "answer_index": 0,
        "explanation": "In directed graph DFS classification, an edge leading to an active ancestor on the recursion stack is a back edge, proving a cycle exists.",
        "difficulty": "Advanced",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "How does Tarjan's strongly connected components (SCC) algorithm utilize DFS?",
        "options": [
            "It uses DFS discovery times and low-link values on the recursion stack to identify maximal strongly connected subgraphs in O(V+E)",
            "It runs BFS from every vertex",
            "It uses A* heuristics to estimate component size",
            "It solves the 8-puzzle by decomposing tiles into SCCs"
        ],
        "answer_index": 0,
        "explanation": "Tarjan's algorithm uses a single pass of DFS tracking discovery time and lowest reachable ancestors to partition a graph into SCCs in linear time.",
        "difficulty": "Advanced",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "If DFS is modified to explore children in random order, does it become an optimal search algorithm?",
        "options": [
            "No, randomization does not change the fact that DFS returns the first path found without optimality checks",
            "Yes, random DFS is statistically optimal",
            "Yes, because random walks always find the shortest path",
            "It guarantees O(1) time complexity"
        ],
        "answer_index": 0,
        "explanation": "Randomizing successor order may alter which solution is reached first, but it provides no guarantee of finding the shortest path.",
        "difficulty": "Advanced",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "Under what specific condition would DFS find the optimal path in a uniform-cost tree?",
        "options": [
            "If all solutions happen to be at the exact same depth and the first branch explored hits a solution",
            "Whenever the branching factor is even",
            "When the start node has 4 neighbors",
            "Never under any circumstances"
        ],
        "answer_index": 0,
        "explanation": "If all goals exist at depth d and the search hits one on its first descent, that path has length d and is trivially minimal.",
        "difficulty": "Advanced",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "How does iterative deepening solve DFS's flaw of potentially infinite paths without losing its linear space advantage?",
        "options": [
            "By repeatedly calling DFS with bounded limits (0, 1, 2, ...), ensuring completeness and optimality while retaining O(b*d) space",
            "By allocating more RAM to the stack",
            "By running BFS backwards from the goal",
            "By using genetic algorithms"
        ],
        "answer_index": 0,
        "explanation": "Iterative Deepening DFS (IDDFS) successively increases a depth cap, ensuring no path deeper than the shallowest goal is explored.",
        "difficulty": "Advanced",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "When DFS is implemented iteratively using an explicit Python list as a stack, how should successors be pushed so that child 0 is explored first?",
        "options": [
            "Push successors in reverse order (e.g. child 3, child 2, child 1, child 0)",
            "Push successors in normal order",
            "Push only the first child",
            "Sort children by their string representation"
        ],
        "answer_index": 0,
        "explanation": "Because a stack is LIFO, pushing in reverse order places child 0 on top of the stack, ensuring it is popped and explored first.",
        "difficulty": "Advanced",
        "category": "Depth-First Search (DFS)"
    },
    {
        "question": "What is the evaluation function used by A* Search?",
        "options": [
            "f(n) = g(n) + h(n)",
            "f(n) = h(n)",
            "f(n) = g(n)",
            "f(n) = g(n) - h(n)"
        ],
        "answer_index": 0,
        "explanation": "A* evaluates nodes using f(n) = g(n) + h(n), where g(n) is the exact cost from start to n, and h(n) is the estimated cost from n to the goal.",
        "difficulty": "Beginner",
        "category": "A* Search"
    },
    {
        "question": "In A* Search, what does g(n) represent?",
        "options": [
            "The exact path cost accumulated from the start node to node n",
            "The estimated cost from node n to the goal",
            "The depth limit of the search tree",
            "The number of unvisited neighbors of node n"
        ],
        "answer_index": 0,
        "explanation": "g(n) is the true cost of reaching node n from the initial state along the current path.",
        "difficulty": "Beginner",
        "category": "A* Search"
    },
    {
        "question": "In A* Search, what does h(n) represent?",
        "options": [
            "The estimated heuristic cost to reach the goal from node n",
            "The actual cost paid so far from the start node",
            "The maximum branching factor of the tree",
            "The time elapsed in seconds"
        ],
        "answer_index": 0,
        "explanation": "h(n) is the heuristic function estimating the remaining distance from state n to the nearest goal state.",
        "difficulty": "Beginner",
        "category": "A* Search"
    },
    {
        "question": "Which data structure is essential for implementing the frontier in A* Search?",
        "options": [
            "Priority Queue (Min-Heap)",
            "FIFO Queue",
            "LIFO Stack",
            "Circular Buffer"
        ],
        "answer_index": 0,
        "explanation": "A* must continuously extract the node with the minimum f(n) value, which is efficiently implemented via a min-heap priority queue.",
        "difficulty": "Beginner",
        "category": "A* Search"
    },
    {
        "question": "What does it mean for a heuristic h(n) to be 'admissible'?",
        "options": [
            "It never overestimates the true minimal cost to reach the goal: h(n) <= h*(n)",
            "It is always strictly greater than the true cost",
            "It returns negative numbers for dead ends",
            "It requires polynomial time to calculate"
        ],
        "answer_index": 0,
        "explanation": "Admissibility means the heuristic is optimistic: it never guesses a cost higher than the true shortest path to the goal.",
        "difficulty": "Beginner",
        "category": "A* Search"
    },
    {
        "question": "If the heuristic h(n) = 0 for all nodes, what standard algorithm does A* Search become?",
        "options": [
            "Uniform Cost Search (Dijkstra's Algorithm)",
            "Depth-First Search",
            "Greedy Best-First Search",
            "Bidirectional BFS"
        ],
        "answer_index": 0,
        "explanation": "When h(n) = 0, f(n) = g(n) + 0 = g(n), so nodes are prioritized strictly by cumulative path cost, which is Uniform Cost Search.",
        "difficulty": "Beginner",
        "category": "A* Search"
    },
    {
        "question": "Is A* Search an informed or uninformed search algorithm?",
        "options": [
            "Informed (Heuristic)",
            "Uninformed (Blind)",
            "Randomized",
            "Unsupervised"
        ],
        "answer_index": 0,
        "explanation": "A* uses domain-specific knowledge via the heuristic function h(n) to guide exploration, making it an informed search algorithm.",
        "difficulty": "Beginner",
        "category": "A* Search"
    },
    {
        "question": "Which heuristic is standardly used for the 8-puzzle in this application?",
        "options": [
            "Manhattan Distance",
            "Euclidean Distance",
            "Random Walk",
            "Hamming Distance exclusively"
        ],
        "answer_index": 0,
        "explanation": "Manhattan Distance (sum of vertical and horizontal grid displacements for all non-blank tiles) is admissible and highly effective for the 8-puzzle.",
        "difficulty": "Beginner",
        "category": "A* Search"
    },
    {
        "question": "Under what condition is A* guaranteed to return an optimal solution in tree search?",
        "options": [
            "When the heuristic function h(n) is admissible",
            "When the heuristic function h(n) is zero everywhere",
            "When all edge weights are negative",
            "When branching factor b = 1"
        ],
        "answer_index": 0,
        "explanation": "For tree search, an admissible heuristic guarantees that A* will find the optimal (lowest cost) path to a goal.",
        "difficulty": "Beginner",
        "category": "A* Search"
    },
    {
        "question": "Why is A* generally preferred over BFS for solving the 8-puzzle?",
        "options": [
            "A* explores far fewer nodes by focusing search toward the goal while still guaranteeing optimality",
            "A* uses less memory than DFS",
            "A* does not require a goal state definition",
            "A* only works on unsolvable puzzles"
        ],
        "answer_index": 0,
        "explanation": "Heuristic guidance prunes unpromising branches, allowing A* to solve puzzles expanding 10x to 1000x fewer nodes than blind BFS.",
        "difficulty": "Beginner",
        "category": "A* Search"
    },
    {
        "question": "What does it mean for a heuristic h(n) to be 'consistent' (or monotonic)?",
        "options": [
            "For every node n and successor n' generated by action a: h(n) <= c(n, a, n') + h(n')",
            "h(n) is always equal to g(n)",
            "h(n) decreases to negative values",
            "h(n) overestimates only at the root"
        ],
        "answer_index": 0,
        "explanation": "Consistency satisfies the triangle inequality: the estimated cost from n cannot exceed the step cost to n' plus the estimated cost from n'.",
        "difficulty": "Intermediate",
        "category": "A* Search"
    },
    {
        "question": "In graph search, why is consistency of h(n) important for A*?",
        "options": [
            "It guarantees that the first time any state is expanded, the path found to it is optimal, eliminating the need to re-open closed nodes",
            "It makes A* run in linear O(d) space",
            "It allows negative edge weights without infinite loops",
            "It guarantees f(n) = 0 for all nodes"
        ],
        "answer_index": 0,
        "explanation": "With a consistent heuristic, f(n) values are monotonically non-decreasing along any path, so expanding a node guarantees its g(n) is minimal.",
        "difficulty": "Intermediate",
        "category": "A* Search"
    },
    {
        "question": "Between two admissible heuristics h1 and h2 for the same problem, if h2(n) >= h1(n) for all nodes n, we say:",
        "options": [
            "h2 dominates h1, and A* using h2 will never expand more nodes than A* using h1 (except possibly tie-breaks)",
            "h1 dominates h2",
            "h2 is inadmissible",
            "Both heuristics are invalid"
        ],
        "answer_index": 0,
        "explanation": "A heuristic with higher values that remain admissible is more informative (dominates) and prunes at least as many nodes as the lower heuristic.",
        "difficulty": "Intermediate",
        "category": "A* Search"
    },
    {
        "question": "Why does Manhattan Distance dominate the Misplaced Tiles heuristic in the 8-puzzle?",
        "options": [
            "Every misplaced tile must move at least 1 step, and its Manhattan distance is always >= 1",
            "Manhattan distance counts the blank tile",
            "Misplaced tiles heuristic is inadmissible",
            "Manhattan distance is faster to compute"
        ],
        "answer_index": 0,
        "explanation": "A tile not in its goal position has Manhattan distance >= 1, so h_Manhattan(n) >= h_Misplaced(n) for all states n, making Manhattan dominate.",
        "difficulty": "Intermediate",
        "category": "A* Search"
    },
    {
        "question": "When does A* terminate and declare success?",
        "options": [
            "When a goal node is popped from the priority queue (selected for expansion)",
            "As soon as a goal node is generated and pushed onto the priority queue",
            "When the frontier becomes completely empty",
            "When f(n) reaches infinity"
        ],
        "answer_index": 0,
        "explanation": "Testing for the goal upon popping ensures that no other node in the priority queue has a lower f(n) cost.",
        "difficulty": "Intermediate",
        "category": "A* Search"
    },
    {
        "question": "What is the primary practical bottleneck of A* Search on complex problems?",
        "options": [
            "Memory consumption: like BFS, it keeps all generated nodes in memory (O(b^d))",
            "It gets stuck in infinite loops",
            "It cannot use multiple heuristic functions",
            "It does not work on graphs with cycles"
        ],
        "answer_index": 0,
        "explanation": "A* retains both the open list (frontier) and closed list (explored set) in RAM, typically running out of memory before running out of time.",
        "difficulty": "Intermediate",
        "category": "A* Search"
    },
    {
        "question": "If h(n) is admissible but NOT consistent, how must graph-search A* be modified to preserve optimality?",
        "options": [
            "Nodes in the closed list must be allowed to be re-opened if a strictly cheaper path is discovered later",
            "The search must immediately abort",
            "All edge costs must be multiplied by -1",
            "The priority queue must be replaced with a LIFO stack"
        ],
        "answer_index": 0,
        "explanation": "Without consistency, a node may be closed via a suboptimal path; discovering a cheaper path requires updating g and re-inserting it into the frontier.",
        "difficulty": "Intermediate",
        "category": "A* Search"
    },
    {
        "question": "How is a tie broken when two nodes in A*'s priority queue have identical f(n) values?",
        "options": [
            "By choosing the node with the higher g(n) (lower h(n)), or using a unique insertion counter",
            "By deleting both nodes",
            "By restarting the search from the root",
            "By picking the node with the largest state value"
        ],
        "answer_index": 0,
        "explanation": "Breaking ties in favor of higher g(n) prefers nodes closer to the goal, significantly reducing unnecessary expansions at the same f-contour.",
        "difficulty": "Intermediate",
        "category": "A* Search"
    },
    {
        "question": "What is the f-value of the start node if start != goal in A* Search?",
        "options": [
            "f(start) = 0 + h(start) = h(start)",
            "f(start) = 0",
            "f(start) = infinity",
            "f(start) = 1"
        ],
        "answer_index": 0,
        "explanation": "Since 0 steps have been taken from the start, g(start) = 0, so f(start) = g(start) + h(start) = h(start).",
        "difficulty": "Intermediate",
        "category": "A* Search"
    },
    {
        "question": "In a search space where the optimal solution cost is C*, what can be said about all nodes expanded by A* with an admissible heuristic?",
        "options": [
            "Every expanded node n satisfies f(n) <= C*",
            "Every expanded node has f(n) > C*",
            "Nodes with f(n) = 0 are never expanded",
            "All expanded nodes have g(n) = C*"
        ],
        "answer_index": 0,
        "explanation": "A* never expands any node with f(n) > C* because the goal node with f = C* will be expanded before any node with higher f.",
        "difficulty": "Intermediate",
        "category": "A* Search"
    },
    {
        "question": "Can an admissible heuristic be inconsistent? If so, give a condition.",
        "options": [
            "Yes, consistency is a stronger requirement than admissibility; a heuristic can be admissible everywhere but violate triangle inequality locally",
            "No, all admissible heuristics are automatically consistent",
            "No, all consistent heuristics are inadmissible",
            "Only on directed graphs with negative weights"
        ],
        "answer_index": 0,
        "explanation": "While consistency implies admissibility (assuming h(goal)=0), the reverse is not true: local jumps in h can violate h(n) <= c + h(n') while still underestimating total cost.",
        "difficulty": "Advanced",
        "category": "A* Search"
    },
    {
        "question": "What is IDA* (Iterative Deepening A*) and what major limitation of A* does it solve?",
        "options": [
            "It performs repeated depth-first search cutoffs based on f-limits, reducing memory from exponential O(b^d) to linear O(b * d)",
            "It replaces heuristics with neural networks",
            "It allows negative edge weights in A*",
            "It eliminates all node re-expansions"
        ],
        "answer_index": 0,
        "explanation": "IDA* uses f(n) cutoffs instead of depth cutoffs, combining A*'s heuristic guidance with DFS's linear memory footprint.",
        "difficulty": "Advanced",
        "category": "A* Search"
    },
    {
        "question": "What is the 'effective branching factor' b* of A* Search?",
        "options": [
            "The branching factor of a uniform tree of depth d that would contain N total nodes: N + 1 = 1 + b* + (b*)^2 + ... + (b*)^d",
            "The maximum number of neighbors of the goal node",
            "The ratio of execution time to memory used",
            "The number of tiles in the 8-puzzle"
        ],
        "answer_index": 0,
        "explanation": "Effective branching factor b* measures heuristic quality: a perfect heuristic has b* = 1, while blind search has b* close to b.",
        "difficulty": "Advanced",
        "category": "A* Search"
    },
    {
        "question": "What occurs if an inadmissible heuristic h(n) that overestimates true costs is used in A*?",
        "options": [
            "A* may find a suboptimal solution path because the optimal goal path may be pruned or delayed by an inflated f-cost",
            "A* is guaranteed to fail completely and find no path",
            "A* becomes identical to BFS",
            "A* enters an infinite loop"
        ],
        "answer_index": 0,
        "explanation": "Overestimating true cost can cause A* to expand a suboptimal path that appeared falsely cheaper, bypassing the true optimal path.",
        "difficulty": "Advanced",
        "category": "A* Search"
    },
    {
        "question": "If we have two admissible heuristics h1 and h2, which composite heuristic h_composite(n) = max(h1(n), h2(n)) is guaranteed to be:",
        "options": [
            "Admissible, consistent (if h1 and h2 are consistent), and dominate both h1 and h2",
            "Inadmissible because of the max operation",
            "Identical to h1 + h2",
            "Only usable in tree search"
        ],
        "answer_index": 0,
        "explanation": "Taking the pointwise maximum of admissible heuristics preserves admissibility while ensuring the combination is >= both, yielding superior pruning.",
        "difficulty": "Advanced",
        "category": "A* Search"
    },
    {
        "question": "What is Weighted A* search (f(n) = g(n) + w * h(n) where w > 1)?",
        "options": [
            "An epsilon-admissible search that trades guaranteed optimality for faster search, bounding suboptimality to at most w * C*",
            "An algorithm that finds optimal paths in O(1) time",
            "An algorithm that completely ignores g(n)",
            "A search that only works when w < 1"
        ],
        "answer_index": 0,
        "explanation": "Weighting h(n) by w > 1 biases search more greedily toward the goal, drastically reducing expansions while guaranteeing cost <= w * C*.",
        "difficulty": "Advanced",
        "category": "A* Search"
    },
    {
        "question": "Why is Manhattan Distance for the 8-puzzle consistent?",
        "options": [
            "Any single tile move changes that tile's Manhattan distance by at most +1 or -1, while the step cost is exactly 1, so |h(n) - h(n')| <= 1 = c(n,a,n')",
            "Because 8 is an even number",
            "Because the blank tile has Manhattan distance 0",
            "Because all 8-puzzles have 181,440 states"
        ],
        "answer_index": 0,
        "explanation": "One slide changes the moved tile's coordinates by 1 step. Thus h can decrease by at most 1, satisfying h(n) <= 1 + h(n').",
        "difficulty": "Advanced",
        "category": "A* Search"
    },
    {
        "question": "In the context of A* search, what is a 'pattern database' heuristic?",
        "options": [
            "A precomputed exact cost database for subproblems (e.g. solving only tiles 1-4) stored in memory as an admissible heuristic",
            "A machine learning pattern classifier",
            "A database of all 181,440 states and their solutions",
            "An SQLite table storing user search history"
        ],
        "answer_index": 0,
        "explanation": "Pattern databases store exact shortest distances for abstracted subproblems; because abstract moves cost <= real moves, they provide powerful admissible heuristics.",
        "difficulty": "Advanced",
        "category": "A* Search"
    },
    {
        "question": "What happens if an edge in a graph search problem has a negative cost c(u, v) < 0 in A* Search?",
        "options": [
            "A* can fail to find the optimal path or enter infinite negative-cost cycles, as f(n) monotonicity breaks",
            "A* automatically adds a constant to make all edges positive",
            "A* converts negative edges into Manhattan distances",
            "A* runs twice as fast"
        ],
        "answer_index": 0,
        "explanation": "Negative edge costs violate non-decreasing path costs, potentially allowing infinite cycling to reduce path cost indefinitely.",
        "difficulty": "Advanced",
        "category": "A* Search"
    },
    {
        "question": "Under what condition does A* expand the exact minimum number of nodes required by ANY optimal search algorithm with the same heuristic?",
        "options": [
            "A* is 'optimally efficient': no other optimal algorithm using the same heuristic can expand fewer nodes (up to tie-breaking)",
            "Only when all edge weights are 0",
            "Only on binary trees",
            "Only when the solution is at depth 1"
        ],
        "answer_index": 0,
        "explanation": "Dechter and Pearl (1985) proved that A* with a consistent heuristic is optimally efficient among all complete, optimal search algorithms.",
        "difficulty": "Advanced",
        "category": "A* Search"
    },
    {
        "question": "What is the evaluation function used by Greedy Best-First Search?",
        "options": [
            "f(n) = h(n)",
            "f(n) = g(n) + h(n)",
            "f(n) = g(n)",
            "f(n) = g(n) / h(n)"
        ],
        "answer_index": 0,
        "explanation": "Greedy Best-First Search evaluates nodes solely using the heuristic function f(n) = h(n), estimating cost to the goal.",
        "difficulty": "Beginner",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "Does Greedy Best-First Search take the accumulated path cost g(n) into account?",
        "options": [
            "No, it completely ignores g(n)",
            "Yes, it adds g(n) to h(n)",
            "Yes, it multiplies g(n) by h(n)",
            "Only at the root node"
        ],
        "answer_index": 0,
        "explanation": "Greedy search looks only at how close the current node appears to be to the goal (h(n)), disregarding how much cost was spent to get there.",
        "difficulty": "Beginner",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "Is Greedy Best-First Search guaranteed to find the optimal (shortest) solution?",
        "options": [
            "No, it often finds suboptimal solutions because it ignores path cost",
            "Yes, it is always optimal",
            "Yes, if the heuristic is admissible",
            "Yes, on unweighted graphs"
        ],
        "answer_index": 0,
        "explanation": "Because Greedy ignores past cost, it may take an enticing initial step that leads down a convoluted, high-cost path.",
        "difficulty": "Beginner",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "What is the primary advantage of Greedy Best-First Search over BFS and A* in practical problem solving?",
        "options": [
            "It is often much faster and explores fewer nodes when a good heuristic guides it directly to the goal",
            "It guarantees the shortest path",
            "It uses O(1) memory",
            "It never encounters dead ends"
        ],
        "answer_index": 0,
        "explanation": "By aggressively chasing lower heuristic values, Greedy often reaches a solution quickly, though the path length may be suboptimal.",
        "difficulty": "Beginner",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "Which data structure is used to implement Greedy Best-First Search?",
        "options": [
            "Priority Queue sorted by h(n)",
            "FIFO Queue",
            "LIFO Stack",
            "Simple Array"
        ],
        "answer_index": 0,
        "explanation": "Greedy search extracts the node with the lowest h(n) value from a min-heap priority queue.",
        "difficulty": "Beginner",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "Is Greedy Best-First Search an informed or uninformed search algorithm?",
        "options": [
            "Informed (Heuristic)",
            "Uninformed (Blind)",
            "Adversarial",
            "Randomized"
        ],
        "answer_index": 0,
        "explanation": "It uses a heuristic function h(n) to estimate proximity to the goal, categorizing it as an informed search.",
        "difficulty": "Beginner",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "What happens in Greedy Best-First Search when the goal node is reached?",
        "options": [
            "h(goal) = 0, so it has the lowest possible heuristic value and is expanded to end the search",
            "It continues searching for a shorter path",
            "It resets all node costs to 1",
            "It switches to DFS"
        ],
        "answer_index": 0,
        "explanation": "At the goal node, h(goal) = 0. In a min-heap, 0 is the minimum possible heuristic, ensuring the goal is popped and returned.",
        "difficulty": "Beginner",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "In the 8-puzzle, if Greedy Best-First Search uses Manhattan distance, can it solve puzzles?",
        "options": [
            "Yes, it frequently finds solutions quickly, but the move count may be higher than A*",
            "No, Greedy cannot solve 8-puzzles",
            "Only if the start state has 0 inversions",
            "Only on 2x2 puzzles"
        ],
        "answer_index": 0,
        "explanation": "Greedy effectively guides the tiles toward their goal slots, though it may take detour moves that A* would avoid.",
        "difficulty": "Beginner",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "In a tree search without cycle detection, can Greedy Best-First Search get trapped in an infinite loop?",
        "options": [
            "Yes, it can endlessly cycle between states that appear locally attractive",
            "No, Greedy never loops",
            "Only if all heuristics are zero",
            "Only on directed graphs"
        ],
        "answer_index": 0,
        "explanation": "Without a visited set, Greedy can bounce back and forth between two states that each appear to have lower h than alternative branches.",
        "difficulty": "Beginner",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "How does Greedy Best-First Search compare to A* Search?",
        "options": [
            "A* considers both past cost g(n) and future estimate h(n); Greedy only considers future estimate h(n)",
            "Greedy is optimal while A* is not",
            "A* does not use a heuristic",
            "Greedy uses a FIFO queue while A* uses a stack"
        ],
        "answer_index": 0,
        "explanation": "A* uses f(n) = g(n) + h(n) for balance and optimality; Greedy uses f(n) = h(n) for pure speed at the cost of optimality.",
        "difficulty": "Beginner",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "What is the worst-case time complexity of Greedy Best-First Search on a tree of depth m and branching factor b?",
        "options": [
            "O(b^m)",
            "O(b * d)",
            "O(m^2)",
            "O(1)"
        ],
        "answer_index": 0,
        "explanation": "In the worst case, a misleading heuristic can lead Greedy down a false path to maximum depth m, exploring up to O(b^m) nodes.",
        "difficulty": "Intermediate",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "What is the worst-case space complexity of Greedy Best-First Search?",
        "options": [
            "O(b^m) because all generated nodes are retained in the priority queue",
            "O(b * m) like DFS",
            "O(1)",
            "O(m)"
        ],
        "answer_index": 0,
        "explanation": "Like A*, Greedy retains all frontier nodes in its priority queue; in the worst case this requires O(b^m) memory.",
        "difficulty": "Intermediate",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "Can Greedy Best-First Search be complete in a finite state space?",
        "options": [
            "Yes, if cycle detection (graph search with an explored set) is implemented",
            "No, it is never complete under any circumstances",
            "Only if edge weights are negative",
            "Only if the graph is bipartite"
        ],
        "answer_index": 0,
        "explanation": "With an explored set preventing duplicate state expansions in a finite graph, Greedy must eventually terminate and find a solution if one exists.",
        "difficulty": "Intermediate",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "What is a 'local minimum' or 'heuristic plateau' in Greedy Best-First Search?",
        "options": [
            "A state where all successors have equal or worse heuristic values than the current state",
            "The global goal state",
            "A state with negative edge costs",
            "A node with branching factor 0"
        ],
        "answer_index": 0,
        "explanation": "A local minimum occurs when the heuristic misleads the search into a region where all neighbors appear farther from the goal.",
        "difficulty": "Intermediate",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "Suppose a start node has two paths to the goal: Path A has 2 steps of cost 50 each (total 100), and Path B has 10 steps of cost 1 each (total 10). If h favors Path A initially:",
        "options": [
            "Greedy will follow Path A and return a path of cost 100, missing the optimal cost 10 path",
            "Greedy will explore Path B because cost is lower",
            "Greedy will report no solution found",
            "Greedy will split between both paths"
        ],
        "answer_index": 0,
        "explanation": "Because Greedy is blind to edge costs and cumulative g(n), it commits to whichever path has lower initial h values.",
        "difficulty": "Intermediate",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "If the heuristic function h(n) is perfectly accurate (h(n) = h*(n) for all n), how does Greedy Best-First Search perform?",
        "options": [
            "It marches directly to the goal in d steps without expanding any extraneous nodes",
            "It still explores O(b^d) nodes",
            "It fails due to division by zero",
            "It behaves identically to BFS"
        ],
        "answer_index": 0,
        "explanation": "With a perfect heuristic, every step strictly decreases the true remaining distance, guiding Greedy straight to the optimal goal.",
        "difficulty": "Intermediate",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "In the Algorithm Lab of this application, when comparing A* and Greedy on the 'Medium' benchmark puzzle, you will typically observe:",
        "options": [
            "Greedy explores fewer nodes and runs faster, but A* finds a path with fewer or equal moves",
            "Greedy finds fewer moves than A*",
            "A* fails to solve the puzzle",
            "Both algorithms always explore identical node counts"
        ],
        "answer_index": 0,
        "explanation": "Greedy's aggressive heuristic pursuit often expands fewer nodes, but its final path length is frequently suboptimal compared to A*.",
        "difficulty": "Intermediate",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "What happens if Greedy Best-First Search is run with h(n) = constant for all nodes?",
        "options": [
            "It degrades into an arbitrary/random uninformed search depending on tie-breaking",
            "It becomes identical to A*",
            "It raises a ValueError",
            "It computes Manhattan distance automatically"
        ],
        "answer_index": 0,
        "explanation": "If h(n) is constant, all nodes in the priority queue have identical priority, reducing the search to queue tie-breaker order.",
        "difficulty": "Intermediate",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "Why is Greedy Best-First Search considered susceptible to 'false leads'?",
        "options": [
            "Because an action that decreases h by 1 might lead directly into a dead end or wall",
            "Because h(n) is always negative",
            "Because it modifies the goal state",
            "Because it uses random numbers"
        ],
        "answer_index": 0,
        "explanation": "A heuristic provides an estimate; moving closer in straight-line distance can trap the agent against an obstacle (like a maze wall).",
        "difficulty": "Intermediate",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "How does Greedy Best-First Search differ from Depth-First Search?",
        "options": [
            "Greedy uses a priority queue guided by h(n); DFS uses an unguided LIFO stack",
            "Greedy requires O(b*m) space while DFS requires exponential space",
            "Greedy is uninformed while DFS is informed",
            "There is no difference between them"
        ],
        "answer_index": 0,
        "explanation": "DFS blindly follows the most recently generated branch; Greedy prioritizes whichever available node has the lowest estimated goal distance.",
        "difficulty": "Intermediate",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "In route finding on a road map, if straight-line Euclidean distance is used as h(n), why can Greedy Best-First Search produce a dramatically suboptimal route?",
        "options": [
            "It may follow a winding local road heading straight toward the destination instead of an initial detour to an interstate highway",
            "Euclidean distance is inadmissible",
            "Euclidean distance cannot be computed in 2D",
            "Road maps cannot have heuristics"
        ],
        "answer_index": 0,
        "explanation": "A highway might initially head away from the goal (increasing h), so Greedy avoids it, choosing slow direct roads that ultimately take longer.",
        "difficulty": "Advanced",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "What is the susceptibility of Greedy Best-First Search to heuristic scaling (e.g. multiplying h(n) by a constant k > 0)?",
        "options": [
            "The search order is completely invariant to positive scaling: argmin(h) == argmin(k * h)",
            "Scaling changes Greedy into A*",
            "Multiplying by 10 makes Greedy find optimal paths",
            "Scaling causes the priority queue to invert"
        ],
        "answer_index": 0,
        "explanation": "Since Greedy ranks nodes solely by h(n), multiplying every heuristic by positive scalar k preserves the relative ranking of all nodes.",
        "difficulty": "Advanced",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "Can Greedy Best-First Search be combined with backtracking like DFS to create a linear-space heuristic search?",
        "options": [
            "Yes, this yields algorithms like Greedy DFS or recursive best-first search (RBFS)",
            "No, heuristics cannot be used with stacks",
            "No, priority queues cannot be cleared",
            "Only on graphs without branch points"
        ],
        "answer_index": 0,
        "explanation": "Sorting children by h(n) before pushing onto a DFS stack creates a depth-first greedy search that retains linear O(b*m) space.",
        "difficulty": "Advanced",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "In a graph where the goal is unreachable from the start node, how does graph-search Greedy Best-First Search behave?",
        "options": [
            "It expands every reachable node in the connected component before exhausting the frontier and reporting failure",
            "It loops infinitely between the two highest nodes",
            "It raises an immediate exception",
            "It returns a fabricated path"
        ],
        "answer_index": 0,
        "explanation": "With visited-set tracking in a finite component, once all reachable nodes are exhausted, the frontier empties and failure is reported.",
        "difficulty": "Advanced",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "Why is Greedy Best-First Search NOT guaranteed to be optimal even if h(n) is both admissible and consistent?",
        "options": [
            "Because optimality requires considering path cost g(n); ignoring g(n) allows high-cost paths to beat low-cost paths",
            "Admissible heuristics are forbidden in Greedy search",
            "Consistency only applies to BFS",
            "Greedy ignores the goal test"
        ],
        "answer_index": 0,
        "explanation": "Admissibility guarantees optimality only when combined with cumulative cost in f = g + h. Ignoring g throws away this guarantee.",
        "difficulty": "Advanced",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "How does beam search relate to Greedy Best-First Search?",
        "options": [
            "Beam search is Greedy Best-First Search with a bounded frontier that retains only the k best nodes at each step",
            "Beam search uses no heuristic",
            "Beam search is an unweighted BFS variant",
            "Beam search only works in quantum computing"
        ],
        "answer_index": 0,
        "explanation": "Beam search limits memory by pruning the priority queue to a fixed capacity k (the beam width), discarding less promising nodes.",
        "difficulty": "Advanced",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "In the 8-puzzle, suppose state S1 has h=2 and g=25, while state S2 has h=3 and g=2. Which node does Greedy expand first, and which does A* expand first?",
        "options": [
            "Greedy expands S1 first (h=2 < 3); A* expands S2 first (f=5 < 27)",
            "Both expand S1 first",
            "Both expand S2 first",
            "Greedy expands S2 first; A* expands S1 first"
        ],
        "answer_index": 0,
        "explanation": "Greedy only checks h (2 < 3, so S1 wins). A* checks f = g + h (S1 has f=27; S2 has f=5, so S2 wins by a landslide).",
        "difficulty": "Advanced",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "What is the mathematical condition for Greedy Best-First Search to explore an optimal path?",
        "options": [
            "Along the optimal path, every node's h value must be strictly lower than the h values of all competing frontier nodes",
            "All edge costs must equal 0",
            "The branching factor must be prime",
            "The heuristic must be inadmissible"
        ],
        "answer_index": 0,
        "explanation": "Greedy only stays on the optimal path if the heuristic never momentarily ranks an off-path node ahead of the on-path successor.",
        "difficulty": "Advanced",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "Why can Greedy Best-First Search suffer from high node expansion counts in maze problems with long dead-end corridors?",
        "options": [
            "The heuristic decreases as the agent moves closer to the goal inside the dead-end corridor, luring the search to the very end before failing",
            "Mazes cannot be represented as graphs",
            "Corridors invert the priority queue",
            "Manhattan distance is zero in mazes"
        ],
        "answer_index": 0,
        "explanation": "The agent walks straight toward the wall because straight-line distance drops with every step, only realizing at the cul-de-sac that it must backtrack.",
        "difficulty": "Advanced",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "Can bidirectional search be applied to Greedy Best-First Search?",
        "options": [
            "Yes, running forward greedy search from start and backward greedy search from goal, meeting when frontiers intersect",
            "No, Greedy cannot run backwards",
            "Only if the graph is a tree",
            "Only on directed acyclic graphs"
        ],
        "answer_index": 0,
        "explanation": "Bidirectional greedy search evaluates forward nodes using h_goal(n) and backward nodes using h_start(n), stopping when frontiers collide.",
        "difficulty": "Advanced",
        "category": "Greedy Best-First Search"
    },
    {
        "question": "What is the fundamental idea behind Bidirectional Search?",
        "options": [
            "Running two simultaneous searches: one forward from start, one backward from goal, meeting in the middle",
            "Searching with two different computers",
            "Searching using both BFS and DFS simultaneously",
            "Evaluating two heuristics at the same time"
        ],
        "answer_index": 0,
        "explanation": "Bidirectional Search expands states from both the initial state and the goal state until their search frontiers intersect.",
        "difficulty": "Beginner",
        "category": "Bidirectional Search"
    },
    {
        "question": "When does Bidirectional Search terminate successfully?",
        "options": [
            "When a node generated by one search already exists in the other search's explored or frontier set",
            "When both frontiers are completely empty",
            "When the start node equals 0",
            "When 100 moves have been recorded"
        ],
        "answer_index": 0,
        "explanation": "A meeting occurs when a state explored in the forward search intersects with a state in the backward search.",
        "difficulty": "Beginner",
        "category": "Bidirectional Search"
    },
    {
        "question": "Why is Bidirectional Search significantly faster than unidirectional BFS on deep trees?",
        "options": [
            "It searches to depth d/2 from both sides, replacing O(b^d) with O(2 * b^(d/2))",
            "It uses no memory",
            "It eliminates the branching factor",
            "It solves problems without expanding nodes"
        ],
        "answer_index": 0,
        "explanation": "Two smaller search perimeters of radius d/2 cover vastly fewer total nodes than one giant perimeter of radius d.",
        "difficulty": "Beginner",
        "category": "Bidirectional Search"
    },
    {
        "question": "What crucial requirement must be met for Bidirectional Search to be possible?",
        "options": [
            "Actions in the state space must be reversible, or backward operators must be explicitly defined",
            "The graph must have weighted edges",
            "The start state must be 0",
            "The heuristic must be Euclidean"
        ],
        "answer_index": 0,
        "explanation": "Backward search requires generating predecessors of a state, which is only possible if transitions can be reversed.",
        "difficulty": "Beginner",
        "category": "Bidirectional Search"
    },
    {
        "question": "In the 8-puzzle, can tile slides be reversed for Bidirectional Search?",
        "options": [
            "Yes, sliding tile X into the blank can always be undone by sliding tile X back into the blank",
            "No, puzzle slides are strictly one-way",
            "Only if the blank is in the center",
            "Only for tiles 1 through 4"
        ],
        "answer_index": 0,
        "explanation": "Tile sliding in the 8-puzzle is completely symmetrical and reversible, making it an ideal problem for Bidirectional Search.",
        "difficulty": "Beginner",
        "category": "Bidirectional Search"
    },
    {
        "question": "Is standard Bidirectional BFS complete and optimal for uniform step costs?",
        "options": [
            "Yes, it is both complete and optimal on uniform-cost graphs",
            "No, it is incomplete",
            "It is complete but never optimal",
            "Only if depth limit is set to 50"
        ],
        "answer_index": 0,
        "explanation": "When both directions expand level-by-level using BFS, the first valid intersection yields an optimal shortest path.",
        "difficulty": "Beginner",
        "category": "Bidirectional Search"
    },
    {
        "question": "How is the final solution path constructed in Bidirectional Search once a meeting node M is found?",
        "options": [
            "Trace forward parents from M to start, trace backward parents from M to goal, and concatenate",
            "Re-run unidirectional BFS from start to goal",
            "Reverse the entire graph",
            "Sort the meeting node's neighbors"
        ],
        "answer_index": 0,
        "explanation": "The complete path is obtained by following parent pointers from M back to the start, and from M forward to the goal.",
        "difficulty": "Beginner",
        "category": "Bidirectional Search"
    },
    {
        "question": "What are the data structures used by standard Bidirectional BFS?",
        "options": [
            "Two FIFO queues and two visited/parent dictionaries (one forward, one backward)",
            "A single stack and a single queue",
            "Three priority queues",
            "Two randomized binary search trees"
        ],
        "answer_index": 0,
        "explanation": "Each direction maintains its own FIFO queue for level-order expansion and a parent dictionary for membership checking and path reconstruction.",
        "difficulty": "Beginner",
        "category": "Bidirectional Search"
    },
    {
        "question": "If b = 10 and solution depth d = 6, BFS explores ~1,000,000 nodes. Approximately how many does Bidirectional BFS explore?",
        "options": [
            "~2,000 nodes (2 * 10^3)",
            "~500,000 nodes",
            "~100 nodes",
            "~10,000,000 nodes"
        ],
        "answer_index": 0,
        "explanation": "At d=6, d/2 = 3. 2 * b^(d/2) = 2 * 10^3 = 2,000 nodes, which is 500 times fewer expansions than unidirectional BFS.",
        "difficulty": "Beginner",
        "category": "Bidirectional Search"
    },
    {
        "question": "Can Bidirectional Search be used if the goal is not a single known state (e.g. multiple possible goal states)?",
        "options": [
            "It is much more difficult or impractical unless all goal states can be enqueued or an abstract goal state is defined",
            "Yes, it works identically without changes",
            "It runs twice as fast",
            "It requires converting the puzzle into a chess board"
        ],
        "answer_index": 0,
        "explanation": "If there are many or implicitly defined goal states, initializing the backward frontier becomes computationally difficult.",
        "difficulty": "Beginner",
        "category": "Bidirectional Search"
    },
    {
        "question": "What is the space complexity of Bidirectional BFS where b is branching factor and d is solution depth?",
        "options": [
            "O(b^(d/2))",
            "O(b^d)",
            "O(b * d)",
            "O(1)"
        ],
        "answer_index": 0,
        "explanation": "At least one of the frontiers must be kept in memory for intersection detection, requiring O(b^(d/2)) space.",
        "difficulty": "Intermediate",
        "category": "Bidirectional Search"
    },
    {
        "question": "What is the primary operational overhead in Bidirectional Search?",
        "options": [
            "Checking whether newly generated nodes exist in the opposing frontier or explored set at every step",
            "Sorting all nodes in Python lists",
            "Calculating Manhattan distance",
            "Writing to the SQLite database"
        ],
        "answer_index": 0,
        "explanation": "Intersection detection requires fast O(1) hash table lookups into the opposing direction's visited set for every generated state.",
        "difficulty": "Intermediate",
        "category": "Bidirectional Search"
    },
    {
        "question": "In Bidirectional Search, why is alternating layer-by-layer expansion (one full depth level forward, then one full level backward) common?",
        "options": [
            "It keeps the two search frontiers balanced in depth and guarantees finding the shallowest connection",
            "It prevents Python from throwing a memory error",
            "It makes edge weights disappear",
            "It allows using LIFO stacks"
        ],
        "answer_index": 0,
        "explanation": "Expanding full levels ensures that when frontiers meet, the combined path depth d_fwd + d_bwd is minimal.",
        "difficulty": "Intermediate",
        "category": "Bidirectional Search"
    },
    {
        "question": "Can Bidirectional Search be applied to directed graphs?",
        "options": [
            "Yes, provided the backward search follows incoming (reverse) directed edges",
            "No, Bidirectional Search is strictly restricted to undirected graphs",
            "Only if every node has in-degree equal to out-degree",
            "Only if the graph is fully connected"
        ],
        "answer_index": 0,
        "explanation": "In directed graphs, the backward search must traverse edges in reverse direction (from v to u along edge u->v).",
        "difficulty": "Intermediate",
        "category": "Bidirectional Search"
    },
    {
        "question": "In the 8-puzzle, if the user enters a custom goal state, how does Bidirectional Search handle it?",
        "options": [
            "It initializes the backward queue with the user's custom goal state and searches toward the initial state",
            "It ignores the custom goal and uses the default 1-8 goal",
            "It crashes because custom goals are invalid",
            "It converts the puzzle into a 15-puzzle"
        ],
        "answer_index": 0,
        "explanation": "Bidirectional search cleanly takes arbitrary start and goal states, starting one frontier at start and the other at goal.",
        "difficulty": "Intermediate",
        "category": "Bidirectional Search"
    },
    {
        "question": "What occurs if the initial and goal states belong to different unreachable parity components in the 8-puzzle?",
        "options": [
            "Both search frontiers will expand until exhausting their respective reachable components (181,440 states each) without ever meeting",
            "They will meet at state [0,1,2,3,4,5,6,7,8]",
            "The backward search will fail immediately on step 1",
            "The solver fabricates a solution path"
        ],
        "answer_index": 0,
        "explanation": "Because the two states reside in disjoint graph components, the frontiers can never intersect, correctly proving unsolvability.",
        "difficulty": "Intermediate",
        "category": "Bidirectional Search"
    },
    {
        "question": "Can Bidirectional Search use heuristics (Bidirectional A*)?",
        "options": [
            "Yes, but care must be taken so that forward and backward heuristics are consistent and guarantee optimal meeting",
            "No, heuristics are strictly forbidden in bidirectional search",
            "Only if both heuristics return 0",
            "Only on Euclidean grids"
        ],
        "answer_index": 0,
        "explanation": "Bidirectional A* uses forward heuristic h_F(n) estimating distance to goal and backward heuristic h_B(n) estimating distance to start.",
        "difficulty": "Intermediate",
        "category": "Bidirectional Search"
    },
    {
        "question": "If the forward search reaches node X with parent P_fwd, and backward search reaches node X with parent P_bwd, what is the path through X?",
        "options": [
            "Start -> ... -> P_fwd -> X -> P_bwd -> ... -> Goal",
            "Start -> Goal -> X",
            "X -> Start -> Goal",
            "P_fwd -> P_bwd -> X"
        ],
        "answer_index": 0,
        "explanation": "Node X is the bridge connecting the forward trajectory ending at X and the backward trajectory starting at X.",
        "difficulty": "Intermediate",
        "category": "Bidirectional Search"
    },
    {
        "question": "What happens if one side of a bidirectional search has a much higher branching factor than the other side (e.g. b_fwd = 2, b_bwd = 10)?",
        "options": [
            "The search can be biased to expand more steps from the side with the smaller branching factor to minimize node count",
            "The search fails to terminate",
            "Bidirectional search cannot be run",
            "The path length doubles"
        ],
        "answer_index": 0,
        "explanation": "Frontier expansion can be dynamically adjusted: expanding the smaller frontier minimizes the product of frontier sizes.",
        "difficulty": "Intermediate",
        "category": "Bidirectional Search"
    },
    {
        "question": "How does Bidirectional Search compare to standard BFS in the Algorithm Lab on the 'Hard' benchmark puzzle?",
        "options": [
            "Bidirectional BFS typically explores significantly fewer nodes than standard BFS to find the same optimal move count",
            "Bidirectional BFS explores 10 times more nodes",
            "Bidirectional BFS produces a longer path than standard BFS",
            "Bidirectional BFS runs out of depth limits"
        ],
        "answer_index": 0,
        "explanation": "Meeting in the middle at depth d/2 dramatically curtails the exponential explosion that standard BFS suffers from at depth d.",
        "difficulty": "Intermediate",
        "category": "Bidirectional Search"
    },
    {
        "question": "In Bidirectional A* (MM algorithm or NBS), why is the first meeting of frontiers NOT necessarily the optimal path when edge costs vary?",
        "options": [
            "A cheaper path connecting the two frontiers might exist through nodes not yet popped from the priority queues",
            "Because heuristics corrupt priority queues",
            "Because meeting nodes always have negative cost",
            "Because backward search inverts edge weights"
        ],
        "answer_index": 0,
        "explanation": "With non-uniform costs, an early intersection might be via a high-cost bridge; search must continue until stopping criteria prove no cheaper bridge exists.",
        "difficulty": "Advanced",
        "category": "Bidirectional Search"
    },
    {
        "question": "What is the 'fraction of state space' advantage of Bidirectional Search in a graph with diameter D?",
        "options": [
            "It covers a volume proportional to 2 * (D/2)^k rather than D^k, which is a massive geometric reduction in high-dimensional spaces",
            "It divides the graph into prime numbers",
            "It makes the diameter equal to 1",
            "It avoids touching the start node"
        ],
        "answer_index": 0,
        "explanation": "The volume of two spheres of radius r is 2 * r^k, whereas a single sphere of radius 2r is 2^k * r^k; for k >= 2 this is an exponential reduction.",
        "difficulty": "Advanced",
        "category": "Bidirectional Search"
    },
    {
        "question": "What is the 'Frontier Intersection' problem in distributed or parallel Bidirectional Search?",
        "options": [
            "Frontiers growing on separate machines must continuously cross-check membership, causing high network communication overhead",
            "Machines run out of disk space",
            "Both machines solve the same puzzle",
            "The goal state changes randomly"
        ],
        "answer_index": 0,
        "explanation": "Detecting the collision of two large sets distributed across multiple processes requires frequent synchronization or shared distributed hash tables.",
        "difficulty": "Advanced",
        "category": "Bidirectional Search"
    },
    {
        "question": "In NBS (Near-Optimal Bidirectional Search), what priority criterion is used to select whether to expand forward or backward?",
        "options": [
            "Expand the direction with the minimum lower bound on the solution cost passing through that frontier",
            "Always expand forward only",
            "Alternate strictly based on CPU clock ticks",
            "Pick randomly based on a coin flip"
        ],
        "answer_index": 0,
        "explanation": "NBS balances expansions by choosing the frontier node that minimizes the lower bound on total cost, proving optimal stopping with minimal nodes.",
        "difficulty": "Advanced",
        "category": "Bidirectional Search"
    },
    {
        "question": "Why is Bidirectional Search particularly well-suited for solving the 15-puzzle and 24-puzzle when combined with pattern databases?",
        "options": [
            "Pattern databases can evaluate distances from both start and goal, allowing deep searches to meet at intermediate configurations efficiently",
            "Because 15 is divisible by 3",
            "Because 24-puzzles have 0 inversions",
            "Because it avoids loading pattern databases into RAM"
        ],
        "answer_index": 0,
        "explanation": "Large sliding tile puzzles have immense depths (God's number for 15-puzzle is 80); bidirectional search cuts required search depth from 80 to 40.",
        "difficulty": "Advanced",
        "category": "Bidirectional Search"
    },
    {
        "question": "If backward search generates a state that was already expanded in the forward search, what is the maximum remaining work needed to form the solution?",
        "options": [
            "Zero search expansions: the path can be immediately reconstructed via parent pointers in O(d) time",
            "O(b^d) additional expansions",
            "Re-running the entire forward search",
            "Solving the puzzle again from scratch"
        ],
        "answer_index": 0,
        "explanation": "Once an intersection is detected, parent pointers in both directions connect start to goal, requiring only a linear traversal to assemble the path.",
        "difficulty": "Advanced",
        "category": "Bidirectional Search"
    },
    {
        "question": "Can Bidirectional Search handle graphs with cycles without an explored set?",
        "options": [
            "No, without cycle detection both the forward and backward searches will get trapped in cycles and fail to terminate",
            "Yes, because two cycles cancel each other out",
            "Yes, if edge costs are integers",
            "Only on trees with branching factor 2"
        ],
        "answer_index": 0,
        "explanation": "Both frontiers are subject to cycle traps; closed sets (or visited hash sets) are mandatory for completeness in cyclic graphs.",
        "difficulty": "Advanced",
        "category": "Bidirectional Search"
    },
    {
        "question": "What is the perimeter search variation of Bidirectional Search?",
        "options": [
            "A small breadth-first perimeter is expanded around the goal once; then forward heuristic search uses distance to the perimeter as h(n)",
            "Searching only along the perimeter of the 3x3 board",
            "Searching around the edges of the screen",
            "A search that never expands interior graph nodes"
        ],
        "answer_index": 0,
        "explanation": "Perimeter search avoids maintaining two active dynamic frontiers by pre-building a fixed goal perimeter that enhances forward heuristic accuracy.",
        "difficulty": "Advanced",
        "category": "Bidirectional Search"
    },
    {
        "question": "Under what scenario does Bidirectional Search perform WORSE than unidirectional BFS?",
        "options": [
            "When the goal has an extremely high branching factor or represents a diffuse set of states, making backward expansion blow up immediately",
            "When the start and goal states are identical",
            "When edge costs are all 1",
            "When the graph has no cycles"
        ],
        "answer_index": 0,
        "explanation": "If the goal has thousands of predecessors, the backward frontier explodes on step 1, whereas forward search might have had a small branching factor.",
        "difficulty": "Advanced",
        "category": "Bidirectional Search"
    },
    {
        "question": "In the 8-puzzle implementation of this project, how does Bidirectional Search verify that a meeting node is legal?",
        "options": [
            "The meeting state is an exact match of the 9-tuple of tiles between forward and backward parent maps",
            "It checks if the meeting state has 0 moves",
            "It validates that tile 0 is in the upper-left corner",
            "It verifies that execution time is under 1 second"
        ],
        "answer_index": 0,
        "explanation": "States are stored as immutable 9-tuples; an intersection is confirmed when `tuple(neighbor) in backward_parent` evaluates to True.",
        "difficulty": "Advanced",
        "category": "Bidirectional Search"
    },
    {
        "question": "What is the node selection criterion for Uniform Cost Search (UCS)?",
        "options": [
            "Lowest cumulative path cost g(n) from the start node",
            "Lowest heuristic estimate h(n)",
            "Highest depth level in the tree",
            "Fewest number of edges regardless of weight"
        ],
        "answer_index": 0,
        "explanation": "UCS always expands the node with the lowest path cost g(n) accumulated from the start node.",
        "difficulty": "Beginner",
        "category": "Uniform Cost Search"
    },
    {
        "question": "Which famous algorithm is Uniform Cost Search essentially identical to in graph theory?",
        "options": [
            "Dijkstra's Algorithm",
            "Kruskal's Algorithm",
            "Prim's Algorithm",
            "Floyd-Warshall Algorithm"
        ],
        "answer_index": 0,
        "explanation": "UCS is Dijkstra's algorithm applied to searching for a specific goal state on an implicit or explicit state graph.",
        "difficulty": "Beginner",
        "category": "Uniform Cost Search"
    },
    {
        "question": "Which data structure is used to implement the frontier in Uniform Cost Search?",
        "options": [
            "Priority Queue (Min-Heap)",
            "FIFO Queue",
            "LIFO Stack",
            "Doubly Linked List"
        ],
        "answer_index": 0,
        "explanation": "A min-heap priority queue ordered by g(n) enables efficient retrieval of the lowest-cost node.",
        "difficulty": "Beginner",
        "category": "Uniform Cost Search"
    },
    {
        "question": "Is Uniform Cost Search an informed or uninformed search algorithm?",
        "options": [
            "Uninformed (Blind)",
            "Informed (Heuristic)",
            "Adversarial",
            "Genetic"
        ],
        "answer_index": 0,
        "explanation": "UCS uses only the true path cost g(n) without any heuristic estimate of the remaining distance to the goal.",
        "difficulty": "Beginner",
        "category": "Uniform Cost Search"
    },
    {
        "question": "When edge weights in a graph vary (e.g. costs of 2, 5, 10), is UCS guaranteed to find the minimum-cost path?",
        "options": [
            "Yes, provided all edge costs are non-negative (>= 0)",
            "No, UCS only minimizes the number of edges",
            "Only if the graph is a tree",
            "Only if an admissible heuristic is provided"
        ],
        "answer_index": 0,
        "explanation": "UCS guarantees optimality for any graph with non-negative edge costs by expanding paths in order of increasing total cost.",
        "difficulty": "Beginner",
        "category": "Uniform Cost Search"
    },
    {
        "question": "If all step costs in a graph are identical positive constants (e.g. cost = 1 everywhere), UCS behaves identically to:",
        "options": [
            "Breadth-First Search (BFS)",
            "Depth-First Search (DFS)",
            "Greedy Best-First Search",
            "Depth-Limited Search"
        ],
        "answer_index": 0,
        "explanation": "When all step costs equal 1, path cost g(n) equals node depth, so expanding by minimum g(n) is identical to FIFO BFS.",
        "difficulty": "Beginner",
        "category": "Uniform Cost Search"
    },
    {
        "question": "When is the goal test applied in Uniform Cost Search to guarantee optimality?",
        "options": [
            "When a node is popped from the priority queue for expansion",
            "As soon as a node is generated and pushed to the queue",
            "When the queue is empty",
            "Only at depth 0"
        ],
        "answer_index": 0,
        "explanation": "A cheaper path to the goal might still reside in the priority queue; testing upon popping guarantees no cheaper path exists.",
        "difficulty": "Beginner",
        "category": "Uniform Cost Search"
    },
    {
        "question": "What does g(n) represent in Uniform Cost Search?",
        "options": [
            "The total cost of the path from the start node to node n",
            "The estimated cost from n to the goal",
            "The number of tiles in the wrong position",
            "The priority queue capacity"
        ],
        "answer_index": 0,
        "explanation": "g(n) is the sum of all individual transition edge costs along the path from the start node to n.",
        "difficulty": "Beginner",
        "category": "Uniform Cost Search"
    },
    {
        "question": "In the 8-puzzle, why does UCS produce the exact same move count as BFS?",
        "options": [
            "Because every valid tile slide has an identical cost of 1 move",
            "Because UCS uses Manhattan distance",
            "Because the 8-puzzle has 9 tiles",
            "Because UCS is a depth-first search"
        ],
        "answer_index": 0,
        "explanation": "With uniform step costs of 1, path cost g(n) is exactly equal to move count, making UCS exploration order match BFS.",
        "difficulty": "Beginner",
        "category": "Uniform Cost Search"
    },
    {
        "question": "What happens if an edge cost in a graph search problem is zero (cost = 0)?",
        "options": [
            "UCS can still find optimal paths, but zero-cost cycles can cause infinite loops unless handled",
            "UCS immediately crashes with division by zero",
            "Zero costs are automatically converted to 1",
            "The search becomes Greedy Search"
        ],
        "answer_index": 0,
        "explanation": "Zero-cost edges do not increase g(n); if a directed cycle has cost 0, the search could cycle infinitely without advancing g.",
        "difficulty": "Beginner",
        "category": "Uniform Cost Search"
    },
    {
        "question": "What is the time and space complexity of Uniform Cost Search in terms of optimal cost C* and minimum step cost epsilon > 0?",
        "options": [
            "O(b^(1 + floor(C* / epsilon)))",
            "O(b * d)",
            "O(C* * epsilon)",
            "O(1)"
        ],
        "answer_index": 0,
        "explanation": "In the worst case, UCS expands all nodes whose cost is <= C*. With minimum edge cost epsilon, the effective depth can be C*/epsilon.",
        "difficulty": "Intermediate",
        "category": "Uniform Cost Search"
    },
    {
        "question": "Why must all step costs be strictly positive (cost >= epsilon > 0) for UCS to be complete in infinite state spaces?",
        "options": [
            "To prevent infinite sequences of zero-cost or infinitesimally small steps from stalling progress toward the goal",
            "Because negative numbers cannot be stored in heaps",
            "Because priority queues require integer keys",
            "To ensure the graph remains planar"
        ],
        "answer_index": 0,
        "explanation": "If step costs can be arbitrarily small (e.g. 1/2, 1/4, 1/8...), an infinite path could exist whose total cost is bounded below C*, trapping UCS.",
        "difficulty": "Intermediate",
        "category": "Uniform Cost Search"
    },
    {
        "question": "How does UCS handle the case where a newly generated path to an already-visited node has a lower g(n) cost than the previous path?",
        "options": [
            "It updates the node's cost in cost_so_far and inserts the lower-cost state into the priority queue",
            "It ignores the new path and keeps the old one",
            "It resets the entire search",
            "It deletes the node from the graph"
        ],
        "answer_index": 0,
        "explanation": "If a cheaper path to an existing state is discovered, the cost must be decreased in the frontier to preserve optimality.",
        "difficulty": "Intermediate",
        "category": "Uniform Cost Search"
    },
    {
        "question": "What is the relationship between Uniform Cost Search and A* Search?",
        "options": [
            "UCS is A* Search with the heuristic function h(n) = 0 for all nodes",
            "UCS is A* Search with g(n) = 0",
            "A* is UCS with a LIFO stack",
            "They are completely incompatible algorithms"
        ],
        "answer_index": 0,
        "explanation": "A* evaluates f(n) = g(n) + h(n). Setting h(n) = 0 yields f(n) = g(n), which is precisely Uniform Cost Search.",
        "difficulty": "Intermediate",
        "category": "Uniform Cost Search"
    },
    {
        "question": "Why is UCS slower than A* on large pathfinding graphs?",
        "options": [
            "UCS explores symmetrically in all directions (concentric circles of cost) rather than focusing toward the goal",
            "UCS uses an inefficient sorting algorithm",
            "UCS cannot handle directed edges",
            "UCS calculates Manhattan distances slowly"
        ],
        "answer_index": 0,
        "explanation": "Without heuristic guidance, UCS expands nodes in every direction regardless of whether they lead toward or away from the goal.",
        "difficulty": "Intermediate",
        "category": "Uniform Cost Search"
    },
    {
        "question": "Suppose the start node connects to Node A (cost 10) and Node B (cost 1). Node B connects to Node C (cost 2). Which node does UCS expand next after start?",
        "options": [
            "Node B (g = 1)",
            "Node A (g = 10)",
            "Node C",
            "The goal node"
        ],
        "answer_index": 0,
        "explanation": "UCS pops the frontier node with minimum g. Since g(B)=1 < g(A)=10, Node B is expanded first.",
        "difficulty": "Intermediate",
        "category": "Uniform Cost Search"
    },
    {
        "question": "In the Graph Search Solver of this website, if edge weights represent travel time in minutes, which algorithm guarantees the fastest route?",
        "options": [
            "Uniform Cost Search (or A* with an admissible heuristic)",
            "Breadth-First Search (BFS)",
            "Depth-First Search (DFS)",
            "Depth-Limited Search (DLS)"
        ],
        "answer_index": 0,
        "explanation": "BFS minimizes edge count, which could be a slow multi-hour flight; UCS minimizes sum of edge weights (total travel time).",
        "difficulty": "Intermediate",
        "category": "Uniform Cost Search"
    },
    {
        "question": "What is the consequence of applying the goal test at node generation in Uniform Cost Search?",
        "options": [
            "It may return a suboptimal path because a cheaper path to the goal might still be waiting in the queue",
            "It improves search speed with zero downside",
            "It causes a fatal Python error",
            "It converts UCS into DFS"
        ],
        "answer_index": 0,
        "explanation": "An unexpanded path in the queue might reach the goal with a lower total cost than the path that happened to generate the goal first.",
        "difficulty": "Intermediate",
        "category": "Uniform Cost Search"
    },
    {
        "question": "What happens if UCS is executed on a graph with negative edge costs?",
        "options": [
            "It may fail to find the optimal path or loop infinitely in negative-cost cycles",
            "It automatically uses the Bellman-Ford equation",
            "Negative edge costs are ignored",
            "It runs normally without any issues"
        ],
        "answer_index": 0,
        "explanation": "Negative edges break the invariant that path costs increase monotonically along paths; Bellman-Ford is needed for negative weights.",
        "difficulty": "Intermediate",
        "category": "Uniform Cost Search"
    },
    {
        "question": "In Python's `heapq` module, how is UCS implemented to handle ties when two nodes have identical path costs g?",
        "options": [
            "By storing tuples (g, counter, state), where counter is an incrementing integer tie-breaker",
            "By comparing the states directly with < operator",
            "By raising an error",
            "By deleting the second state"
        ],
        "answer_index": 0,
        "explanation": "If states cannot be compared with `<` (e.g. complex objects), a unique integer counter prevents comparison errors in the heap.",
        "difficulty": "Intermediate",
        "category": "Uniform Cost Search"
    },
    {
        "question": "Why does UCS expand all nodes with g(n) < C*, and only SOME nodes with g(n) = C*?",
        "options": [
            "Any node strictly cheaper than the optimal goal must be explored; once a goal node with g = C* is popped, search halts immediately",
            "Nodes with g < C* are ignored",
            "Because C* is prime",
            "Because goal nodes have g = 0"
        ],
        "answer_index": 0,
        "explanation": "Every node with g < C* could potentially lead to a goal cheaper than C*; as soon as a goal with g = C* is popped, no remaining node can beat it.",
        "difficulty": "Advanced",
        "category": "Uniform Cost Search"
    },
    {
        "question": "In a road network where graph edges are planar and costs represent Euclidean distance, what is the geometric shape of the UCS exploration frontier?",
        "options": [
            "A circle (or disc) expanding outward uniformly from the start node",
            "An ellipse oriented toward the goal",
            "A straight line directly to the goal",
            "A square with side length C*"
        ],
        "answer_index": 0,
        "explanation": "Because UCS expands in increasing order of cost in all directions, its wavefront forms concentric circles centered at the start.",
        "difficulty": "Advanced",
        "category": "Uniform Cost Search"
    },
    {
        "question": "How does the time complexity of UCS compare between using a binary min-heap versus a Fibonacci heap for V vertices and E edges?",
        "options": [
            "Binary heap runs in O((V + E) log V); Fibonacci heap runs in O(E + V log V)",
            "Binary heap is O(V^2); Fibonacci heap is O(E^2)",
            "Both are strictly O(V * E)",
            "Fibonacci heap is slower in theory"
        ],
        "answer_index": 0,
        "explanation": "Fibonacci heaps support O(1) amortized `decrease-key` operations, improving the O(E log V) heap update step to O(E).",
        "difficulty": "Advanced",
        "category": "Uniform Cost Search"
    },
    {
        "question": "Can Uniform Cost Search be used with multiple start nodes (multi-source shortest path)?",
        "options": [
            "Yes, by pushing all start nodes into the priority queue with initial cost g = 0",
            "No, UCS can only have a single start node",
            "Only if all start nodes have edges between them",
            "Only on directed acyclic graphs"
        ],
        "answer_index": 0,
        "explanation": "Initializing the min-heap with multiple nodes at cost 0 finds the shortest path from ANY of the source nodes to the goal.",
        "difficulty": "Advanced",
        "category": "Uniform Cost Search"
    },
    {
        "question": "In a state space where C* = 100 and epsilon = 0.01, what is the maximum depth that UCS might explore?",
        "options": [
            "Depth up to 10,000 (100 / 0.01)",
            "Depth 100",
            "Depth 10",
            "Depth 1,000,000"
        ],
        "answer_index": 0,
        "explanation": "If the graph contains paths of many tiny steps of size 0.01, UCS can descend 10,000 levels before reaching cost 100.",
        "difficulty": "Advanced",
        "category": "Uniform Cost Search"
    },
    {
        "question": "How does bidirectional Uniform Cost Search maintain optimality?",
        "options": [
            "It tracks the cheapest connection found between forward and backward frontiers and terminates when g_fwd(min) + g_bwd(min) >= best_cost",
            "It halts the instant the two frontiers touch",
            "It runs forward UCS to completion, then backward UCS",
            "It multiplies forward and backward costs"
        ],
        "answer_index": 0,
        "explanation": "Stopping immediately upon first touch could miss a cheaper path; search can only stop when the sum of minimum frontier keys exceeds the best path seen.",
        "difficulty": "Advanced",
        "category": "Uniform Cost Search"
    },
    {
        "question": "If all edge weights in a graph are positive integers bounded by a small constant K (e.g. edge costs 1 to 5), what data structure optimizes UCS to O(E + V)?",
        "options": [
            "Dial's algorithm (using circular buckets of size K + 1)",
            "A balanced Red-Black tree",
            "A standard LIFO stack",
            "A SQLite database index"
        ],
        "answer_index": 0,
        "explanation": "Dial's algorithm uses an array of buckets for each integer cost modulo (K+1), allowing O(1) insertion and extraction.",
        "difficulty": "Advanced",
        "category": "Uniform Cost Search"
    },
    {
        "question": "What is the difference between Dijkstra's algorithm standard textbook formulation and UCS in artificial intelligence?",
        "options": [
            "Dijkstra typically finds shortest paths to ALL vertices in a graph; UCS stops as soon as the specific GOAL node is popped",
            "Dijkstra uses heuristics while UCS does not",
            "Dijkstra only works on trees while UCS works on graphs",
            "UCS requires negative edge weights"
        ],
        "answer_index": 0,
        "explanation": "In AI, state spaces are often infinite or generated on the fly; UCS terminates as soon as the target goal is dequeued.",
        "difficulty": "Advanced",
        "category": "Uniform Cost Search"
    },
    {
        "question": "What happens if an edge cost in a graph search problem is updated dynamically during search?",
        "options": [
            "If edge costs decrease, affected frontier nodes must have their priorities decreased (decrease-key)",
            "The search must be aborted and restarted",
            "The priority queue automatically updates all nodes in O(1)",
            "The algorithm switches to DFS"
        ],
        "answer_index": 0,
        "explanation": "Dynamic cost reductions require updating cost_so_far and re-adjusting heap positions to preserve the priority queue invariant.",
        "difficulty": "Advanced",
        "category": "Uniform Cost Search"
    },
    {
        "question": "In a graph where edge costs are probabilities of survival p in (0, 1] and we seek the path of maximum survival, how can UCS be applied?",
        "options": [
            "Transform edge costs to -log(p) >= 0; minimizing the sum of -log(p) maximizes the product of probabilities",
            "Use probabilities directly as edge costs",
            "Divide probabilities by branching factor",
            "UCS cannot be used for probability problems"
        ],
        "answer_index": 0,
        "explanation": "Since log(a * b) = log(a) + log(b) and -log(p) >= 0 for p in (0, 1], minimizing sum of -log(p) converts multiplication into non-negative addition.",
        "difficulty": "Advanced",
        "category": "Uniform Cost Search"
    },
    {
        "question": "What is Depth-Limited Search (DLS)?",
        "options": [
            "Depth-First Search with a predetermined maximum depth limit L beyond which nodes are not expanded",
            "A search that only explores nodes with low heuristics",
            "A search that runs to infinity",
            "BFS with a limit on memory"
        ],
        "answer_index": 0,
        "explanation": "DLS restricts standard DFS by imposing a cutoff depth L; any node at depth L is treated as having no successors.",
        "difficulty": "Beginner",
        "category": "Depth-Limited Search"
    },
    {
        "question": "Why is a depth limit introduced into Depth-First Search?",
        "options": [
            "To prevent DFS from getting trapped in infinite paths or excessively deep branches",
            "To make DFS find the optimal path",
            "To reduce the branching factor to 1",
            "To allow DLS to calculate Manhattan distances"
        ],
        "answer_index": 0,
        "explanation": "Without a depth limit, DFS can follow an infinite path indefinitely. Imposing limit L guarantees termination.",
        "difficulty": "Beginner",
        "category": "Depth-Limited Search"
    },
    {
        "question": "What happens if the solution depth d is strictly greater than the chosen depth limit L (d > L)?",
        "options": [
            "DLS fails to find the solution, reporting cutoff failure",
            "DLS automatically increases the limit",
            "DLS jumps straight to the goal",
            "DLS raises a memory error"
        ],
        "answer_index": 0,
        "explanation": "If the goal lies deeper than L, DLS will never reach depth d, making DLS incomplete when d > L.",
        "difficulty": "Beginner",
        "category": "Depth-Limited Search"
    },
    {
        "question": "What is the space complexity of Depth-Limited Search with depth limit L and branching factor b?",
        "options": [
            "O(b * L)",
            "O(b^L)",
            "O(L^b)",
            "O(1)"
        ],
        "answer_index": 0,
        "explanation": "Like DFS, DLS stores only the active path of length at most L plus sibling nodes, giving linear O(b * L) space.",
        "difficulty": "Beginner",
        "category": "Depth-Limited Search"
    },
    {
        "question": "Is Depth-Limited Search guaranteed to find the shortest (optimal) path to a goal?",
        "options": [
            "No, it returns the first path found within the limit L, which may not be optimal",
            "Yes, it is always optimal",
            "Yes, provided L is prime",
            "Only if the limit L is 1"
        ],
        "answer_index": 0,
        "explanation": "DLS explores in depth-first order; it returns whatever valid path reaches a goal first within depth L, regardless of length.",
        "difficulty": "Beginner",
        "category": "Depth-Limited Search"
    },
    {
        "question": "What are the three possible return outcomes of a Depth-Limited Search?",
        "options": [
            "Solution found, Cutoff (reached depth limit without finding goal), Failure (entire state space explored without finding goal)",
            "Success, Crash, Hang",
            "True, False, None",
            "Goal, Root, Leaf"
        ],
        "answer_index": 0,
        "explanation": "DLS distinguishes between a complete failure (no solution exists anywhere) and a cutoff (a solution might exist beyond depth L).",
        "difficulty": "Beginner",
        "category": "Depth-Limited Search"
    },
    {
        "question": "In the 8-puzzle solver of this project, what is the default depth limit used for Depth-Limited Search?",
        "options": [
            "30 moves",
            "2 moves",
            "1000 moves",
            "181,440 moves"
        ],
        "answer_index": 0,
        "explanation": "A depth cap of 30 covers almost all solvable 8-puzzles (since God's Number is 31) while preventing deep runaways.",
        "difficulty": "Beginner",
        "category": "Depth-Limited Search"
    },
    {
        "question": "Is Depth-Limited Search an informed or uninformed search algorithm?",
        "options": [
            "Uninformed (Blind)",
            "Informed (Heuristic)",
            "Metaheuristic",
            "Genetic"
        ],
        "answer_index": 0,
        "explanation": "DLS does not use any heuristic evaluation function to guide its choices; it is a blind search method.",
        "difficulty": "Beginner",
        "category": "Depth-Limited Search"
    },
    {
        "question": "What data structure is used to implement Depth-Limited Search?",
        "options": [
            "LIFO Stack (or recursive function calls)",
            "FIFO Queue",
            "Priority Queue",
            "B-Tree"
        ],
        "answer_index": 0,
        "explanation": "DLS is implemented using recursion or an explicit LIFO stack tracking the current depth of each node.",
        "difficulty": "Beginner",
        "category": "Depth-Limited Search"
    },
    {
        "question": "What happens when the depth limit L is set to 0 in DLS?",
        "options": [
            "Only the initial (start) node is checked; if start != goal, it reports cutoff",
            "DLS explores the entire tree",
            "DLS crashes",
            "DLS sets L = 10 automatically"
        ],
        "answer_index": 0,
        "explanation": "At L=0, no successors of the root can be generated; DLS simply checks if the root itself is the goal.",
        "difficulty": "Beginner",
        "category": "Depth-Limited Search"
    },
    {
        "question": "What is the time complexity of Depth-Limited Search in terms of branching factor b and limit L?",
        "options": [
            "O(b^L)",
            "O(b * L)",
            "O(L^2)",
            "O(log(b^L))"
        ],
        "answer_index": 0,
        "explanation": "In the worst case, DLS expands all nodes down to depth L, visiting 1 + b + b^2 + ... + b^L = O(b^L) nodes.",
        "difficulty": "Intermediate",
        "category": "Depth-Limited Search"
    },
    {
        "question": "How does DLS handle the problem of infinite loops in cyclic graphs?",
        "options": [
            "Any path that repeats states can only loop up to depth L before being cut off",
            "It automatically detects cycles in O(1) time",
            "It uses a priority queue to sort cycles",
            "It deletes cycles from the graph"
        ],
        "answer_index": 0,
        "explanation": "Even without an explicit visited set, a depth limit caps any recursive cycle at depth L, preventing infinite execution.",
        "difficulty": "Intermediate",
        "category": "Depth-Limited Search"
    },
    {
        "question": "What is the primary challenge in using Depth-Limited Search in practice?",
        "options": [
            "Choosing a good depth limit L: if L is too small, no solution is found; if L is too large, search time explodes",
            "DLS uses too much memory",
            "DLS cannot be run in Python",
            "DLS only works on trees with branching factor 2"
        ],
        "answer_index": 0,
        "explanation": "Selecting L requires problem knowledge; an underestimate fails, while an overestimate can cause massive unneeded search.",
        "difficulty": "Intermediate",
        "category": "Depth-Limited Search"
    },
    {
        "question": "In a map of Romania with 20 cities, what is a natural depth limit L for finding a path between any two cities?",
        "options": [
            "L = 19 (the maximum number of edges in a simple path between 20 cities)",
            "L = 1",
            "L = 100",
            "L = 20!"
        ],
        "answer_index": 0,
        "explanation": "A simple path in a graph of |V| vertices can contain at most |V| - 1 edges; setting L = 19 guarantees completeness.",
        "difficulty": "Intermediate",
        "category": "Depth-Limited Search"
    },
    {
        "question": "If a goal state exists at depth 5 and depth 15, and DLS is executed with L = 10, which goal can DLS find?",
        "options": [
            "It can find the goal at depth 5, but will never reach the goal at depth 15",
            "It finds the goal at depth 15",
            "It finds both goals simultaneously",
            "It reports cutoff failure"
        ],
        "answer_index": 0,
        "explanation": "Because L = 10, nodes beyond depth 10 are pruned; the goal at depth 5 is within the search envelope and can be found.",
        "difficulty": "Intermediate",
        "category": "Depth-Limited Search"
    },
    {
        "question": "How is the current depth tracked in recursive Depth-Limited Search?",
        "options": [
            "By passing a remaining depth integer that decrements with each recursive call: dls(node, limit - 1)",
            "By checking the system clock",
            "By counting the number of characters in the state name",
            "By reading a global variable"
        ],
        "answer_index": 0,
        "explanation": "Recursion naturally tracks depth by decrementing the remaining limit; when limit == 0, child generation is halted.",
        "difficulty": "Intermediate",
        "category": "Depth-Limited Search"
    },
    {
        "question": "Why is DLS complete when the diameter of the state space graph is known and we set L = diameter?",
        "options": [
            "Because any shortest path between any two states cannot exceed the graph diameter",
            "Because diameter equals branching factor",
            "Because all graphs are planar",
            "Because diameter eliminates cycles"
        ],
        "answer_index": 0,
        "explanation": "The diameter is the maximum shortest path between any two vertices; setting L = diameter ensures all reachable goals are covered.",
        "difficulty": "Intermediate",
        "category": "Depth-Limited Search"
    },
    {
        "question": "What is the difference between DLS returning `None` due to 'Cutoff' versus 'Failure'?",
        "options": [
            "'Cutoff' means at least one path hit depth limit L; 'Failure' means the entire tree within depth L was exhausted with no cutoffs",
            "They mean the exact same thing",
            "'Failure' means the computer crashed",
            "'Cutoff' means a solution was found"
        ],
        "answer_index": 0,
        "explanation": "If no nodes were cut off at depth L and no goal was found, the finite graph has no solution; if cutoffs occurred, a solution might lie deeper.",
        "difficulty": "Intermediate",
        "category": "Depth-Limited Search"
    },
    {
        "question": "In the Graph Search Solver of this application, what parameter can the user configure when selecting Depth-Limited Search?",
        "options": [
            "The Depth Limit slider (L)",
            "The Heuristic function",
            "The edge cost multiplier",
            "The database username"
        ],
        "answer_index": 0,
        "explanation": "The application provides a slider allowing students to experiment with different depth cutoffs L (e.g. 1 to 50).",
        "difficulty": "Intermediate",
        "category": "Depth-Limited Search"
    },
    {
        "question": "If DLS is executed with L = 5 on a graph where the goal is at depth 8, what does the solver output?",
        "options": [
            "A clear error message stating that no path was found within depth limit 5, advising to increase the limit",
            "A false solution with 5 moves",
            "The solver hangs indefinitely",
            "A solution to a different goal"
        ],
        "answer_index": 0,
        "explanation": "The application handles cutoff gracefully, explaining why the search terminated and prompting the user to raise L.",
        "difficulty": "Intermediate",
        "category": "Depth-Limited Search"
    },
    {
        "question": "How does Depth-Limited Search serve as the core building block for Iterative Deepening DFS (IDDFS)?",
        "options": [
            "IDDFS simply calls DLS repeatedly in an outer loop with limits L = 0, 1, 2, 3, ... until a solution is found",
            "IDDFS runs DLS backwards",
            "IDDFS runs DLS on separate CPU threads",
            "IDDFS converts DLS into A*"
        ],
        "answer_index": 0,
        "explanation": "IDDFS leverages DLS as a subroutine, progressively relaxing the depth limit until the shallowest goal is encountered.",
        "difficulty": "Advanced",
        "category": "Depth-Limited Search"
    },
    {
        "question": "In a tree with branching factor b = 3 and limit L = 10, how many total nodes can DLS expand in the worst case?",
        "options": [
            "(3^11 - 1) / 2 = 88,573 nodes",
            "30 nodes",
            "3,000 nodes",
            "1,000,000 nodes"
        ],
        "answer_index": 0,
        "explanation": "Summing the geometric series from depth 0 to 10 for b=3 gives (3^11 - 1) / (3 - 1) = 88,573 nodes.",
        "difficulty": "Advanced",
        "category": "Depth-Limited Search"
    },
    {
        "question": "What is the memory footprint of DLS compared to BFS at depth L = 20 with b = 4 and 100 bytes per node?",
        "options": [
            "DLS uses ~8 KB (b * L * 100 bytes); BFS would require ~100 Terabytes (4^20 * 100 bytes)",
            "Both use ~8 KB",
            "DLS uses 100 Terabytes",
            "BFS uses 8 KB"
        ],
        "answer_index": 0,
        "explanation": "DLS needs only O(b * L) = 4 * 20 * 100 bytes = 8 KB; BFS needs O(b^L) = 4^20 = 10^12 nodes * 100 bytes = 100 TB.",
        "difficulty": "Advanced",
        "category": "Depth-Limited Search"
    },
    {
        "question": "If cycle detection is added to DLS, does it check cycles globally or along the current branch?",
        "options": [
            "Branch checking (ancestor set) preserves O(L) space; global closed set requires O(V) space",
            "Both require O(1) space",
            "Branch checking requires exponential space",
            "Global checking requires zero memory"
        ],
        "answer_index": 0,
        "explanation": "Tracking visited nodes strictly along the active recursion branch keeps memory linear with depth L.",
        "difficulty": "Advanced",
        "category": "Depth-Limited Search"
    },
    {
        "question": "In the 8-puzzle, why would setting depth limit L = 25 be insufficient for arbitrary solvable configurations?",
        "options": [
            "Because some 8-puzzle configurations require up to 31 moves (God's Number for 8-puzzle is 31)",
            "Because 25 is not divisible by 3",
            "Because 8-puzzle solutions must have an even number of moves",
            "Because all 8-puzzles require at least 32 moves"
        ],
        "answer_index": 0,
        "explanation": "A subset of solvable 8-puzzle configurations have shortest solution paths of 26 to 31 moves; a cap of 25 would fail on them.",
        "difficulty": "Advanced",
        "category": "Depth-Limited Search"
    },
    {
        "question": "Can DLS be implemented non-recursively using an explicit stack while retaining depth tracking?",
        "options": [
            "Yes, by storing tuples of (node, path, current_depth) on the stack and only expanding if current_depth < L",
            "No, depth tracking is mathematically impossible with stacks",
            "Only if edge costs are powers of 2",
            "Only in assembly language"
        ],
        "answer_index": 0,
        "explanation": "Storing the current depth along with each node reference allows an iterative while-loop to enforce the depth cutoff.",
        "difficulty": "Advanced",
        "category": "Depth-Limited Search"
    },
    {
        "question": "What is the effect of setting a depth limit L that is excessively large (e.g. L = 1,000,000) on a graph with cycles?",
        "options": [
            "DLS will effectively behave like unconstrained DFS, diving into gigantic cycle paths and practically hanging",
            "It runs as fast as BFS",
            "It converts into A*",
            "It guarantees O(1) run time"
        ],
        "answer_index": 0,
        "explanation": "If L is far larger than necessary, DLS wanders through hundreds of thousands of redundant cycle iterations before backtracking.",
        "difficulty": "Advanced",
        "category": "Depth-Limited Search"
    },
    {
        "question": "How does Depth-Limited Search interact with weighted edges?",
        "options": [
            "DLS completely ignores edge weights, counting only the number of edge transitions (depth)",
            "DLS automatically sums edge weights and cuts off when cost exceeds L",
            "DLS divides edge weights by L",
            "DLS fails on weighted edges"
        ],
        "answer_index": 0,
        "explanation": "DLS is depth-bounded, not cost-bounded. Bounding by path cost g(n) instead of depth produces Uniform Cost / Branch-and-Bound search.",
        "difficulty": "Advanced",
        "category": "Depth-Limited Search"
    },
    {
        "question": "If a graph has multiple connected components and the goal is in a different component from the start, what does DLS return?",
        "options": [
            "Failure (not Cutoff), because the entire reachable component is explored without any paths exceeding depth L",
            "Cutoff",
            "Optimal path",
            "Infinite loop"
        ],
        "answer_index": 0,
        "explanation": "If all reachable paths terminate naturally (dead ends) before reaching depth L without finding the goal, DLS conclusively reports Failure.",
        "difficulty": "Advanced",
        "category": "Depth-Limited Search"
    },
    {
        "question": "Under what condition does DLS guarantee finding an optimal solution?",
        "options": [
            "When the optimal solution depth d <= L, and the goal happens to be the very first leaf explored at depth d",
            "Whenever L is an odd number",
            "Whenever the graph is directed",
            "Never under any circumstances"
        ],
        "answer_index": 0,
        "explanation": "If the first descent happens to hit an optimal goal, DLS returns it, but this is fortuitous rather than a systematic guarantee.",
        "difficulty": "Advanced",
        "category": "Depth-Limited Search"
    },
    {
        "question": "How does Iterative Deepening Depth-First Search (IDDFS) operate?",
        "options": [
            "It repeatedly runs Depth-Limited Search, gradually increasing the depth limit (0, 1, 2, ...) until the goal is found",
            "It runs BFS and DFS at the same time",
            "It doubles the number of nodes at each step",
            "It searches from the deepest nodes up to the root"
        ],
        "answer_index": 0,
        "explanation": "IDDFS combines depth-limited searches in an outer loop with limits L = 0, 1, 2, ... until a solution is encountered.",
        "difficulty": "Beginner",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "What is the major memory advantage of IDDFS?",
        "options": [
            "It achieves BFS-level completeness and optimality while using only linear DFS memory: O(b * d)",
            "It uses zero bytes of memory",
            "It compresses states into 1 bit",
            "It stores all states in the database"
        ],
        "answer_index": 0,
        "explanation": "Because each iteration is a depth-first search, IDDFS only needs to store the current path of length d, requiring O(b * d) space.",
        "difficulty": "Beginner",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "Is IDDFS guaranteed to find the shortest (optimal) path in a uniform-cost search tree?",
        "options": [
            "Yes, because it tests depth limits in increasing order and stops at the very first depth containing a goal",
            "No, IDDFS is never optimal",
            "Only if Manhattan distance is enabled",
            "Only on trees with branching factor 1"
        ],
        "answer_index": 0,
        "explanation": "Since depth limit L increases by 1 each round, the first solution discovered must be at the minimal possible depth d.",
        "difficulty": "Beginner",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "Is IDDFS an informed or uninformed search algorithm?",
        "options": [
            "Uninformed (Blind)",
            "Informed (Heuristic)",
            "Adversarial",
            "Probabilistic"
        ],
        "answer_index": 0,
        "explanation": "IDDFS does not rely on a heuristic distance estimate; it systematically explores depths using uninformed depth-first search.",
        "difficulty": "Beginner",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "What is the space complexity of IDDFS where b is branching factor and d is solution depth?",
        "options": [
            "O(b * d)",
            "O(b^d)",
            "O(d^b)",
            "O(1)"
        ],
        "answer_index": 0,
        "explanation": "At depth limit d, the underlying DLS only retains nodes along the active branch of depth d, requiring O(b * d) space.",
        "difficulty": "Beginner",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "What apparent disadvantage does IDDFS have that concerns beginners?",
        "options": [
            "It re-expands nodes at shallow levels multiple times across successive iterations",
            "It uses more memory than BFS",
            "It cannot solve puzzles deeper than 5 moves",
            "It requires a supercomputer"
        ],
        "answer_index": 0,
        "explanation": "The root node is expanded in every single iteration, and shallow nodes are re-visited, which seems wasteful at first glance.",
        "difficulty": "Beginner",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "In a search tree where branching factor b = 3, why is the overhead of re-expanding nodes in IDDFS surprisingly small?",
        "options": [
            "Because the vast majority of nodes in an exponential tree reside in the bottom level (about 67-75% of all nodes)",
            "Because CPU caches store all previous trees",
            "Because shallow nodes are skipped",
            "Because the root node is free"
        ],
        "answer_index": 0,
        "explanation": "In an exponential tree, the bottom level contains more nodes than all previous levels combined, so re-expanding upper levels adds minimal cost.",
        "difficulty": "Beginner",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "When is IDDFS the preferred search strategy in artificial intelligence?",
        "options": [
            "When the search space is large, the solution depth is unknown, and memory is constrained",
            "When memory is infinite and all edges are weighted",
            "When we already know the exact solution moves",
            "When we want a random path"
        ],
        "answer_index": 0,
        "explanation": "IDDFS is the gold standard uninformed search for large state spaces because it guarantees optimality without running out of RAM.",
        "difficulty": "Beginner",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "What happens if IDDFS is run on an unsolvable 8-puzzle with max_depth limit = 50?",
        "options": [
            "It iterates through all limits up to 50, exhausts all states at each limit, and reports that no solution exists within 50 moves",
            "It crashes on depth 1",
            "It creates an infinite loop",
            "It fabricates a winning board"
        ],
        "answer_index": 0,
        "explanation": "IDDFS systematically checks every depth level up to the max depth cap before cleanly returning failure.",
        "difficulty": "Beginner",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "What is the time complexity of IDDFS in big-O notation?",
        "options": [
            "O(b^d)",
            "O(b * d)",
            "O(d!)",
            "O(2^d)"
        ],
        "answer_index": 0,
        "explanation": "The total nodes generated across all iterations is bounded by O(b^d), matching standard BFS asymptotically.",
        "difficulty": "Beginner",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "Mathematically, for branching factor b and depth d, the root node in IDDFS is generated (d + 1) times, depth 1 nodes d times, and depth d nodes 1 time. What is the total node count?",
        "options": [
            "Sum_{i=0}^d (d + 1 - i) * b^i = O(b^d)",
            "O(b^(d^2))",
            "O(d * b^d)",
            "O(b * d^2)"
        ],
        "answer_index": 0,
        "explanation": "The sum is dominated by the b^d term: N(IDDFS) = b^d / (1 - 1/b)^2, which is O(b^d). For b=10, the overhead is only about 11%.",
        "difficulty": "Intermediate",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "Compared to Breadth-First Search (BFS), IDDFS:",
        "options": [
            "Requires exponentially less memory while finding the exact same shortest path",
            "Requires more memory",
            "Is not complete",
            "Cannot run on trees"
        ],
        "answer_index": 0,
        "explanation": "IDDFS finds the identical optimal shortest path as BFS, but drops the memory requirement from O(b^d) to O(b * d).",
        "difficulty": "Intermediate",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "For b = 10 and d = 5, BFS generates approximately 111,111 nodes. How many nodes does IDDFS generate approximately?",
        "options": [
            "~123,456 nodes (only about 11% more than BFS)",
            "~1,000,000 nodes",
            "~10,000,000 nodes",
            "Exactly 50 nodes"
        ],
        "answer_index": 0,
        "explanation": "1*(10^5) + 2*(10^4) + 3*(10^3) + 4*(10^2) + 5*(10) + 6 = 123,456. The overhead for b=10 is only ~11% extra node generations.",
        "difficulty": "Intermediate",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "How does IDDFS know when to terminate if no solution exists in a FINITE state space?",
        "options": [
            "When an entire iteration completes without hitting any depth cutoff (no states were pruned by the limit)",
            "When limit reaches 1,000,000",
            "When CPU temperature rises",
            "When memory is exhausted"
        ],
        "answer_index": 0,
        "explanation": "If an iteration finishes and reports Failure (not Cutoff), every reachable state has been explored, proving no solution exists.",
        "difficulty": "Intermediate",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "Can IDDFS find the optimal solution if edge costs are non-uniform (e.g. edge weights 5, 20, 1)?",
        "options": [
            "No, standard IDDFS increments depth by step count; it is optimal only for uniform step costs",
            "Yes, IDDFS is optimal for all edge costs",
            "Only if all edge costs are negative",
            "Only if limit increments by 10"
        ],
        "answer_index": 0,
        "explanation": "IDDFS finds the path with the fewest edges; for non-uniform edge costs, Iterative Deepening A* (IDA*) or UCS is required.",
        "difficulty": "Intermediate",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "In the Algorithm Lab of this application, why might IDDFS show a slightly higher 'Nodes Explored' count than BFS for the same moves?",
        "options": [
            "Because IDDFS re-evaluates shallow nodes on each successive depth limit iteration",
            "Because IDDFS explores wrong paths randomly",
            "Because IDDFS uses a slower CPU clock",
            "Because IDDFS includes graph edge weights"
        ],
        "answer_index": 0,
        "explanation": "The cumulative node count of IDDFS tallies all node evaluations across iterations 0 through d.",
        "difficulty": "Intermediate",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "What is the branching factor threshold below which IDDFS re-expansion overhead becomes noticeably larger?",
        "options": [
            "Small branching factors like b = 2 (overhead ~100% extra nodes)",
            "Large branching factors like b = 100",
            "b = 10",
            "Overhead is independent of branching factor"
        ],
        "answer_index": 0,
        "explanation": "When b is small (e.g. binary tree b=2), the ratio b/(b-1) is 2, meaning roughly double the node generations of BFS.",
        "difficulty": "Intermediate",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "How does IDDFS avoid storing an entire explored set while still avoiding cycles?",
        "options": [
            "It checks for duplicate states along the current active branch (ancestor path) in O(d) space",
            "It saves states to a temporary disk file",
            "It ignores cycles completely",
            "It only expands leaf nodes"
        ],
        "answer_index": 0,
        "explanation": "Checking `state not in on_path` verifies the state has not appeared earlier on the current branch, avoiding cycles in linear memory.",
        "difficulty": "Intermediate",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "If the goal is at depth 0 (the start state is the goal), what does IDDFS do?",
        "options": [
            "Immediately finds the goal in iteration L=0 after expanding only 1 node",
            "Runs all 50 iterations anyway",
            "Reports an error",
            "Switches to BFS"
        ],
        "answer_index": 0,
        "explanation": "At L=0, the root node is tested; since start == goal, IDDFS halts immediately with path length 0.",
        "difficulty": "Intermediate",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "In tournament chess engines, why is Iterative Deepening standardly used for time management?",
        "options": [
            "If allotted time expires during a search, the engine can safely abort and play the best move from the last fully completed depth",
            "Chess engines only have 1 MB of RAM",
            "IDDFS solves chess completely",
            "Chess rules require depth-first search"
        ],
        "answer_index": 0,
        "explanation": "Iterative deepening provides an 'anytime algorithm' property: a valid move from the previous completed depth is always ready to play.",
        "difficulty": "Intermediate",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "What is Iterative Lengthening Search, and how does it relate to IDDFS and Uniform Cost Search?",
        "options": [
            "It increases a path cost limit C instead of a depth limit L, making iterative deepening optimal for non-uniform step costs",
            "It searches graphs with variable string lengths",
            "It doubles the word size of the CPU",
            "It is identical to Greedy Search"
        ],
        "answer_index": 0,
        "explanation": "Iterative Lengthening Search adapts IDDFS to arbitrary edge costs by incrementing cost cutoffs, achieving UCS optimality in linear space.",
        "difficulty": "Advanced",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "Why is IDDFS generally considered asymptotically superior to BFS for large state spaces with unit costs?",
        "options": [
            "Both have O(b^d) time complexity, but IDDFS requires O(b * d) space while BFS requires O(b^d) space",
            "IDDFS runs in O(d) time",
            "BFS is incomplete on trees",
            "IDDFS expands zero nodes"
        ],
        "answer_index": 0,
        "explanation": "Space is almost always the fatal bottleneck in search; IDDFS eliminates the exponential space bottleneck at negligible time overhead.",
        "difficulty": "Advanced",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "In a bidirectional version of IDDFS, what is the asymptotic time complexity for branching factor b and depth d?",
        "options": [
            "O(b^(d/2)) with linear O(b * (d/2)) space on the DFS side",
            "O(b^d)",
            "O(d^2)",
            "O(1)"
        ],
        "answer_index": 0,
        "explanation": "Bidirectional IDDFS combines the meeting-in-the-middle exponent d/2 with the linear memory characteristics of depth-bounded search.",
        "difficulty": "Advanced",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "How does the asymptotic overhead ratio R = N_IDDFS / N_BFS simplify as b becomes very large?",
        "options": [
            "R = b / (b - 1) -> 1 as b -> infinity (the overhead approaches 0%)",
            "R -> infinity",
            "R -> 0",
            "R -> 2"
        ],
        "answer_index": 0,
        "explanation": "As branching factor b grows large, the fraction of nodes in the final level approaches 100%, making previous level re-expansions negligible.",
        "difficulty": "Advanced",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "What is move ordering and how does it dramatically improve alpha-beta pruning within Iterative Deepening?",
        "options": [
            "Moves from the previous iteration are used to order successors in the current iteration, maximizing alpha-beta cutoffs",
            "Moves are sorted alphabetically",
            "Moves are executed in reverse",
            "Move ordering reduces branching factor to 0"
        ],
        "answer_index": 0,
        "explanation": "Evaluating the best move found at depth d-1 first at depth d triggers immediate beta cutoffs, minimizing node expansions to O(b^(d/2)).",
        "difficulty": "Advanced",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "In the 8-puzzle, why does IDDFS take noticeably longer in real-world seconds than A* for puzzles requiring 15+ moves?",
        "options": [
            "Because IDDFS is uninformed and blindly searches all directions, whereas A* uses Manhattan distance to focus toward the goal",
            "Because IDDFS has a bug in its loop",
            "Because 8-puzzle tiles cannot be incremented",
            "Because Python does not support recursion"
        ],
        "answer_index": 0,
        "explanation": "Uninformed IDDFS must explore the full exponential tree of size ~3^15 \u2248 14 million nodes, while A* prunes almost all of them.",
        "difficulty": "Advanced",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "Can IDDFS be used with a transposition table (transposition table IDDFS), and what trade-off does this introduce?",
        "options": [
            "Yes, storing visited states in a hash table prevents re-searching identical states, trading memory for speed",
            "No, transposition tables can only be used with BFS",
            "It eliminates all depth limits",
            "It makes IDDFS incomplete"
        ],
        "answer_index": 0,
        "explanation": "A transposition table caches state outcomes across iterations; if memory fills up, states can be replaced using LRU or depth schemes.",
        "difficulty": "Advanced",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "What happens if IDDFS increments the depth limit by 2 instead of 1 on each iteration?",
        "options": [
            "It reduces iteration overhead, but may discover a solution 1 move longer than optimal if the true depth was odd",
            "It guarantees finding optimal paths faster",
            "It crashes on even depths",
            "It becomes identical to A*"
        ],
        "answer_index": 0,
        "explanation": "Stepping by 2 risks overshooting: if the goal is at depth 3 and limit jumps from 2 to 4, a depth 4 path might be found first if explored earlier.",
        "difficulty": "Advanced",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "In a graph search with many alternate paths of equal length to the same node, how does IDDFS compare with BFS without a closed list?",
        "options": [
            "IDDFS will re-expand identical subtrees exponentially many times across separate paths unless path-merging is implemented",
            "IDDFS merges paths automatically",
            "BFS expands more paths than IDDFS",
            "Both have O(V) space"
        ],
        "answer_index": 0,
        "explanation": "On dense grid graphs with many cycles, tree-search IDDFS suffers from exponential path explosion, where graph BFS with a closed list shines.",
        "difficulty": "Advanced",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "Why is IDDFS guaranteed to terminate in finite time on any finite graph, even without a closed list?",
        "options": [
            "Because at each iteration L, no path exceeds L steps, and the number of paths of length <= L in a finite graph with finite b is finite",
            "Because all finite graphs are trees",
            "Because Python terminates after 1000 loops",
            "Because the start node is deleted"
        ],
        "answer_index": 0,
        "explanation": "Every single depth-limited run is bounded to depth L. Since b is finite, the tree of depth L is finite, guaranteeing finite termination.",
        "difficulty": "Advanced",
        "category": "Iterative Deepening DFS"
    },
    {
        "question": "What are the two primary components that define an intelligent agent?",
        "options": [
            "Sensors (to perceive) and Actuators (to act)",
            "Monitors and Keyboards",
            "CPUs and GPUs",
            "Databases and Tables"
        ],
        "answer_index": 0,
        "explanation": "An intelligent agent perceives its environment through sensors and affects that environment through actuators.",
        "difficulty": "Beginner",
        "category": "General AI & Agents"
    },
    {
        "question": "In the PEAS framework for describing intelligent agents, what does PEAS stand for?",
        "options": [
            "Performance measure, Environment, Actuators, Sensors",
            "Planning, Execution, Analysis, Search",
            "Program, Efficiency, Accuracy, Speed",
            "Perception, Entity, Action, State"
        ],
        "answer_index": 0,
        "explanation": "PEAS specifies Performance measure, Environment, Actuators, and Sensors when specifying an agent design.",
        "difficulty": "Beginner",
        "category": "General AI & Agents"
    },
    {
        "question": "What distinguishes a 'rational agent' from an omniscient agent?",
        "options": [
            "A rational agent maximizes expected performance given its knowledge; an omniscient agent knows the actual outcome of all actions",
            "A rational agent never makes mistakes",
            "An omniscient agent cannot use sensors",
            "There is no difference"
        ],
        "answer_index": 0,
        "explanation": "Rationality is about expected success given what the agent perceives, whereas omniscience requires knowing the future and all hidden variables.",
        "difficulty": "Beginner",
        "category": "General AI & Agents"
    },
    {
        "question": "Which environment property best describes the 8-puzzle problem?",
        "options": [
            "Fully observable, deterministic, static, discrete, single-agent",
            "Partially observable, stochastic, dynamic, continuous, multi-agent",
            "Continuous, dynamic, adversarial",
            "Stochastic, fully observable, continuous"
        ],
        "answer_index": 0,
        "explanation": "The 8-puzzle board is fully visible (fully observable), tile slides have 100% predictable outcomes (deterministic), doesn't change on its own (static), and has distinct states (discrete).",
        "difficulty": "Intermediate",
        "category": "General AI & Agents"
    },
    {
        "question": "What are the 5 formal components of a classical state-space problem formulation?",
        "options": [
            "Initial state, Actions, Transition model, Goal test, Path cost",
            "Sensors, Actuators, Camera, Motor, Wheels",
            "Start, Middle, End, Win, Loss",
            "Variables, Domains, Constraints, Heuristic, Pruning"
        ],
        "answer_index": 0,
        "explanation": "Russell and Norvig define problem formulation by: Initial state, Available actions, Transition model Result(s, a), Goal test, and Path cost c(s, a, s').",
        "difficulty": "Intermediate",
        "category": "General AI & Agents"
    },
    {
        "question": "What is the difference between an online search agent and an offline search agent?",
        "options": [
            "Offline search computes a complete solution before taking its first action; online search interleaves computation and action in the real world",
            "Online search uses the internet; offline search does not",
            "Offline search only runs on trees",
            "Online search is strictly uninformed"
        ],
        "answer_index": 0,
        "explanation": "Offline agents (like this puzzle solver) compute the full plan in simulation before moving; online agents must explore unknown environments dynamically.",
        "difficulty": "Advanced",
        "category": "General AI & Agents"
    },
    {
        "question": "How many total permutations of the 9 tiles (including blank 0) exist in the 8-puzzle?",
        "options": [
            "9! = 362,880 total configurations",
            "8! = 40,320 configurations",
            "9^2 = 81 configurations",
            "181,440 configurations"
        ],
        "answer_index": 0,
        "explanation": "There are 9 distinct tiles arranged in 9 grid slots, giving 9! = 362,880 possible arrangements.",
        "difficulty": "Beginner",
        "category": "8-Puzzle & State Space"
    },
    {
        "question": "How many of the 362,880 total configurations of the 8-puzzle can reach any given fixed goal state?",
        "options": [
            "Exactly half: 9! / 2 = 181,440 configurations",
            "All 362,880 configurations",
            "Only 40,320 configurations",
            "Only 1 configuration"
        ],
        "answer_index": 0,
        "explanation": "The state space is partitioned into two equal, disconnected halves of 181,440 states based on permutation parity.",
        "difficulty": "Beginner",
        "category": "8-Puzzle & State Space"
    },
    {
        "question": "In the 8-puzzle, what is an 'inversion'?",
        "options": [
            "A pair of non-blank tiles (A, B) where A appears before B in the list but A > B",
            "When the blank tile moves into a corner",
            "When two tiles swap diagonally",
            "When a puzzle cannot be solved in under 10 moves"
        ],
        "answer_index": 0,
        "explanation": "An inversion occurs whenever a larger numbered tile precedes a smaller numbered tile in the linear sequence of tiles (ignoring 0).",
        "difficulty": "Beginner",
        "category": "8-Puzzle & State Space"
    },
    {
        "question": "Why does any legal slide of a tile into the blank space preserve the even/odd parity of inversions in a 3x3 puzzle?",
        "options": [
            "Horizontal slides do not change tile order; vertical slides jump exactly 2 tiles, changing inversions by +2, 0, or -2 (always even)",
            "Because the board is square",
            "Because 3 is a prime number",
            "Because the blank tile always has value 0"
        ],
        "answer_index": 0,
        "explanation": "Moving a tile horizontally changes 0 non-blank pairs. Moving vertically shifts it past 2 non-blank tiles, altering inversion count by +/-2 or 0.",
        "difficulty": "Intermediate",
        "category": "8-Puzzle & State Space"
    },
    {
        "question": "How does the application check if an arbitrary initial state can reach an arbitrary user-selected goal state?",
        "options": [
            "By verifying that the number of inversions of the start state RELATIVE to the goal state ordering is even",
            "By checking if both start and goal have tile 1 at index 0",
            "By running BFS for 1 second",
            "By summing all tile numbers modulo 2"
        ],
        "answer_index": 0,
        "explanation": "Mapping start tiles to their target goal indices and verifying that the resulting relative permutation has an even inversion count guarantees solvability.",
        "difficulty": "Intermediate",
        "category": "8-Puzzle & State Space"
    },
    {
        "question": "What is the solvability rule for an N x N puzzle when N is EVEN (e.g. the 15-puzzle where N=4)?",
        "options": [
            "Solvable if: (inversions is even AND blank on odd row from bottom) OR (inversions is odd AND blank on even row from bottom)",
            "Solvable if and only if inversions are even, regardless of blank row",
            "All 15-puzzles are solvable",
            "Solvable only if blank is at (0,0)"
        ],
        "answer_index": 0,
        "explanation": "On even grids, vertical moves change the blank row parity by 1 and swap past an odd number of tiles (N-1 = 3), linking blank row to inversion parity.",
        "difficulty": "Advanced",
        "category": "8-Puzzle & State Space"
    },
    {
        "question": "How is the Manhattan distance heuristic calculated for the 8-puzzle?",
        "options": [
            "Sum of |current_row - goal_row| + |current_col - goal_col| for all non-blank tiles 1 to 8",
            "The count of tiles that are not in their goal position",
            "The straight-line Euclidean distance: sqrt(dx^2 + dy^2)",
            "The number of inversions in the board"
        ],
        "answer_index": 0,
        "explanation": "Manhattan distance measures grid displacement (horizontal + vertical steps) required for each numbered tile to reach its target slot.",
        "difficulty": "Beginner",
        "category": "Heuristic Functions"
    },
    {
        "question": "Why is the blank tile (0) excluded from the Manhattan distance calculation in the 8-puzzle?",
        "options": [
            "Because the blank is an empty space whose movement is just the byproduct of moving the 8 physical tiles",
            "Because 0 times anything is 0",
            "Because the blank tile cannot move",
            "To make the heuristic equal to 0"
        ],
        "answer_index": 0,
        "explanation": "Solving the puzzle means placing the 8 numbered tiles in place; once they are placed, the blank tile is automatically in place.",
        "difficulty": "Beginner",
        "category": "Heuristic Functions"
    },
    {
        "question": "Why is the Misplaced Tiles heuristic h1(n) dominated by the Manhattan Distance heuristic h2(n)?",
        "options": [
            "Every misplaced tile must move at least 1 grid step, so h2(n) >= h1(n) for every state n",
            "Because h1 is inadmissible",
            "Because h2 counts negative numbers",
            "Because h1 is faster to compute"
        ],
        "answer_index": 0,
        "explanation": "For every tile not in place, its Manhattan displacement is at least 1. Summing displacements is therefore always >= the count of misplaced tiles.",
        "difficulty": "Intermediate",
        "category": "Heuristic Functions"
    },
    {
        "question": "What is the Linear Conflict heuristic for the 8-puzzle, and why is it admissible?",
        "options": [
            "It adds 2 moves for every pair of tiles in their goal row/column but in inverted order, because one must move out of the row to let the other pass",
            "It measures conflicts between heuristic functions",
            "It computes linear regression on tile coordinates",
            "It is inadmissible but fast"
        ],
        "answer_index": 0,
        "explanation": "Two tiles in the correct row/col but reversed cannot slide past each other on a 1D line; one must leave the line and re-enter, adding at least 2 moves.",
        "difficulty": "Advanced",
        "category": "Heuristic Functions"
    },
    {
        "question": "In the classical Water Jug problem with Jug A (capacity 4L) and Jug B (capacity 3L), what is the goal?",
        "options": [
            "Measure exactly a target amount (e.g. 2L) using only Fill, Empty, and Pour operations",
            "Drink all the water in the jugs",
            "Measure temperature of the water",
            "Fill both jugs to the brim"
        ],
        "answer_index": 0,
        "explanation": "The problem asks to reach a target volume in one of the jugs using only full fills, full empties, and pouring between jugs.",
        "difficulty": "Beginner",
        "category": "Water Jug Problem"
    },
    {
        "question": "According to number theory (B\u00e9zout's identity), a Water Jug problem with capacities A and B can measure target amount C if and only if:",
        "options": [
            "C is a multiple of gcd(A, B) and C <= max(A, B)",
            "A and B are both prime numbers",
            "C is equal to A + B",
            "C is an even number"
        ],
        "answer_index": 0,
        "explanation": "Any measurable quantity is an integer linear combination x*A + y*B, which must be a multiple of the greatest common divisor gcd(A, B).",
        "difficulty": "Intermediate",
        "category": "Water Jug Problem"
    },
    {
        "question": "How is the Water Jug problem represented as an AI state-space search problem in this project?",
        "options": [
            "State is a tuple (a, b) of current water volumes; BFS explores transitions (Fill A, Fill B, Empty A, Empty B, Pour A->B, Pour B->A)",
            "Using a neural network to estimate flow rates",
            "Using differential equations",
            "Using linear programming"
        ],
        "answer_index": 0,
        "explanation": "State-space search models each jug configuration as a discrete node (a, b) and valid jug operations as directed graph edges.",
        "difficulty": "Advanced",
        "category": "Water Jug Problem"
    },
    {
        "question": "What is the main difference between Tree Search and Graph Search?",
        "options": [
            "Graph Search maintains an explored (closed) set to avoid re-expanding already-visited states and getting trapped in cycles",
            "Tree Search only works on binary trees",
            "Graph Search does not support heuristics",
            "Tree Search uses more memory than Graph Search"
        ],
        "answer_index": 0,
        "explanation": "Graph Search checks states against an explored set to prevent revisiting states reached via cycles or alternative paths.",
        "difficulty": "Beginner",
        "category": "Graph Search"
    },
    {
        "question": "In an undirected graph, how does `parse_edges` in this application represent edges?",
        "options": [
            "It stores bidirectional entries: edge (u, v) is added to both graph[u] and graph[v] with equal cost",
            "It only stores the edge from u to v",
            "It stores edges as random numbers",
            "It converts nodes to integers 0-8"
        ],
        "answer_index": 0,
        "explanation": "Undirected edges allow traversal in both directions, so adding 'A B 5' creates transitions A->B and B->A with cost 5.",
        "difficulty": "Intermediate",
        "category": "Graph Search"
    },
    {
        "question": "If a graph contains a disconnected component and the goal is in that component, how do all eight search algorithms behave?",
        "options": [
            "They explore all nodes reachable from the start node and then terminate, returning None (No path found)",
            "They hang in an infinite loop",
            "They automatically add a bridge edge",
            "They return the start node as the goal"
        ],
        "answer_index": 0,
        "explanation": "When the goal is unreachable, search exhaustively explores the connected component of the start node before cleanly reporting failure.",
        "difficulty": "Advanced",
        "category": "Graph Search"
    }
]
