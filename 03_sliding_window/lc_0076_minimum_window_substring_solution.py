"""LeetCode 76: Minimum Window Substring (Reference Solution)

Problem URL: https://leetcode.com/problems/minimum-window-substring/
Difficulty: Hard
Category: Sliding Window

Complexity Analysis:
- Time Complexity: O(n + m) where n = len(s) and m = len(t).
  Building count_t takes O(m).
  In the worst case, both right and left pointers traverse each character in s
  at most twice, leading to 2n operations = O(n).
  Overall Time: O(n + m).
- Space Complexity: O(k) where k is the number of distinct characters in s and t
  (bounded by 52 for uppercase/lowercase English letters, or O(1) auxiliary space).
"""

from __future__ import annotations
from typing import Dict
from collections import Counter, defaultdict


def min_window(s: str, t: str) -> str:
    """Finds the minimal substring containing all characters of t using an O(n) sliding window."""
    if not t or not s:
        return ""

    count_t = Counter(t)
    window: Dict[str, int] = defaultdict(int)

    have, need = 0, len(count_t)
    res, res_len = [-1, -1], float("inf")
    left = 0

    for right, c in enumerate(s):
        window[c] += 1

        if c in count_t and window[c] == count_t[c]:
            have += 1

        # Contract window from left while all conditions are met
        while have == need:
            window_len = right - left + 1
            if window_len < res_len:
                res = [left, right]
                res_len = window_len

            # Remove character at left from current window
            char_left = s[left]
            window[char_left] -= 1
            if char_left in count_t and window[char_left] < count_t[char_left]:
                have -= 1

            left += 1

    return s[res[0]: res[1] + 1] if res_len != float("inf") else ""


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("ab", "b", "b"),
        ("cabwefgewcwaefgcf", "cae", "cwae"),
        ("aaflslflsldkalskaaa", "aaa", "aaa"),
    ]

    print("Running verification for lc_0076_minimum_window_substring_solution.py...")
    for idx, (s, t, expected) in enumerate(test_cases, 1):
        result = min_window(s, t)
        assert result == expected, f"Case {idx} failed: got {repr(result)}, expected {repr(expected)}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
