"""
Graph search module — all eight algorithms on user-defined graphs.

Supported algorithms
--------------------
BFS, DFS, A*, Greedy Best-First, Bidirectional BFS,
Uniform Cost Search, Depth-Limited Search, IDDFS.

Graph representation
--------------------
graph     : dict[str, list[str]]          adjacency list
edge_costs: dict[tuple[str,str], float]   (u,v) → weight (both directions)
heuristic : dict[str, float]              node → h-value for informed search

All functions return (path, traversal_order, nodes_explored).
path is None when no solution is found.
"""

from collections import deque


# ─────────────────────────────────────────────────────────────────────────────
# Shared utilities
# ─────────────────────────────────────────────────────────────────────────────

def _cost(edge_costs, u, v):
    """Return edge cost; default 1 if not specified."""
    return edge_costs.get((u, v), edge_costs.get((v, u), 1.0))


def _neighbors(graph, node, directed=False):
    """Return sorted neighbor list."""
    return sorted(graph.get(node, []))


# ─────────────────────────────────────────────────────────────────────────────
# BFS
# ─────────────────────────────────────────────────────────────────────────────

def bfs_graph(graph, start, goal, directed=False, **_):
    if start not in graph:
        return None, [], 0
    if start == goal:
        return [start], [start], 1

    queue = deque([(start, [start])])
    visited = {start}
    traversal = []
    explored = 0

    while queue:
        node, path = queue.popleft()
        traversal.append(node)
        explored += 1

        for nb in _neighbors(graph, node, directed):
            if nb not in visited:
                visited.add(nb)
                new_path = path + [nb]
                if nb == goal:
                    traversal.append(nb)
                    return new_path, traversal, explored
                queue.append((nb, new_path))

    return None, traversal, explored


# ─────────────────────────────────────────────────────────────────────────────
# DFS
# ─────────────────────────────────────────────────────────────────────────────

def dfs_graph(graph, start, goal, directed=False, **_):
    if start not in graph:
        return None, [], 0
    if start == goal:
        return [start], [start], 1

    stack = [(start, [start])]
    visited = set()
    traversal = []
    explored = 0

    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        traversal.append(node)
        explored += 1

        if node == goal:
            return path, traversal, explored

        for nb in reversed(_neighbors(graph, node, directed)):
            if nb not in visited:
                stack.append((nb, path + [nb]))

    return None, traversal, explored


# ─────────────────────────────────────────────────────────────────────────────
# A*
# ─────────────────────────────────────────────────────────────────────────────

def astar_graph(graph, start, goal, edge_costs=None, heuristic=None, directed=False, **_):
    import heapq
    from itertools import count

    edge_costs = edge_costs or {}
    heuristic = heuristic or {}

    if start not in graph:
        return None, [], 0
    if start == goal:
        return [start], [start], 1

    tie = count()
    frontier = [(heuristic.get(start, 0), next(tie), 0.0, start)]
    came_from = {start: None}
    g_cost = {start: 0.0}
    traversal = []
    explored = 0

    while frontier:
        _, _, g, node = heapq.heappop(frontier)

        if g > g_cost.get(node, float("inf")):
            continue

        traversal.append(node)
        explored += 1

        if node == goal:
            path = []
            cur = goal
            while cur is not None:
                path.append(cur)
                cur = came_from[cur]
            return path[::-1], traversal, explored

        for nb in _neighbors(graph, node, directed):
            new_g = g + _cost(edge_costs, node, nb)
            if new_g < g_cost.get(nb, float("inf")):
                g_cost[nb] = new_g
                came_from[nb] = node
                h = heuristic.get(nb, 0)
                heapq.heappush(frontier, (new_g + h, next(tie), new_g, nb))

    return None, traversal, explored


# ─────────────────────────────────────────────────────────────────────────────
# Greedy Best-First Search
# ─────────────────────────────────────────────────────────────────────────────

