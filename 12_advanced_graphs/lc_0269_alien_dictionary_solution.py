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


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        Derives the alien alphabet order using Kahn's Algorithm (Topological Sort).

        Key Insights:
        1. Adjacent Word Differences: Lexicographical order is defined by the first differing character
           between adjacent words in the sorted dictionary. Subsequent characters provide no ordering information.
        2. Prefix Invariant: If word A is a prefix of word B, word A MUST appear before word B. If word B
           precedes word A (and len(B) > len(A)), the dictionary is invalid.
        3. DAG Cycle Detection: If the directed graph of character dependencies contains a cycle, no valid
           linear order exists.

        Time Complexity:  O(C) where C is the total number of characters across all words in `words`.
                          Building the adjacency list takes O(C). Topological sort visits at most U <= 26
                          vertices and min(U^2, N-1) edges, which is bounded by O(1).
        Space Complexity: O(1) auxiliary space, since the alphabet is bounded by U <= 26 letters.
        """
        # Step 1: Initialize adjacency list and in-degrees for all unique characters
        adj: Dict[str, Set[str]] = {char: set() for word in words for char in word}
        in_degrees: Dict[str, int] = {char: 0 for char in adj}

        # Step 2: Compare adjacent words to build directed precedence edges
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # Edge Case: Prefix violation (e.g. ["abc", "ab"])
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            # Find the first point of divergence
            for j in range(min_len):
                if w1[j] != w2[j]:
                    c1, c2 = w1[j], w2[j]
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        in_degrees[c2] += 1
                    break

        # Step 3: Kahn's Algorithm (BFS using in-degrees)
        queue = deque([char for char, deg in in_degrees.items() if deg == 0])
        topo_order: List[str] = []

        while queue:
            curr = queue.popleft()
            topo_order.append(curr)

            for neighbor in adj[curr]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: If any characters remain with in-degree > 0, there is a cycle
        if len(topo_order) < len(in_degrees):
            return ""

        return "".join(topo_order)


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

    print("All solution tests passed successfully!")


if __name__ == "__main__":
    test_alien_dictionary()
