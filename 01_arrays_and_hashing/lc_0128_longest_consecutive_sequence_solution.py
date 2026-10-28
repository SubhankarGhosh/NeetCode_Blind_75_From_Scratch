"""LeetCode 128: Longest Consecutive Sequence (Reference Solution)

Problem URL: https://leetcode.com/problems/longest-consecutive-sequence/
Difficulty: Medium
Category: Arrays & Hashing

Complexity Analysis:
- Time Complexity: O(n) where n is the length of nums.
  Converting to a hash set takes O(n).
  Although there is a nested while loop, the inner loop only executes when
  `n - 1 not in num_set` (the start of a sequence). Each number is visited
  at most twice (once in the outer set iteration, once inside a while loop).
  Total operations bounded strictly by 2n = O(n).
- Space Complexity: O(n) auxiliary space to store elements in the hash set.
"""

from __future__ import annotations
from typing import List


def longest_consecutive(nums: List[int]) -> int:
    """Computes the length of the longest consecutive sequence in O(n) time."""
    num_set = set(nums)
    longest = 0

    for n in num_set:
        # Check if n is the start of a consecutive sequence
        if (n - 1) not in num_set:
            length = 1
            while (n + length) in num_set:
                length += 1
            longest = max(longest, length)

    return longest


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
        ([9], 1),
        ([1, 2, 0, 1], 3),
        ([-5, -4, -3, 10, 11, 12, 13, 14], 5),
    ]

    print("Running verification for lc_0128_longest_consecutive_sequence_solution.py...")
    for idx, (nums, expected) in enumerate(test_cases, 1):
        result = longest_consecutive(list(nums))
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
