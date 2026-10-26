"""
Puzzle validation and solvability utilities.

For the 3×3 sliding puzzle, two states can reach each other if and only if
they have the same *relative* inversion parity.  We count inversions of the
start state expressed in terms of the goal ordering, then check whether that
count is even.

This works correctly for *any* valid goal state, not just the standard
[1,2,3,4,5,6,7,8,0] goal.
"""


def validate_puzzle(state):
    """Return True if state contains every integer 0–8 exactly once."""
    return len(state) == 9 and sorted(state) == list(range(9))


def count_inversions_relative(state, goal):
    """
    Count the number of inversions in `state` relative to `goal`.

    Algorithm
    ---------
    1. Build a mapping  tile → goal_position  (excluding the blank).
    2. Translate `state` into a sequence of goal-positions (excluding blank).
    3. Count pairs (i, j) where i < j but goal_pos[i] > goal_pos[j].

    This counts how "out of order" the tiles in `state` are with respect to
    the goal arrangement.
    """
    state = list(state)
    goal = list(goal)

    # Map each non-blank tile to its target position in the goal.
    goal_pos = {tile: idx for idx, tile in enumerate(goal) if tile != 0}

    # Translate start state into a sequence of goal-position indices.
    seq = [goal_pos[tile] for tile in state if tile != 0]

    inversions = 0
    n = len(seq)
    for i in range(n):
        for j in range(i + 1, n):
            if seq[i] > seq[j]:
                inversions += 1
    return inversions


def is_solvable(start, goal):
    """
    Return True if the start state can reach the goal state through legal
    sliding-puzzle moves.

    For a 3×3 puzzle on an odd-width grid, a configuration is reachable
    from the goal if and only if the number of inversions (relative to the
    goal) is even.
    """
    if not validate_puzzle(list(start)) or not validate_puzzle(list(goal)):
        return False
    return count_inversions_relative(start, goal) % 2 == 0


def format_state(state):
    """Convert a flat 9-element puzzle state into three rows of three."""
    return [
        list(state[0:3]),
        list(state[3:6]),
        list(state[6:9]),
    ]


def explain_unsolvable(start, goal):
    """
    Return a human-readable explanation of why start cannot reach goal.
    """
    inv = count_inversions_relative(start, goal)
    return (
        f"This puzzle is mathematically unsolvable: the number of inversions "
        f"relative to the goal is {inv} (odd). No sequence of legal tile "
        f"slides can transform the initial arrangement into the goal. "
        f"Try a different initial state or goal state."
    )