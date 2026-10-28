"""LeetCode 3: Longest Substring Without Repeating Characters (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: Medium
Category: Sliding Window

Pattern Context:
    To find the length of the longest substring without duplicate characters:
    Maintain a sliding window [left, right] where every character within the window
    is strictly unique.
    Using a hash map to store the most recent index of each character:
    - When s[right] has been seen previously at index j >= left, we can instantaneously
      teleport `left = j + 1`, skipping all redundant intermediate window increments.
    - Window length at each step is simply (right - left + 1).

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 03_sliding_window/lc_0003_longest_substring_without_repeating_characters_compact.py
"""

from __future__ import annotations
from typing import Dict

# Sentinel placeholder for exercise tasks
TODO = None


def length_of_longest_substring(s: str) -> int:
    """Finds length of the longest substring without repeating characters.

    Algorithmic Requirements:
    - Time Complexity: O(n) single pass with hash-mapped pointer leaps.
    - Space Complexity: O(min(n, m)) where m is character alphabet size.

    Steps to implement:
    1. Initialize `last_seen = {}` (char -> last observed index), `left = 0`, `max_len = 0`.
    2. For `right, c` in `enumerate(s)`:
       - If `c in last_seen and last_seen[c] >= left`:
         * Update `left = last_seen[c] + 1`.
       - Record `last_seen[c] = right`.
       - Update `max_len = max(max_len, right - left + 1)`.
    3. Return `max_len`.

    -------------------------------------------------------------------------
    TODO: Implement the sliding window character jump logic below.
    -------------------------------------------------------------------------
    """
    last_seen: Dict[str, int] = {}
    left = 0
    max_len = 0

    for right, c in enumerate(s):
        # <<< YOUR CODE HERE >>>
        # Hint: If c was seen within the current window, jump left past it
        if c in last_seen and last_seen[c] >= left:
            new_left = TODO  # Replace with: last_seen[c] + 1
            if new_left is None:
                raise NotImplementedError("TODO: Update left boundary after duplicate.")
            left = new_left

        last_seen[c] = right
        max_len = max(max_len, right - left + 1)

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

    print("Running verification for lc_0003_longest_substring_without_repeating_characters_compact.py...")
    for idx, (s, expected) in enumerate(test_cases, 1):
        result = length_of_longest_substring(s)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
