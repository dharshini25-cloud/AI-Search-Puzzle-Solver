
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from algorithms.iddfs import iddfs

start = (1, 2, 3,
         4, 5, 6,
         7, 0, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

path, explored = iddfs(start, goal, max_depth=10)

print("Solution found:", path is not None)
print("Total nodes explored across depth limits:", explored)

if path:
    print("Number of moves:", len(path) - 1)

    for step, state in enumerate(path):
        print(f"\nStep {step}:")
        for i in range(0, 9, 3):
            print(state[i:i + 3])
else:
    print("No solution found within the maximum depth.")
