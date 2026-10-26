
def get_neighbors(state):
    neighbors = []
    blank = state.index(0)
    row, col = divmod(blank, 3)

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new_blank = nr * 3 + nc
            new_state = list(state)
            new_state[blank], new_state[new_blank] = (
                new_state[new_blank],
                new_state[blank],
            )
            neighbors.append(tuple(new_state))

    return neighbors


def dfs(start, goal, max_depth=30):
    """Depth-First Search with a depth limit and visited-state tracking."""
    start = tuple(start)
    goal = tuple(goal)

    if start == goal:
        return [start], 1

    stack = [(start, [start])]
    visited = set()
    nodes_explored = 0

    while stack:
        current, path = stack.pop()
        depth = len(path) - 1

        if current in visited:
            continue

        visited.add(current)
        nodes_explored += 1

        if current == goal:
            return path, nodes_explored

        if depth >= max_depth:
            continue

        # Append in order so the last neighbor is explored first.
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None, nodes_explored
