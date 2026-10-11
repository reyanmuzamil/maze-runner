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


def nullHeuristic(state, problem=None):
    """The trivial heuristic: it knows nothing, so it always says 0."""

    return 0


def manhattanHeuristic(state, problem):
    """
    Q6: the Manhattan distance from 'state' to problem.goal:
        |row1 - row2| + |col1 - col2|
    """
    "*** YOUR CODE HERE ***"
<<<<<<< HEAD
    row1,col1=state[0],state[1]
    row2,col2=problem.goal[0],problem.goal[1]
    return abs(row1-row2)+abs(col1-col2)
    util.raiseNotDefined()
=======
>>>>>>> b2e2a7cf82c930a63ff73283e46228349035a292

    row,col = state
    g_row,g_col = problem.goal

    m_heuristic = abs(row-g_row) + abs(col - g_col)

    return m_heuristic

def euclideanHeuristic(state, problem):
    """
    Q6: the straight-line (Euclidean) distance from 'state' to problem.goal.
    """
    "*** YOUR CODE HERE ***"
<<<<<<< HEAD
    row1,col1=state[0],state[1]
    row2,col2=problem.goal[0],problem.goal[1]
    return math.sqrt((row1-row2)**2+(col1-col2)**2)
    util.raiseNotDefined()
=======

    row,col = state
    g_row,g_col = problem.goal

    sqr = (row-g_row) ** 2 + (col - g_col) ** 2
    e_heuristic = math.sqrt(sqr)

    return e_heuristic
>>>>>>> b2e2a7cf82c930a63ff73283e46228349035a292
