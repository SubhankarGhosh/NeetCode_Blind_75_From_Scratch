"""LeetCode 49: Group Anagrams (Reference Solution)

Problem URL: https://leetcode.com/problems/group-anagrams/
Difficulty: Medium
Category: Arrays & Hashing

Complexity Analysis:
- Time Complexity: O(n * k) where n is the number of strings and k is the maximum
  string length. Counting characters takes O(k) per string, avoiding the O(k log k)
  overhead of string sorting.
- Space Complexity: O(n * k) to store all strings categorized into hash table lists.
"""

from __future__ import annotations
from typing import List, Dict, Tuple
from collections import defaultdict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Groups anagrams using a 26-element character count tuple as the hash map key."""
    groups: Dict[Tuple[int, ...], List[str]] = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        groups[tuple(count)].append(s)

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

    print("Running verification for lc_0049_group_anagrams_solution.py...")
    for idx, (strs, expected) in enumerate(test_cases, 1):
        result = group_anagrams(list(strs))
        norm_res = normalize_groups(result)
        norm_exp = normalize_groups(expected)
        assert norm_res == norm_exp, f"Case {idx} failed: got {norm_res}, expected {norm_exp}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
