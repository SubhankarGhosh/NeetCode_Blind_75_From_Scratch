"""LeetCode 212: Word Search II (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/word-search-ii/
Difficulty: Hard
Category: Tries

Pattern Context:
    Given an m x n board of characters and a list of strings words, return all words
    on the board. Each word must be constructed from letters of sequentially adjacent cells.
    Trie-Pruned 2D Grid Backtracking:
    1. Pre-build a Trie from `words`:
       Store `node.word = word` directly on the terminal node (eliminates string concatenation).
    2. Synchronized DFS Traversal:
       Start DFS from every cell (r, c). If `board[r][c]` is not in `node.children`, prune immediately!
    3. In-Place Visited Marking:
       Temporarily set `board[r][c] = '#'` during exploration; restore on backtrack.
    4. Subtree Pruning Optimization:
       When a leaf node has no children left, remove it from its parent (`parent.children.pop(c)`),
       massively accelerating future board scans.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 08_tries/lc_0212_word_search_ii_compact.py
"""

from __future__ import annotations
from typing import List, Dict, Optional

# Sentinel placeholder for exercise tasks
TODO = None


class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.word: Optional[str] = None


class Trie:
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
    """Finds all words from words list present on the board.

    Algorithmic Requirements:
    - Time Complexity: O(M * N * 4 * 3^(L - 1)) where L is maximum word length.
    - Space Complexity: O(total characters across words) for Trie.

    Steps to implement:
    1. Build Trie from `words`.
    2. Define `dfs(r, c, parent, char)`:
       - If cell out of bounds or `board[r][c] not in parent.children`: return.
       - Node: `curr = parent.children[char]`.
       - If `curr.word`: append to `res`, set `curr.word = None`.
       - Mark `board[r][c] = '#'`.
       - Recurse in 4 directions (up, down, left, right).
       - Restore `board[r][c] = char`.
       - If `len(curr.children) == 0`: `parent.children.pop(char)` (prune dead branch).
    3. Run DFS from all (r, c).
    4. Return `res`.

    -------------------------------------------------------------------------
    TODO: Implement Trie-guided grid backtracking below.
    -------------------------------------------------------------------------
    """
    trie = Trie()
    for w in words:
        trie.add_word(w)

    ROWS, COLS = len(board), len(board[0])
    res: List[str] = []

    def dfs(r: int, c: int, parent: TrieNode, char: str) -> None:
        curr_node = parent.children[char]

        # Match found
        if curr_node.word:
            res.append(curr_node.word)
            curr_node.word = None  # Prevent duplicate matches

        # Mark cell visited
        board[r][c] = "#"

        # Explore 4 orthogonal neighbors
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                next_char = board[nr][nc]
                # <<< YOUR CODE HERE >>>
                # Hint: Check if next_char is a child of curr_node
                has_child = TODO  # Replace with: next_char in curr_node.children
                if has_child is None:
                    raise NotImplementedError("TODO: Check Trie child presence.")
                if has_child:
                    dfs(nr, nc, curr_node, next_char)

        # Backtrack cell state
        board[r][c] = char

        # Optimization: prune leaf nodes to prevent redundant future traversals
        if not curr_node.children:
            parent.children.pop(char)

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

    print("Running verification for lc_0212_word_search_ii_compact.py...")
    for idx, (board_in, words_in, expected) in enumerate(test_cases, 1):
        b_copy = [row[:] for row in board_in]
        result = find_words(b_copy, list(words_in))
        assert set(result) == expected, f"Case {idx} failed: got {set(result)}, expected {expected}"
        print(f"  [PASS] Test Case {idx} (Found {result})")
    print("All tests passed with 100% success rate!")
