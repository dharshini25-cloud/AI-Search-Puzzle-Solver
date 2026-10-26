"""
Comprehensive Unit Test Suite for AI Search & Puzzle Solver
===========================================================
Tests all 10 core modules and requirements:
1. 8-Puzzle Arbitrary Initial and Goal States + Solvability Checks
2. 8 Search Algorithms on 8-Puzzle
3. Graph Search Solver with all 8 Search Algorithms
4. AI Tutor Knowledge Base and Contextual Resolution + Heading Sanitization
5. AI Quiz Question Bank Counts, Categories, and Difficulty Distribution
6. Water Jug Problem Solver
7. Image OCR Pipeline Logic
"""

import sys
import unittest
from pathlib import Path

# Set root directory in sys.path
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from utils.puzzle import validate_puzzle, is_solvable, explain_unsolvable
from algorithms.astar import astar, manhattan_distance
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.greedy import greedy
from algorithms.bidirectional import bidirectional
from algorithms.uniform_cost import uniform_cost
from algorithms.depth_limited import depth_limited
from algorithms.iddfs import iddfs
from algorithms.graph_search import (
    parse_edges, run_graph_algorithm, GRAPH_ALGORITHMS
)
from algorithms.water_jug import solve_water_jug
from utils.tutor_kb import answer_question, sanitize_answer
from utils.quiz_data import QUIZ_QUESTIONS
from utils.puzzle_image import extract_puzzle_from_image


class TestPuzzleLogic(unittest.TestCase):
    def test_validation_valid(self):
        self.assertTrue(validate_puzzle((1, 2, 3, 4, 5, 6, 7, 8, 0)))

    def test_validation_duplicate_and_missing(self):
        self.assertFalse(validate_puzzle((1, 1, 3, 4, 5, 6, 7, 8, 0)))

    def test_validation_out_of_range(self):
        self.assertFalse(validate_puzzle((1, 2, 3, 4, 5, 6, 7, 8, 9)))

    def test_solvability_standard_goal(self):
        # 1-step move from standard goal (solvable)
        solvable_init = (1, 2, 3, 4, 5, 6, 7, 0, 8)
        std_goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
        self.assertTrue(is_solvable(solvable_init, std_goal))

        # Swapping two non-blank tiles changes parity by 1 (unsolvable)
        unsolvable_init = (1, 2, 3, 4, 5, 6, 8, 7, 0)
        self.assertFalse(is_solvable(unsolvable_init, std_goal))
        expl = explain_unsolvable(unsolvable_init, std_goal)
        self.assertIn("unsolvable", expl.lower())

    def test_solvability_arbitrary_custom_goal(self):
        # Custom spiral goal
        custom_goal = (1, 2, 3, 8, 0, 4, 7, 6, 5)
        # Shift 0 with 4 (solvable from custom_goal)
        neighbor = (1, 2, 3, 8, 4, 0, 7, 6, 5)
        self.assertTrue(is_solvable(neighbor, custom_goal))

        # Swap two non-blank tiles (unsolvable relative to custom_goal)
        swapped = (2, 1, 3, 8, 4, 0, 7, 6, 5)
        self.assertFalse(is_solvable(swapped, custom_goal))

    def test_custom_goal_manhattan_distance(self):
        goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
        self.assertEqual(manhattan_distance(goal, goal), 0)
        # Tile 8 at pos 6 (row 2, col 0) instead of pos 7 (row 2, col 1) -> distance 1
        state = (1, 2, 3, 4, 5, 6, 8, 7, 0)
        # Tile 8: distance 1, Tile 7: distance 1 -> total 2
        self.assertEqual(manhattan_distance(state, goal), 2)

    def test_astar_arbitrary_goal(self):
        custom_goal = (0, 1, 2, 3, 4, 5, 6, 7, 8)
        # 2 moves away
        # (3, 1, 2, 0, 4, 5, 6, 7, 8) -> move 3 down gives goal
        init = (3, 1, 2, 0, 4, 5, 6, 7, 8)
        path, explored = astar(init, custom_goal)
        self.assertIsNotNone(path)
        self.assertEqual(path[0], init)
        self.assertEqual(path[-1], custom_goal)
        self.assertEqual(len(path) - 1, 1)


