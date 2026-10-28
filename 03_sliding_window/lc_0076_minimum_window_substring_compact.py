"""LeetCode 76: Minimum Window Substring (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/minimum-window-substring/
Difficulty: Hard
Category: Sliding Window

Pattern Context:
    Given two strings s and t, find the minimum window substring of s such that every
    character in t (including duplicates) is included in the window.
    Sliding Window with State Tracking:
    - Instead of re-verifying the entire character map in O(26) each step, we maintain
      two scalar counters:
        * `need = len(count_t)`: number of distinct characters in t to satisfy.
        * `have`: number of distinct characters currently meeting their frequency requirement.
    - When `have == need`, the window is valid: record the minimum window, then shrink
      from `left` to minimize length until `have < need`.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 03_sliding_window/lc_0076_minimum_window_substring_compact.py
"""

from __future__ import annotations
from typing import Dict
from collections import Counter, defaultdict

# Sentinel placeholder for exercise tasks
TODO = None


def min_window(s: str, t: str) -> str:
    """Finds the minimum window in s containing all characters of t in O(n) time.

    Algorithmic Requirements:
    - Time Complexity: O(n + m) where n = len(s) and m = len(t).
    - Space Complexity: O(k) where k is the count of unique characters in s and t.

    Steps to implement:
    1. If `t == ""`, return `""`.
    2. Build `count_t = Counter(t)`, initialize `window = defaultdict(int)`.
    3. Initialize `have = 0`, `need = len(count_t)`, `res = [-1, -1]`, `res_len = float("inf")`, `left = 0`.
    4. For `right, c` in `enumerate(s)`:
       - `window[c] += 1`
       - If `c in count_t and window[c] == count_t[c]`:
         * `have += 1`
       - While `have == need`:
         * Update result if `(right - left + 1) < res_len`.
         * Shrink window: `window[s[left]] -= 1`.
         * If `s[left] in count_t and window[s[left]] < count_t[s[left]]`:
           - `have -= 1`
         * `left += 1`
    5. Return `s[res[0] : res[1] + 1]` if `res_len != float("inf")` else `""`.

    -------------------------------------------------------------------------
    TODO: Implement the window shrinking and match-count logic below.
    -------------------------------------------------------------------------
    """
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

        # While window satisfies all character constraints, minimize it
        while have == need:
            # Update best recorded window
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1

            # <<< YOUR CODE HERE >>>
            # Hint: Pop character at s[left] from window and decrement have if condition violated
            char_left = s[left]
            window[char_left] -= 1

            is_deficit = TODO  # Replace with: char_left in count_t and window[char_left] < count_t[char_left]
            if is_deficit is None:
                raise NotImplementedError("TODO: Check if removing s[left] creates character deficit.")

            if is_deficit:
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

    print("Running verification for lc_0076_minimum_window_substring_compact.py...")
    for idx, (s, t, expected) in enumerate(test_cases, 1):
        result = min_window(s, t)
        assert result == expected, f"Case {idx} failed: got {repr(result)}, expected {repr(expected)}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
