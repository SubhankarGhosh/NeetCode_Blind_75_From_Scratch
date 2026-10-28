"""LeetCode 212: Word Search II (Reference Solution)

Problem URL: https://leetcode.com/problems/word-search-ii/
Difficulty: Hard
Category: Tries

Complexity Analysis:
- Time Complexity: O(M * N * 4 * 3^(L - 1)) where M * N is the number of cells on the board
  and L is the maximum word length. Starting from any cell, the first step has at most 4
  directions, and subsequent steps have at most 3 directions (avoiding immediate parent).
  Trie-guided pruning terminates unpromising branches early, making execution orders of
  magnitude faster than naive DFS per word (O(W * M * N * 4^L)).
- Space Complexity: O(total characters across words) to store the prefix tree.
"""

from __future__ import annotations
from typing import List, Dict, Optional


class TrieNode:
    """Trie node holding next character references and full word terminal payload."""

    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.word: Optional[str] = None


class Trie:
    """Prefix tree optimized for multi-word grid matching."""

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = word


def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    """Finds all words in board using Trie-guided DFS with dynamic branch pruning."""
    trie = Trie()
    for w in words:
        trie.add_word(w)

    ROWS, COLS = len(board), len(board[0])
    res: List[str] = []

    def dfs(r: int, c: int, parent: TrieNode, char: str) -> None:
        curr_node = parent.children[char]

        # Terminal word match
        if curr_node.word:
            res.append(curr_node.word)
            curr_node.word = None  # Deduplicate multiple path discoveries of same word

        # Mark cell as visited in-place
        board[r][c] = "#"

        # Explore orthogonal neighbors
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                next_char = board[nr][nc]
                if next_char in curr_node.children:
                    dfs(nr, nc, curr_node, next_char)

        # Restore cell value on backtrack
        board[r][c] = char

        # Dynamic Trie Pruning: remove dead leaf nodes from parent map
        if not curr_node.children:
            parent.children.pop(char)

    # Launch DFS from every valid starting cell
    for r in range(ROWS):
        for c in range(COLS):
            char = board[r][c]
            if char in trie.root.children:
                dfs(r, c, trie.root, char)

    return res


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
            {"eat", "oath"},
        ),
        (
            [["a", "b"], ["c", "d"]],
            ["abcb"],
            set(),
        ),
        (
            [["a"]],
            ["a"],
            {"a"},
        ),
        (
            [
                ["a", "b", "c"],
                ["a", "e", "d"],
                ["a", "f", "g"],
            ],
            ["abcdefg", "gfedcba", "eaabcd"],
            {"abcdefg", "gfedcba", "eaabcd"},
        ),
    ]

    print("Running verification for lc_0212_word_search_ii_solution.py...")
    for idx, (board_in, words_in, expected) in enumerate(test_cases, 1):
        b_copy = [row[:] for row in board_in]
        result = find_words(b_copy, list(words_in))
        assert set(result) == expected, f"Case {idx} failed: got {set(result)}, expected {expected}"
        print(f"  [PASS] Test Case {idx} (Found {result})")
    print("All tests passed with 100% success rate!")