def greedy_graph(graph, start, goal, heuristic=None, directed=False, **_):
    import heapq
    from itertools import count

    heuristic = heuristic or {}

    if start not in graph:
        return None, [], 0
    if start == goal:
        return [start], [start], 1

    tie = count()
    frontier = [(heuristic.get(start, 0), next(tie), start)]
    came_from = {start: None}
    visited = set()
    traversal = []
    explored = 0

    while frontier:
        _, _, node = heapq.heappop(frontier)
        if node in visited:
            continue
        visited.add(node)
        traversal.append(node)
        explored += 1

        if node == goal:
            path = []
            cur = goal
            while cur is not None:
                path.append(cur)
                cur = came_from[cur]
            return path[::-1], traversal, explored

        for nb in _neighbors(graph, node, directed):
            if nb not in visited and nb not in came_from:
                came_from[nb] = node
                h = heuristic.get(nb, 0)
                heapq.heappush(frontier, (h, next(tie), nb))

    return None, traversal, explored


# ─────────────────────────────────────────────────────────────────────────────
# Uniform Cost Search
# ─────────────────────────────────────────────────────────────────────────────

def ucs_graph(graph, start, goal, edge_costs=None, directed=False, **_):
    import heapq
    from itertools import count

    edge_costs = edge_costs or {}

    if start not in graph:
        return None, [], 0
    if start == goal:
        return [start], [start], 1

    tie = count()
    frontier = [(0.0, next(tie), start)]
    came_from = {start: None}
    g_cost = {start: 0.0}
    traversal = []
    explored = 0

    while frontier:
        g, _, node = heapq.heappop(frontier)

        if g > g_cost.get(node, float("inf")):
            continue

        traversal.append(node)
        explored += 1

        if node == goal:
            path = []
            cur = goal
            while cur is not None:
                path.append(cur)
                cur = came_from[cur]
            return path[::-1], traversal, explored

        for nb in _neighbors(graph, node, directed):
            new_g = g + _cost(edge_costs, node, nb)
            if new_g < g_cost.get(nb, float("inf")):
                g_cost[nb] = new_g
                came_from[nb] = node
                heapq.heappush(frontier, (new_g, next(tie), nb))

    return None, traversal, explored


# ─────────────────────────────────────────────────────────────────────────────
# Bidirectional BFS
# ─────────────────────────────────────────────────────────────────────────────

def bidirectional_graph(graph, start, goal, directed=False, **_):
    if start not in graph:
        return None, [], 0
    if start == goal:
        return [start], [start], 1

    fwd_q = deque([start])
    bwd_q = deque([goal])
    fwd_parent = {start: None}
    bwd_parent = {goal: None}
    traversal = []
    explored = 0
    meeting = None

    def _get_reverse_neighbors(node):
        """For undirected graphs, same as forward neighbors."""
        return _neighbors(graph, node, directed)

    while fwd_q and bwd_q and meeting is None:
        # Expand one forward layer
        for _ in range(len(fwd_q)):
            if meeting:
                break
            node = fwd_q.popleft()
            traversal.append(node)
            explored += 1
            for nb in _neighbors(graph, node, directed):
                if nb not in fwd_parent:
                    fwd_parent[nb] = node
                    fwd_q.append(nb)
                if nb in bwd_parent:
                    meeting = nb
                    break

        if meeting:
            break

        # Expand one backward layer
        for _ in range(len(bwd_q)):
            if meeting:
                break
            node = bwd_q.popleft()
            traversal.append(node)
            explored += 1
            for nb in _get_reverse_neighbors(node):
                if nb not in bwd_parent:
                    bwd_parent[nb] = node
                    bwd_q.append(nb)
                if nb in fwd_parent:
                    meeting = nb
                    break

    if meeting is None:
        return None, traversal, explored

    # Reconstruct path: start → meeting
    path = []
    cur = meeting
    while cur is not None:
        path.append(cur)
        cur = fwd_parent[cur]
    path.reverse()

    # Append meeting → goal (excluding meeting itself)
    cur = bwd_parent.get(meeting)
    while cur is not None:
        path.append(cur)
        cur = bwd_parent.get(cur)

    return path, traversal, explored


