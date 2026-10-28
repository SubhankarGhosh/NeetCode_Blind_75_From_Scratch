"""LeetCode 208: Implement Trie (Prefix Tree) (Reference Solution)

Problem URL: https://leetcode.com/problems/implement-trie-prefix-tree/
Difficulty: Medium
Category: Tries

Complexity Analysis:
- Time Complexity:
  * insert(word): O(L) where L is the length of the string.
  * search(word): O(L) single branch traversal.
  * starts_with(prefix): O(P) where P is prefix length.
- Space Complexity: O(N * L) total memory where N is the total number of words inserted
  and L is average word length. Nodes sharing common prefixes share memory branches.
"""

from __future__ import annotations
from typing import Dict


class TrieNode:
    """Represents a node in the Trie structure."""

    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.end_of_word: bool = False


class Trie:
    """Production-grade prefix tree implementation supporting insertion, exact search, and prefix matching."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts word into the trie, creating nodes for novel prefixes."""
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        """Searches for an exact word match."""
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end_of_word

    def starts_with(self, prefix: str) -> bool:
        """Checks if any previously inserted word begins with the given prefix."""
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")

    assert trie.search("apple") is True, "Expected 'apple' to be found"
    assert trie.search("app") is False, "Expected 'app' not to be found as word"
    assert trie.starts_with("app") is True, "Expected 'app' to be valid prefix"

    trie.insert("app")
    assert trie.search("app") is True, "Expected 'app' to be found after insertion"

    assert trie.search("appl") is False
    assert trie.starts_with("appl") is True
    assert trie.starts_with("b") is False

    print("Running verification for lc_0208_implement_trie_prefix_tree_solution.py...")
    print("  [PASS] Insert 'apple'")
    print("  [PASS] Search 'apple' == True")
    print("  [PASS] Search 'app' == False")
    print("  [PASS] StartsWith 'app' == True")
    print("  [PASS] Insert 'app' and Search 'app' == True")
    print("All tests passed with 100% success rate!")
