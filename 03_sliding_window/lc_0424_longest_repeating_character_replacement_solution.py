"""LeetCode 424: Longest Repeating Character Replacement (Reference Solution)

Problem URL: https://leetcode.com/problems/longest-repeating-character-replacement/
Difficulty: Medium
Category: Sliding Window

Complexity Analysis:
- Time Complexity: O(n) where n is the length of string s.
  Each pointer moves monotonically from left to right. Because max_f is not
  recalculated upon shrinking, each character is processed in strictly O(1) time.
- Space Complexity: O(1) auxiliary space (at most 26 entries for uppercase English letters).
"""

from __future__ import annotations
from typing import Dict
from collections import defaultdict


def character_replacement(s: str, k: int) -> int:
    """Finds maximum uniform substring length achievable with at most k replacements."""
    count: Dict[str, int] = defaultdict(int)
    max_len = 0
    max_f = 0
    left = 0

    for right, char in enumerate(s):
        count[char] += 1
        if count[char] > max_f:
            max_f = count[char]

        # If current window requires more than k replacements, shrink from left
        while (right - left + 1) - max_f > k:
            count[s[left]] -= 1
            left += 1

        window_len = right - left + 1
        if window_len > max_len:
            max_len = window_len

    return max_len


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("AAAA", 2, 4),
        ("ABCDE", 1, 2),
        ("BAAA", 0, 3),
        ("ABBB", 2, 4),
    ]

    print("Running verification for lc_0424_longest_repeating_character_replacement_solution.py...")
    for idx, (s, k, expected) in enumerate(test_cases, 1):
        result = character_replacement(s, k)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