# ─────────────────────────────────────────────────────────────────────────────
# Depth-Limited Search
# ─────────────────────────────────────────────────────────────────────────────

def depth_limited_graph(graph, start, goal, limit=10, directed=False, **_):
    if start not in graph:
        return None, [], 0

    traversal = []
    explored = [0]

    def _dls(node, path, on_path, depth):
        traversal.append(node)
        explored[0] += 1
        if node == goal:
            return path
        if depth == 0:
            return None
        for nb in _neighbors(graph, node, directed):
            if nb not in on_path:
                result = _dls(nb, path + [nb], on_path | {nb}, depth - 1)
                if result is not None:
                    return result
        return None

    path = _dls(start, [start], {start}, limit)
    return path, traversal, explored[0]


# ─────────────────────────────────────────────────────────────────────────────
# IDDFS
# ─────────────────────────────────────────────────────────────────────────────

def iddfs_graph(graph, start, goal, max_depth=20, directed=False, **_):
    if start not in graph:
        return None, [], 0

    traversal = []
    explored = [0]

    def _dls(node, path, on_path, depth):
        traversal.append(node)
        explored[0] += 1
        if node == goal:
            return path
        if depth == 0:
            return None
        for nb in _neighbors(graph, node, directed):
            if nb not in on_path:
                result = _dls(nb, path + [nb], on_path | {nb}, depth - 1)
                if result is not None:
                    return result
        return None

    for lim in range(max_depth + 1):
        path = _dls(start, [start], {start}, lim)
        if path is not None:
            return path, traversal, explored[0]

    return None, traversal, explored[0]


# ─────────────────────────────────────────────────────────────────────────────
# Dispatcher
# ─────────────────────────────────────────────────────────────────────────────

GRAPH_ALGORITHMS = {
    "BFS":                      bfs_graph,
    "DFS":                      dfs_graph,
    "A* Search":                astar_graph,
    "Greedy Best-First Search": greedy_graph,
    "Bidirectional BFS":        bidirectional_graph,
    "Uniform Cost Search":      ucs_graph,
    "Depth-Limited Search":     depth_limited_graph,
    "IDDFS":                    iddfs_graph,
}


def run_graph_algorithm(algo_name, graph, start, goal,
                        edge_costs=None, heuristic=None,
                        directed=False, limit=10, max_depth=20):
    """
    Unified dispatcher for all graph search algorithms.

    Returns (path, traversal_order, nodes_explored).
    """
    fn = GRAPH_ALGORITHMS.get(algo_name)
    if fn is None:
        raise ValueError(f"Unknown algorithm: {algo_name!r}")

    kwargs = dict(
        graph=graph,
        start=start,
        goal=goal,
        edge_costs=edge_costs or {},
        heuristic=heuristic or {},
        directed=directed,
        limit=limit,
        max_depth=max_depth,
    )
    return fn(**kwargs)


# ─────────────────────────────────────────────────────────────────────────────
# Edge parser
# ─────────────────────────────────────────────────────────────────────────────

def parse_edges(edge_text, directed=False):
    """
    Parse a multi-line edge definition.

    Accepted formats per line:
        A B          → undirected edge, cost 1
        A B 5        → undirected edge, cost 5
        A,B,5        → comma-separated variant

    Returns (graph, edge_costs).
    graph      : {node: [neighbors]}
    edge_costs : {(u,v): float}
    """
    graph: dict = {}
    edge_costs: dict = {}

    for raw_line in edge_text.strip().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        # Support comma-separated format
        parts = [p.strip() for p in line.replace(",", " ").split() if p.strip()]
        if len(parts) < 2:
            continue

        a, b = parts[0].upper(), parts[1].upper()
        try:
            cost = float(parts[2]) if len(parts) >= 3 else 1.0
        except ValueError:
            cost = 1.0

        for node in (a, b):
            graph.setdefault(node, [])

        if b not in graph[a]:
            graph[a].append(b)
        edge_costs[(a, b)] = cost

        if not directed:
            if a not in graph[b]:
                graph[b].append(a)
            edge_costs[(b, a)] = cost

    return graph, edge_costs
