"""
heuristics.py
-------------
Heuristics for the basic maze problem (Question 6).

A heuristic is a function heuristic(state, problem) that returns an estimate
of the cost of the cheapest path from 'state' to a goal. For a MazeProblem,
'state' is a (row, col) tuple and the goal position is 'problem.goal'.
"""

import math
import util


def _extract_coords(state):
    """
    Safely extracts (row, col) from state whether it is a simple (row, col)
    tuple or a nested structure like ((row, col), keys_tuple).
    """
    if isinstance(state[0], (list, tuple)):
        return state[0][0], state[0][1]
    return state[0], state[1]


def nullHeuristic(state, problem=None):
    """The trivial heuristic: it knows nothing, so it always says 0."""
    return 0


def manhattanHeuristic(state, problem):
    """
    Q6: the Manhattan distance from 'state' to problem.goal:
        |row1 - row2| + |col1 - col2|
    """
    "*** YOUR CODE HERE ***"

    row,col = state
    g_row,g_col = problem.goal

    m_heuristic = abs(row-g_row) + abs(col - g_col)

    return m_heuristic


def euclideanHeuristic(state, problem):
    """
    Q6: the straight-line (Euclidean) distance from 'state' to problem.goal.
    """
    row, col = _extract_coords(state)
    g_row, g_col = _extract_coords(problem.goal)

    sqr = (row - g_row) ** 2 + (col - g_col) ** 2
    return math.sqrt(sqr)