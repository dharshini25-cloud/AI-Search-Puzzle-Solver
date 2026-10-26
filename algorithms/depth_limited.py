
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


def depth_limited(start, goal, limit=20):
    """Search up to a maximum depth. Returns path, explored count."""
    start = tuple(start)
    goal = tuple(goal)
    nodes_explored = 0

    def search(state, depth, path, on_path):
        nonlocal nodes_explored
        nodes_explored += 1

        if state == goal:
            return path

        if depth == limit:
            return None

        for neighbor in get_neighbors(state):
            if neighbor not in on_path:
                result = search(
                    neighbor,
                    depth + 1,
                    path + [neighbor],
                    on_path | {neighbor},
                )

                if result is not None:
                    return result

        return None

    path = search(start, 0, [start], {start})
    return path, nodes_explored
