
import heapq
from itertools import count


def manhattan_distance(state, goal):
    """Calculate Manhattan distance, ignoring the blank tile."""
    distance = 0

    for tile in range(1, 9):
        current = state.index(tile)
        target = goal.index(tile)

        row1, col1 = divmod(current, 3)
        row2, col2 = divmod(target, 3)

        distance += abs(row1 - row2) + abs(col1 - col2)

    return distance


def get_neighbors(state):
    """Generate valid next states."""
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


def astar(start, goal):
    """Find an optimal path using A* search."""
    start = tuple(start)
    goal = tuple(goal)

    if start == goal:
        return [start], 0

    tie_breaker = count()
    frontier = [
        (manhattan_distance(start, goal), next(tie_breaker), 0, start)
    ]

    came_from = {start: None}
    cost_so_far = {start: 0}
    nodes_explored = 0

    while frontier:
        _, _, current_cost, current = heapq.heappop(frontier)

        if current_cost != cost_so_far.get(current):
            continue

        nodes_explored += 1

        if current == goal:
            path = []
            state = goal

            while state is not None:
                path.append(state)
                state = came_from[state]

            return path[::-1], nodes_explored

        for neighbor in get_neighbors(current):
            new_cost = current_cost + 1

            if new_cost < cost_so_far.get(neighbor, float("inf")):
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current

                priority = new_cost + manhattan_distance(neighbor, goal)

                heapq.heappush(
                    frontier,
                    (priority, next(tie_breaker), new_cost, neighbor),
                )

    return None, nodes_explored
