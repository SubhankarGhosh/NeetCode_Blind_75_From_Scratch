"""LeetCode 49: Group Anagrams (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/group-anagrams/
Difficulty: Medium
Category: Arrays & Hashing

Pattern Context:
    To group anagrams together, we need a canonical hashable signature for each word:
    1. Method A: Sorted string (e.g. "eat" -> "aet"), running in O(k log k).
    2. Method B: 26-element character frequency tuple (e.g. (1, 0, ..., 1)), running in O(k).
    Since tuple keys in Python are hashable, frequency tuples allow linear-time string hashing.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 01_arrays_and_hashing/lc_0049_group_anagrams_compact.py
"""

from __future__ import annotations
from typing import List, Dict, Tuple
from collections import defaultdict

# Sentinel placeholder for exercise tasks
TODO = None


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Groups strings that are anagrams of each other.

    Algorithmic Requirements:
    - Time Complexity: O(n * k) where n = len(strs) and k is the maximum string length.
    - Space Complexity: O(n * k) to store strings in grouped buckets.

    Steps to implement:
    1. Initialize `groups = defaultdict(list)` where key is a 26-tuple of character counts.
    2. For each string `s` in `strs`:
       - Construct a 26-element count list initialized to 0.
       - Increment count for each character `c` in `s`: `ord(c) - ord('a')`.
       - Convert the count list to an immutable tuple `tuple(count)` to serve as dictionary key.
       - Append `s` to `groups[tuple(count)]`.
    3. Return `list(groups.values())`.

    -------------------------------------------------------------------------
    TODO: Implement the frequency-tuple grouping logic below.
    -------------------------------------------------------------------------
    """
    groups: Dict[Tuple[int, ...], List[str]] = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1

        # <<< YOUR CODE HERE >>>
        # Hint: Convert the list 'count' to a hashable tuple
        key = TODO  # Replace with: tuple(count)
        if key is None:
            raise NotImplementedError("TODO: Create hashable tuple key from count list.")

        groups[key].append(s)

    return list(groups.values())


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    def normalize_groups(res: List[List[str]]) -> List[List[str]]:
        return sorted([sorted(group) for group in res])

    test_cases = [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        (
            [""],
            [[""]],
        ),
        (
            ["a"],
            [["a"]],
        ),
        (
            ["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"],
            [["cab"], ["tin"], ["pew"], ["duh"], ["may"], ["ill"], ["buy"], ["bar"], ["max"], ["doc"]],
        ),
    ]

    print("Running verification for lc_0049_group_anagrams_compact.py...")
    for idx, (strs, expected) in enumerate(test_cases, 1):
        result = group_anagrams(list(strs))
        norm_res = normalize_groups(result)
        norm_exp = normalize_groups(expected)
        assert norm_res == norm_exp, f"Case {idx} failed: got {norm_res}, expected {norm_exp}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
