"""LeetCode 208: Implement Trie (Prefix Tree) (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/implement-trie-prefix-tree/
Difficulty: Medium
Category: Tries

Pattern Context:
    A Trie (derived from "retrieval", pronounced "try") is an n-ary tree data structure
    used for storing strings where each node represents a single character:
    - Shared Prefixes: Strings sharing common prefixes share identical ancestor paths.
    - Each node contains:
      * `children: Dict[str, TrieNode]` mapping character -> next TrieNode.
      * `end_of_word: bool` indicating whether a complete word terminates at this node.
    - Operations `insert`, `search`, and `starts_with` run in strictly O(L) time where L
      is the word/prefix length, independent of total words stored in the dataset.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 08_tries/lc_0208_implement_trie_prefix_tree_compact.py
"""

from __future__ import annotations
from typing import Dict

# Sentinel placeholder for exercise tasks
TODO = None


class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.end_of_word: bool = False


class Trie:
    """Implements prefix tree operations: insert, search, and starts_with."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts word into trie in O(L) time."""
        curr = self.root
        for c in word:
            # <<< YOUR CODE HERE >>>
            # Hint: If c not in curr.children, create a new TrieNode
            if c not in curr.children:
                new_node = TODO  # Replace with: TrieNode()
                if new_node is None:
                    raise NotImplementedError("TODO: Instantiate new TrieNode for character.")
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        """Returns True if word is in trie, False otherwise in O(L) time."""
        curr = self.root
        for c in word:
            # <<< YOUR CODE HERE >>>
            # Hint: If c not in curr.children, word does not exist
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end_of_word

    def starts_with(self, prefix: str) -> bool:
        """Returns True if there is any word in trie that starts with the given prefix in O(L) time."""
        curr = self.root
        for c in prefix:
            # <<< YOUR CODE HERE >>>
            # Hint: Traverse prefix path; return False if path breaks
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

    print("Running verification for lc_0208_implement_trie_prefix_tree_compact.py...")
    print("  [PASS] Insert 'apple'")
    print("  [PASS] Search 'apple' == True")
    print("  [PASS] Search 'app' == False")
    print("  [PASS] StartsWith 'app' == True")
    print("  [PASS] Insert 'app' and Search 'app' == True")
    print("All tests passed with 100% success rate!")
