
import heapq
from itertools import count


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


def uniform_cost(start, goal):
    """Find a minimum-cost path using Uniform Cost Search."""
    start = tuple(start)
    goal = tuple(goal)

    if start == goal:
        return [start], 0

    tie_breaker = count()
    frontier = [(0, next(tie_breaker), start)]
    cost_so_far = {start: 0}
    came_from = {start: None}
    nodes_explored = 0

    while frontier:
        current_cost, _, current = heapq.heappop(frontier)

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

                heapq.heappush(
                    frontier,
                    (new_cost, next(tie_breaker), neighbor),
                )

    return None, nodes_explored
