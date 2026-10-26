
from collections import deque


def bfs(start, goal):
    """Find the shortest path using Breadth-First Search."""
    start = tuple(start)
    goal = tuple(goal)

    if start == goal:
        return [start], 0

    queue = deque([(start, [start])])
    visited = {start}
    nodes_explored = 0

    while queue:
        current, path = queue.popleft()
        nodes_explored += 1

        for neighbor in get_neighbors(current):
            if neighbor in visited:
                continue

            visited.add(neighbor)
            new_path = path + [neighbor]

            if neighbor == goal:
                return new_path, nodes_explored

            queue.append((neighbor, new_path))

    return None, nodes_explored


def get_neighbors(state):
    """Generate valid neighboring 3x3 puzzle states."""
    neighbors = []
    blank = state.index(0)
    row, col = divmod(blank, 3)

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank = new_row * 3 + new_col
            new_state = list(state)
            new_state[blank], new_state[new_blank] = (
                new_state[new_blank],
                new_state[blank],
            )
            neighbors.append(tuple(new_state))

    return neighbors

