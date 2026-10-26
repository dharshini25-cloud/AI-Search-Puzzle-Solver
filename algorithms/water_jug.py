"""
Water Jug Problem solver using BFS state-space search.
"""

from collections import deque


def solve_water_jug(cap_a, cap_b, target):
    """
    Solve the water jug problem with BFS.

    Parameters
    ----------
    cap_a   : int  capacity of Jug A
    cap_b   : int  capacity of Jug B
    target  : int  desired amount in either jug

    Returns
    -------
    (steps, nodes_explored) where steps is a list of dicts:
        {"a": int, "b": int, "action": str}
    or (None, nodes_explored) if no solution exists.
    """
    if target > max(cap_a, cap_b):
        return None, 0

    start = (0, 0)
    goal_check = lambda a, b: a == target or b == target

    if goal_check(*start):
        return [{"a": 0, "b": 0, "action": "Start (already solved)"}], 0

    queue = deque([(start, [{"a": 0, "b": 0, "action": "Initial state"}])])
    visited = {start}
    nodes_explored = 0

    while queue:
        (a, b), history = queue.popleft()
        nodes_explored += 1

        # Generate all valid successor states.
        successors = [
            (cap_a, b, f"Fill Jug A to {cap_a}L"),
            (a, cap_b, f"Fill Jug B to {cap_b}L"),
            (0, b, "Empty Jug A"),
            (a, 0, "Empty Jug B"),
        ]

        # Pour A → B
        pour_ab = min(a, cap_b - b)
        successors.append(
            (a - pour_ab, b + pour_ab, f"Pour {pour_ab}L from A to B")
        )

        # Pour B → A
        pour_ba = min(b, cap_a - a)
        successors.append(
            (a + pour_ba, b - pour_ba, f"Pour {pour_ba}L from B to A")
        )

        for na, nb, action in successors:
            if (na, nb) in visited:
                continue

            visited.add((na, nb))
            new_history = history + [{"a": na, "b": nb, "action": action}]

            if goal_check(na, nb):
                return new_history, nodes_explored

            queue.append(((na, nb), new_history))

    return None, nodes_explored
