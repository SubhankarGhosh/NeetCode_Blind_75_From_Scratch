"""LeetCode 79: Word Search (Reference Solution)

Problem URL: https://leetcode.com/problems/word-search/
Difficulty: Medium
Category: Backtracking

Complexity Analysis:
- Time Complexity: O(M * N * 3^L) where M * N is the board dimension and L is word length.
  From the starting cell, the first step has at most 4 directions, and subsequent steps
  have at most 3 directions (excluding visited predecessor).
  Frequency counting and frequency-based word reversal prune futile searches prior to DFS.
- Space Complexity: O(L) auxiliary space corresponding to the recursion call stack depth.
  Visited tracking is performed in-place on the board without extra hash sets.
"""

from __future__ import annotations
from typing import List
from collections import Counter


def exist(board: List[List[str]], word: str) -> bool:
    """Determines whether word exists in grid via in-place DFS backtracking and heuristic pruning."""
    ROWS, COLS = len(board), len(board[0])

    # Optimization 1: Verify global board character availability
    board_counts = Counter(c for row in board for c in row)
    word_counts = Counter(word)
    for c, count in word_counts.items():
        if board_counts[c] < count:
            return False

    # Optimization 2: Reverse word if start character is more common than end character
    if board_counts[word[0]] > board_counts[word[-1]]:
        word = word[::-1]

    def dfs(r: int, c: int, k: int) -> bool:
        if k == len(word):
            return True
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[k]:
            return False

        # In-place marking
        board[r][c] = "#"

        # Explore 4 orthogonal directions
        found = (
            dfs(r + 1, c, k + 1)
            or dfs(r - 1, c, k + 1)
            or dfs(r, c + 1, k + 1)
            or dfs(r, c - 1, k + 1)
        )

        # Backtrack state
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

    print("Running verification for lc_0079_word_search_solution.py...")
    for idx, (b_in, w, expected) in enumerate(test_cases, 1):
        b_copy = [row[:] for row in b_in]
        result = exist(b_copy, w)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx} (Word: '{w}')")
    print("All tests passed with 100% success rate!")
