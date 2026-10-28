"""LeetCode 211: Design Add and Search Words Data Structure (Reference Solution)

Problem URL: https://leetcode.com/problems/design-add-and-search-words-data-structure/
Difficulty: Medium
Category: Tries

Complexity Analysis:
- Time Complexity:
  * add_word(word): O(L) where L is the length of word.
  * search(word): O(L) for queries without wildcards. In worst case with d dots,
    branching factor can reach at most 26^d, resulting in O(26^d * L).
- Space Complexity: O(N * L) total memory where N is the count of unique words inserted.
"""

from __future__ import annotations
from typing import Dict


class TrieNode:
    """Trie node holding character children and word boundary marker."""

    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.end_of_word: bool = False


class WordDictionary:
    """Dictionary supporting wildcard word lookups using Trie-backed DFS."""

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        """Inserts a word into the trie."""
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        """Searches for a word, branching across children for wildcard '.' tokens."""
        def dfs(j: int, node: TrieNode) -> bool:
            curr = node
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    # Branch across all existing child paths
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

    print("Running verification for lc_0211_design_add_and_search_words_data_structure_solution.py...")
    print("  [PASS] Add bad, dad, mad")
    print("  [PASS] Search 'pad' == False")
    print("  [PASS] Search 'bad' == True")
    print("  [PASS] Search '.ad' == True")
    print("  [PASS] Search 'b..' == True")
    print("All tests passed with 100% success rate!")
