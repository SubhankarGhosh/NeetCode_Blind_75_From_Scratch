"""LeetCode 424: Longest Repeating Character Replacement (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/longest-repeating-character-replacement/
Difficulty: Medium
Category: Sliding Window

Pattern Context:
    Given a string s and an integer k, you can choose up to k characters and replace
    them with any other uppercase English character.
    Sliding Window Invariant:
    - In any window [left, right], the number of characters that need replacement is:
        replacements_needed = (window_length) - (most_frequent_character_count)
    - If `(right - left + 1) - max_f > k`, the window is invalid and must shrink from `left`.
    - Key Optimization: `max_f` does NOT need to be decremented when shrinking because
      a smaller max_f cannot yield a new record window length! This guarantees O(n) runtime.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 03_sliding_window/lc_0424_longest_repeating_character_replacement_compact.py
"""

from __future__ import annotations
from typing import Dict
from collections import defaultdict

# Sentinel placeholder for exercise tasks
TODO = None


def character_replacement(s: str, k: int) -> int:
    """Finds length of longest substring with same letter after at most k replacements.

    Algorithmic Requirements:
    - Time Complexity: O(n) single pass with non-shrinking / monotonic frequency tracking.
    - Space Complexity: O(1) auxiliary space (26 uppercase letters).

    Steps to implement:
    1. Initialize `count = defaultdict(int)`, `max_len = 0`, `max_f = 0`, `left = 0`.
    2. For `right, char` in `enumerate(s)`:
       - `count[char] += 1`
       - `max_f = max(max_f, count[char])`
       - If `(right - left + 1) - max_f > k`:
         * `count[s[left]] -= 1`
         * `left += 1`
       - Update `max_len = max(max_len, right - left + 1)`.
    3. Return `max_len`.

    -------------------------------------------------------------------------
    TODO: Implement the window validity check and shrink logic below.
    -------------------------------------------------------------------------
    """
    count: Dict[str, int] = defaultdict(int)
    max_len = 0
    max_f = 0
    left = 0

    for right, char in enumerate(s):
        count[char] += 1
        max_f = max(max_f, count[char])

        # <<< YOUR CODE HERE >>>
        # Hint: Window is invalid when total replacements needed exceeds k
        is_invalid = TODO  # Replace with: (right - left + 1) - max_f > k
        if is_invalid is None:
            raise NotImplementedError("TODO: Implement window invalidity check.")

        if is_invalid:
            count[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

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

    print("Running verification for lc_0424_longest_repeating_character_replacement_compact.py...")
    for idx, (s, k, expected) in enumerate(test_cases, 1):
        result = character_replacement(s, k)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
