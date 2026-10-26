
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


def iddfs(start, goal, max_depth=50):
    """Find a solution by repeatedly increasing the depth limit."""
    start = tuple(start)
    goal = tuple(goal)
    total_explored = 0

    def depth_limited_search(state, depth, path, on_path):
        nonlocal total_explored
        total_explored += 1

        if state == goal:
            return path

        if depth == 0:
            return None

        for neighbor in get_neighbors(state):
            if neighbor not in on_path:
                result = depth_limited_search(
                    neighbor,
                    depth - 1,
                    path + [neighbor],
                    on_path | {neighbor},
                )

                if result is not None:
                    return result

        return None

    for limit in range(max_depth + 1):
        path = depth_limited_search(start, limit, [start], {start})

        if path is not None:
            return path, total_explored

    return None, total_explored
