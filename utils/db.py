"""
SQLite database utilities for the AI Search & Puzzle Solver.

Storage
-------
- solve_history : one row per algorithm run (puzzle or graph search)
- quiz_scores   : one row per completed quiz attempt

Timestamps are stored as UTC ISO-8601 strings and displayed in local time.
"""

import sqlite3
import json
import io
from datetime import datetime, timezone, timedelta
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "history.db"

# ---------------------------------------------------------------------------
# Timezone helpers
# ---------------------------------------------------------------------------

def _utc_now() -> str:
    """Return the current UTC time as an ISO-8601 string."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def _local_display(utc_str: str) -> str:
    """
    Convert a stored UTC timestamp string to local time for display.
    Falls back to the raw string if parsing fails.
    """
    try:
        # Support both 'UTC' suffix and plain strings
        clean = utc_str.replace(" UTC", "").strip()
        dt_utc = datetime.strptime(clean, "%Y-%m-%d %H:%M:%S").replace(
            tzinfo=timezone.utc
        )
        dt_local = dt_utc.astimezone()          # system local tz
        tz_name = dt_local.strftime("%Z")       # e.g. IST, EST, PST
        return dt_local.strftime(f"%Y-%m-%d %H:%M:%S {tz_name}")
    except Exception:
        return utc_str


# ---------------------------------------------------------------------------
# Connection & initialisation
# ---------------------------------------------------------------------------

def get_connection():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Create or migrate tables."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS solve_history (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp    TEXT NOT NULL,
            problem_type TEXT NOT NULL DEFAULT 'puzzle',
            algorithm    TEXT NOT NULL,
            start_state  TEXT NOT NULL,
            goal_state   TEXT NOT NULL,
            moves        INTEGER,
            nodes        INTEGER,
            elapsed      REAL,
            success      INTEGER NOT NULL DEFAULT 0,
            failure_reason TEXT
        )
        """
    )

    # Add problem_type column to existing DBs if missing (migration).
    try:
        cur.execute("ALTER TABLE solve_history ADD COLUMN problem_type TEXT NOT NULL DEFAULT 'puzzle'")
        conn.commit()
    except sqlite3.OperationalError:
        pass  # Column already exists

    # Add failure_reason column if missing.
    try:
        cur.execute("ALTER TABLE solve_history ADD COLUMN failure_reason TEXT")
        conn.commit()
    except sqlite3.OperationalError:
        pass

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS quiz_scores (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp  TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            category   TEXT,
            score      INTEGER NOT NULL,
            total      INTEGER NOT NULL,
            pct        REAL NOT NULL
        )
        """
    )

    # Add category column if missing.
    try:
        cur.execute("ALTER TABLE quiz_scores ADD COLUMN category TEXT")
        conn.commit()
    except sqlite3.OperationalError:
        pass

    conn.commit()
    conn.close()


# ---------------------------------------------------------------------------
# Write helpers
# ---------------------------------------------------------------------------

def record_solve(
    algorithm,
    start_state,
    goal_state,
    moves,
    nodes,
    elapsed,
    success,
    problem_type="puzzle",
    failure_reason=None,
):
    """Insert one algorithm-run record with a UTC timestamp."""
    conn = get_connection()
    conn.execute(
        """
        INSERT INTO solve_history
            (timestamp, problem_type, algorithm, start_state, goal_state,
             moves, nodes, elapsed, success, failure_reason)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            _utc_now(),
            problem_type,
            algorithm,
            json.dumps(list(start_state)),
            json.dumps(list(goal_state)) if goal_state else "",
            moves,
            nodes,
            round(elapsed, 6) if elapsed is not None else None,
            1 if success else 0,
            failure_reason,
        ),
    )
    conn.commit()
    conn.close()


def record_quiz(difficulty, score, total, category="All Categories"):
    """Insert one quiz-score record with a UTC timestamp."""
    pct = round(score / total * 100, 1) if total > 0 else 0.0
    conn = get_connection()
    conn.execute(
        """
        INSERT INTO quiz_scores (timestamp, difficulty, category, score, total, pct)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (_utc_now(), difficulty, category, score, total, pct),
    )
    conn.commit()
    conn.close()


# ---------------------------------------------------------------------------
# Read helpers
# ---------------------------------------------------------------------------

def get_solve_history(limit=200, algorithm=None, problem_type=None, success=None):
    """Return recent solve records as a list of dicts with localised timestamps."""
    conditions = []
    params: list = []

    if algorithm:
        conditions.append("algorithm = ?")
        params.append(algorithm)
    if problem_type:
        conditions.append("problem_type = ?")
        params.append(problem_type)
    if success is not None:
        conditions.append("success = ?")
        params.append(1 if success else 0)

    where = ("WHERE " + " AND ".join(conditions)) if conditions else ""
    params.append(limit)

    conn = get_connection()
    rows = conn.execute(
        f"SELECT * FROM solve_history {where} ORDER BY id DESC LIMIT ?",
        params,
    ).fetchall()
    conn.close()

    records = []
    for r in rows:
        d = dict(r)
        d["timestamp_local"] = _local_display(d["timestamp"])
        records.append(d)
    return records


def get_quiz_scores(limit=100):
    """Return recent quiz score records with localised timestamps."""
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM quiz_scores ORDER BY id DESC LIMIT ?", (limit,)
    ).fetchall()
    conn.close()
    records = []
    for r in rows:
        d = dict(r)
        d["timestamp_local"] = _local_display(d["timestamp"])
        records.append(d)
    return records


def get_stats():
    """Return aggregate statistics for the home dashboard."""
    conn = get_connection()
    puzzles_solved = conn.execute(
        "SELECT COUNT(*) FROM solve_history WHERE success=1"
    ).fetchone()[0]
    algorithms_tested = conn.execute(
        "SELECT COUNT(DISTINCT algorithm) FROM solve_history"
    ).fetchone()[0]
    quiz_attempts = conn.execute(
        "SELECT COUNT(*) FROM quiz_scores"
    ).fetchone()[0]
    conn.close()
    return {
        "puzzles_solved": puzzles_solved,
        "algorithms_tested": algorithms_tested,
        "quiz_attempts": quiz_attempts,
    }


def clear_history():
    """Delete all records from both tables."""
    conn = get_connection()
    conn.execute("DELETE FROM solve_history")
    conn.execute("DELETE FROM quiz_scores")
    conn.commit()
    conn.close()


# ---------------------------------------------------------------------------
# Export helpers
# ---------------------------------------------------------------------------

def export_solve_csv(records) -> bytes:
    """Convert a list of solve-history dicts to UTF-8 CSV bytes."""
    import csv

    fieldnames = [
        "id", "timestamp_local", "problem_type", "algorithm",
        "start_state", "goal_state", "moves", "nodes",
        "elapsed", "success", "failure_reason",
    ]
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()
    for r in records:
        row = dict(r)
        row["success"] = "Yes" if row.get("success") == 1 else "No"
        writer.writerow(row)
    return buf.getvalue().encode("utf-8")


def export_quiz_csv(records) -> bytes:
    """Convert quiz-score dicts to UTF-8 CSV bytes."""
    import csv

    fieldnames = ["id", "timestamp_local", "difficulty", "category", "score", "total", "pct"]
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()
    for r in records:
        writer.writerow(r)
    return buf.getvalue().encode("utf-8")


# Initialise database on import.
init_db()
