"""LeetCode 211: Design Add and Search Words Data Structure (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/design-add-and-search-words-data-structure/
Difficulty: Medium
Category: Tries

Pattern Context:
    Design a data structure that supports adding new words and searching for existing words
    with a wildcard dot `.` character that can match any lowercase letter:
    - `addWord(word)`: Standard O(L) Trie insertion.
    - `search(word)`:
      * When character `c != '.'`: standard constant-time hash map lookup.
      * When wildcard `c == '.'`: recursive branch exploration across all existing children
        `child in node.children.values()`. If any branch matches the suffix, return True.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 08_tries/lc_0211_design_add_and_search_words_data_structure_compact.py
"""

from __future__ import annotations
from typing import Dict

# Sentinel placeholder for exercise tasks
TODO = None


class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.end_of_word: bool = False


class WordDictionary:
    """Supports word additions and prefix-tree regex search with '.' wildcards."""

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        """Adds word to trie in O(L) time."""
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        """Searches word with '.' wildcard matching in O(26^d * L) time."""
        def dfs(j: int, node: TrieNode) -> bool:
            curr = node
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    # <<< YOUR CODE HERE >>>
                    # Hint: Recursively try all children in curr.children.values()
                    branch_match = TODO  # Replace with: any(dfs(i + 1, child) for child in curr.children.values())
                    if branch_match is None:
                        raise NotImplementedError("TODO: Implement wildcard dot branch search.")
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.end_of_word

        return dfs(0, self.root)


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    wd = WordDictionary()
    wd.add_word("bad")
    wd.add_word("dad")
    wd.add_word("mad")

    assert wd.search("pad") is False, "pad should not match"
    assert wd.search("bad") is True, "bad should match"
    assert wd.search(".ad") is True, ".ad should match bad/dad/mad"
    assert wd.search("b..") is True, "b.. should match bad"
    assert wd.search("b.d") is True, "b.d should match bad"
    assert wd.search("....") is False, "4 dots should not match 3-letter words"

    print("Running verification for lc_0211_design_add_and_search_words_data_structure_compact.py...")
    print("  [PASS] Add bad, dad, mad")
    print("  [PASS] Search 'pad' == False")
    print("  [PASS] Search 'bad' == True")
    print("  [PASS] Search '.ad' == True")
    print("  [PASS] Search 'b..' == True")
    print("All tests passed with 100% success rate!")
