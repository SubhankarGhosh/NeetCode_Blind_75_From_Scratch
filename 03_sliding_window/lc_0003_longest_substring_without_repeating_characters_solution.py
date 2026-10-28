"""LeetCode 3: Longest Substring Without Repeating Characters (Reference Solution)

Problem URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: Medium
Category: Sliding Window

Complexity Analysis:
- Time Complexity: O(n) where n is the length of string s.
  Each character is visited once by the right pointer. Left pointer jumps forward
  monotonically and never backtracks.
- Space Complexity: O(min(n, m)) where m is the size of the character set
  (e.g., at most 26 for lowercase English, 128 for ASCII).
"""

from __future__ import annotations
from typing import Dict


def length_of_longest_substring(s: str) -> int:
    """Computes longest unique-character substring length using hash-indexed sliding window."""
    last_seen: Dict[str, int] = {}
    left = 0
    max_len = 0

    for right, c in enumerate(s):
        # If character appeared inside the current active window, leap left pointer
        if c in last_seen and last_seen[c] >= left:
            left = last_seen[c] + 1

        last_seen[c] = right
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len

    return max_len


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3),
        ("abba", 2),
    ]

    print("Running verification for lc_0003_longest_substring_without_repeating_characters_solution.py...")
    for idx, (s, expected) in enumerate(test_cases, 1):
        result = length_of_longest_substring(s)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
