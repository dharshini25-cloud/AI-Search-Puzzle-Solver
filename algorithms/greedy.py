
import heapq
from itertools import count


def manhattan_distance(state, goal):
    distance = 0

    for tile in range(1, 9):
        current = state.index(tile)
        target = goal.index(tile)

        row1, col1 = divmod(current, 3)
        row2, col2 = divmod(target, 3)

        distance += abs(row1 - row2) + abs(col1 - col2)

    return distance


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


def greedy(start, goal):
    """Find a path using Greedy Best-First Search."""
    start = tuple(start)
    goal = tuple(goal)

    if start == goal:
        return [start], 0

    tie_breaker = count()
    frontier = [
        (manhattan_distance(start, goal), next(tie_breaker), start)
    ]

    came_from = {start: None}
    visited = set()
    nodes_explored = 0

    while frontier:
        _, _, current = heapq.heappop(frontier)

        if current in visited:
            continue

        visited.add(current)
        nodes_explored += 1

        if current == goal:
            path = []
            state = goal

            while state is not None:
                path.append(state)
                state = came_from[state]

            return path[::-1], nodes_explored

        for neighbor in get_neighbors(current):
            if neighbor not in visited and neighbor not in came_from:
                came_from[neighbor] = current

                heapq.heappush(
                    frontier,
                    (
                        manhattan_distance(neighbor, goal),
                        next(tie_breaker),
                        neighbor,
                    ),
                )

    return None, nodes_explored
