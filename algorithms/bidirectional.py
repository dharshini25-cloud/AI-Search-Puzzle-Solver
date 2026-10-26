
from collections import deque


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


def bidirectional(start, goal):
    """Find a shortest path using bidirectional BFS."""
    start = tuple(start)
    goal = tuple(goal)

    if start == goal:
        return [start], 1

    forward_queue = deque([start])
    backward_queue = deque([goal])

    forward_parent = {start: None}
    backward_parent = {goal: None}

    nodes_explored = 0
    meeting = None

    while forward_queue and backward_queue:
        # Expand one layer from the forward side.
        for _ in range(len(forward_queue)):
            current = forward_queue.popleft()
            nodes_explored += 1

            if current in backward_parent:
                meeting = current
                break

            for neighbor in get_neighbors(current):
                if neighbor not in forward_parent:
                    forward_parent[neighbor] = current
                    forward_queue.append(neighbor)

                    if neighbor in backward_parent:
                        meeting = neighbor
                        break

            if meeting is not None:
                break

        if meeting is not None:
            break

        # Expand one layer from the backward side.
        for _ in range(len(backward_queue)):
            current = backward_queue.popleft()
            nodes_explored += 1

            if current in forward_parent:
                meeting = current
                break

            for neighbor in get_neighbors(current):
                if neighbor not in backward_parent:
                    backward_parent[neighbor] = current
                    backward_queue.append(neighbor)

                    if neighbor in forward_parent:
                        meeting = neighbor
                        break

            if meeting is not None:
                break

        if meeting is not None:
            break

    if meeting is None:
        return None, nodes_explored

    # Reconstruct the start-to-meeting path.
    path = []
    current = meeting

    while current is not None:
        path.append(current)
        current = forward_parent[current]

    path.reverse()

    # Append the meeting-to-goal path.
    current = backward_parent[meeting]

    while current is not None:
        path.append(current)
        current = backward_parent[current]

    return path, nodes_explored