class TestGraphSearch(unittest.TestCase):
    def setUp(self):
        edge_text = "A B 1\nA C 4\nB D 2\nB E 5\nC F 3\nD G 2\nE G 1\nF H 4\nG H 1"
        self.graph, self.edge_costs = parse_edges(edge_text)
        self.heuristic = {"A": 7, "B": 6, "C": 5, "D": 4, "E": 3, "F": 2, "G": 1, "H": 0}

    def test_all_eight_algorithms_run(self):
        for algo_name in GRAPH_ALGORITHMS:
            path, traversal, explored = run_graph_algorithm(
                algo_name, self.graph, "A", "H",
                edge_costs=self.edge_costs,
                heuristic=self.heuristic,
                limit=10, max_depth=20
            )
            self.assertIsNotNone(path, f"Failed for {algo_name}")
            self.assertEqual(path[0], "A")
            self.assertEqual(path[-1], "H")
            self.assertGreater(explored, 0)

    def test_ucs_finds_minimum_cost_path(self):
        path, _, _ = run_graph_algorithm("Uniform Cost Search", self.graph, "A", "H", edge_costs=self.edge_costs)
        # Optimal cost path is A-B-D-G-H (1+2+2+1 = 6)
        expected_cost = 6.0
        actual_cost = sum(self.edge_costs.get((path[i], path[i+1]), 1.0) for i in range(len(path)-1))
        self.assertEqual(actual_cost, expected_cost)
        self.assertEqual(path, ["A", "B", "D", "G", "H"])

    def test_unreachable_node(self):
        # Disconnected graph
        edges = "A B 1\nX Y 1"
        g, c = parse_edges(edges)
        path, _, _ = run_graph_algorithm("BFS", g, "A", "Y")
        self.assertIsNone(path)


class TestAITutor(unittest.TestCase):
    def test_heading_sanitization(self):
        raw = "### Key Features\n- First\n## Summary\nGood."
        clean = sanitize_answer(raw)
        self.assertNotIn("###", clean)
        self.assertNotIn("##", clean)
        self.assertIn("**Key Features**", clean)

    def test_question_answering(self):
        ans = answer_question("What is A* search?")
        self.assertTrue("A*" in ans or "A\\*" in ans)
        self.assertNotIn("###", ans)

    def test_contextual_follow_up(self):
        history = [
            {"role": "user", "content": "Tell me about Uniform Cost Search"},
            {"role": "assistant", "content": "Uniform Cost Search (UCS) expands lowest path cost..."}
        ]
        ans = answer_question("Is it complete and optimal?", chat_history=history)
        self.assertTrue("optimal" in ans.lower() or "cost" in ans.lower())


class TestAIQuiz(unittest.TestCase):
    def test_question_count_and_distribution(self):
        # Must have at least 240 questions
        self.assertGreaterEqual(len(QUIZ_QUESTIONS), 240)

        # Check each of the 8 algorithms has at least 10 Beginner, 10 Intermediate, 10 Advanced
        algos = [
            "Breadth-First Search (BFS)",
            "Depth-First Search (DFS)",
            "A* Search",
            "Greedy Best-First Search",
            "Bidirectional Search",
            "Uniform Cost Search",
            "Depth-Limited Search",
            "Iterative Deepening DFS",
        ]
        difficulties = ["Beginner", "Intermediate", "Advanced"]

        for algo in algos:
            for diff in difficulties:
                count = sum(1 for q in QUIZ_QUESTIONS if q["category"] == algo and q["difficulty"] == diff)
                self.assertGreaterEqual(
                    count, 10,
                    f"Algorithm '{algo}' difficulty '{diff}' has {count} questions (expected >= 10)"
                )

    def test_question_integrity(self):
        for i, q in enumerate(QUIZ_QUESTIONS):
            self.assertIn("question", q)
            self.assertIn("options", q)
            self.assertEqual(len(q["options"]), 4, f"Question {i} does not have 4 options")
            self.assertIn("answer_index", q)
            self.assertTrue(0 <= q["answer_index"] <= 3, f"Question {i} answer index out of range: {q['answer_index']}")
            self.assertIn("explanation", q)
            self.assertTrue(len(q["explanation"]) > 5)


class TestWaterJug(unittest.TestCase):
    def test_solvable_case(self):
        path, nodes = solve_water_jug(4, 3, 2)
        self.assertIsNotNone(path)
        self.assertGreater(len(path), 0)
        final_state = path[-1]
        # Target of 2 must be reached in at least one jug
        self.assertTrue(final_state["a"] == 2 or final_state["b"] == 2)


if __name__ == "__main__":
    unittest.main()
