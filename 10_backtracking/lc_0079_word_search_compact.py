"""LeetCode 79: Word Search (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/word-search/
Difficulty: Medium
Category: Backtracking

Pattern Context:
    Given an m x n grid of characters and a string word, return True if word exists in the grid.
    The word can be constructed from letters of sequentially adjacent cells, where the same letter
    cell may not be used more than once.

    DFS Grid Backtracking & In-Place State Mutation:
    - Base Case Success: If character index k == len(word), entire word found!
    - Base Case Failure: Out of grid bounds, or board[r][c] != word[k].
    - In-Place Marking: Temporarily set `board[r][c] = '#'` to mark visited without O(MN) set allocations.
    - Exploration: Recurse into 4 orthogonal neighbors (up, down, left, right) for character k + 1.
    - Backtrack: Restore `board[r][c] = word[k]` before returning.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 10_backtracking/lc_0079_word_search_compact.py
"""

from __future__ import annotations
from typing import List
from collections import Counter

# Sentinel placeholder for exercise tasks
TODO = None


def exist(board: List[List[str]], word: str) -> bool:
    """Finds if word exists in grid using DFS backtracking and pruning optimizations.

    Algorithmic Requirements:
    - Time Complexity: O(M * N * 3^L) where L is len(word).
    - Space Complexity: O(L) recursion stack frames.

    Steps to implement:
    1. Early Pruning: Verify board character counts satisfy word counts.
    2. Path Inversion Optimization: If word[-1] is rarer than word[0], reverse word.
    3. Define `dfs(r, c, k)`:
       - If `k == len(word)`: return True.
       - If out of bounds or `board[r][c] != word[k]`: return False.
       - Mark `board[r][c] = '#'`.
       - Recurse in 4 directions for `k + 1`.
       - Restore `board[r][c] = word[k]`.
       - Return True if any branch succeeded.
    4. Call DFS from every matching starting cell.

    -------------------------------------------------------------------------
    TODO: Implement DFS grid backtracking and neighbor exploration below.
    -------------------------------------------------------------------------
    """
    ROWS, COLS = len(board), len(board[0])

    # Optimization 1: Character frequency check
    board_counts = Counter(c for row in board for c in row)
    word_counts = Counter(word)
    for c, count in word_counts.items():
        if board_counts[c] < count:
            return False

    # Optimization 2: Reverse search if tail letter is rarer than head
    if board_counts[word[0]] > board_counts[word[-1]]:
        word = word[::-1]

    def dfs(r: int, c: int, k: int) -> bool:
        if k == len(word):
            return True
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[k]:
            return False

        # Mark cell visited in-place
        board[r][c] = "#"

        # <<< YOUR CODE HERE >>>
        # Hint: Recurse into 4 neighbors (r + dr, c + dc) with index k + 1
        found = False
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # Check if neighbor search succeeds
            if dfs(r + dr, c + dc, k + 1):
                found = True
                break

        # Backtrack: restore original character
        board[r][c] = word[k]

        return found

    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True

    return False


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    board_ex = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]

    test_cases = [
        (board_ex, "ABCCED", True),
        (board_ex, "SEE", True),
        (board_ex, "ABCB", False),
        ([["a"]], "a", True),
        ([["a", "b"], ["c", "d"]], "abcd", False),
        ([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS", True),
    ]

    print("Running verification for lc_0079_word_search_compact.py...")
    for idx, (b_in, w, expected) in enumerate(test_cases, 1):
        b_copy = [row[:] for row in b_in]
        result = exist(b_copy, w)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx} (Word: '{w}')")
    print("All tests passed with 100% success rate!")
