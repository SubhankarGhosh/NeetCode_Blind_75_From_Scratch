"""
LeetCode 269 / LintCode 892: Alien Dictionary
Module: 12_advanced_graphs
Difficulty: Hard
Tags: Array, String, Depth-First Search, Breadth-First Search, Graph, Topological Sort

PROBLEM DESCRIPTION:
There is a new alien language that uses the English alphabet. However, the order
among the letters is unknown to you.

You are given a list of strings `words` from the alien language's dictionary, where
the strings are claimed to be sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in
lexicographically increasing order by the new language's rules. If there is no solution,
return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than string t if at the first letter where they
differ, the letter in s comes before the letter in t in the alien language. If the first
min(s.length, t.length) letters are the same, then s is smaller if and only if
s.length < t.length.

Example 1:
    Input: words = ["wrt","wrf","er","ett","rftt"]
    Output: "wertf"

Example 2:
    Input: words = ["z","x"]
    Output: "zx"

Example 3:
    Input: words = ["z","x","z"]
    Output: ""
    Explanation: The order is invalid because 'z' comes before 'x' and 'x' comes before 'z' (cycle).

Example 4 (Invalid Prefix):
    Input: words = ["abc","ab"]
    Output: ""
    Explanation: "abc" cannot come before "ab" because a prefix must come before a longer word.

Constraints:
    * 1 <= words.length <= 100
    * 1 <= words[i].length <= 100
    * words[i] consists of only lowercase English letters.
"""

from collections import deque
from typing import Dict, List, Set

TODO = None


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        Derives the alien alphabet order using Kahn's Algorithm (Topological Sort).

        Time Complexity:  O(C) where C is the total number of characters across all words.
        Space Complexity: O(1) or O(U + min(U^2, N)) where U <= 26 is the alphabet size.
        """
        # Active Learning:
        # Step 1: Initialize graph with all unique characters in the vocabulary
        adj: Dict[str, Set[str]] = {char: set() for word in words for char in word}
        in_degrees: Dict[str, int] = {char: 0 for char in adj}

        # Step 2: Build directed edges from adjacent word pairs
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # TODO: Check prefix violation (w1 longer than w2, but shares full prefix w2)
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            # Find first differing character
            for j in range(min_len):
                if w1[j] != w2[j]:
                    # Directed edge: w1[j] must precede w2[j]
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degrees[w2[j]] += 1
                    break

        # Step 3: Kahn's Algorithm - Initialize queue with zero in-degree characters
        queue = deque([char for char in in_degrees if in_degrees[char] == 0])
        order: List[str] = []

        # Step 4: Process queue
        while queue:
            curr = queue.popleft()
            order.append(curr)

            for neighbor in adj[curr]:
                # TODO: Decrement in_degrees[neighbor]
                # If in_degrees reaches 0, append neighbor to queue
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        # TODO: Return string order if all unique characters were visited (no cycle), else ""
        if len(order) < len(in_degrees):
            return ""

        return "".join(order)


def validate_alien_order(words: List[str], order: str) -> bool:
    """Verifies that the generated order satisfies all dictionary constraints."""
    if not order:
        return False

    unique_chars = {c for w in words for c in w}
    if set(order) != unique_chars or len(order) != len(unique_chars):
        return False

    char_rank = {c: i for i, c in enumerate(order)}
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if char_rank[c1] > char_rank[c2]:
                    return False
                break
        else:
            if len(w1) > len(w2):
                return False
    return True


def test_alien_dictionary():
    solver = Solution()

    # Case 1: Standard dictionary
    words1 = ["wrt", "wrf", "er", "ett", "rftt"]
    res1 = solver.alienOrder(words1)
    assert validate_alien_order(words1, res1), f"Case 1 failed: got {res1}"

    # Case 2: Simple 2-character order
    words2 = ["z", "x"]
    res2 = solver.alienOrder(words2)
    assert validate_alien_order(words2, res2), f"Case 2 failed: got {res2}"

    # Case 3: Direct cycle (z -> x and x -> z)
    words3 = ["z", "x", "z"]
    assert solver.alienOrder(words3) == "", "Case 3 failed (expected empty string for cycle)"

    # Case 4: Invalid prefix order (longer word precedes prefix)
    words4 = ["abc", "ab"]
    assert solver.alienOrder(words4) == "", "Case 4 failed (expected empty string for invalid prefix)"

    # Case 5: Single character dictionary
    words5 = ["z"]
    assert solver.alienOrder(words5) == "z", "Case 5 failed"

    # Case 6: Disconnected characters
    words6 = ["zy", "zx"]
    res6 = solver.alienOrder(words6)
    assert validate_alien_order(words6, res6), f"Case 6 failed: got {res6}"

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_alien_dictionary()
