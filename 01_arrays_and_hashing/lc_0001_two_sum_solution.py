"""LeetCode 1: Two Sum (Reference Solution)

Problem URL: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Category: Arrays & Hashing

Complexity Analysis:
- Time Complexity: O(n) where n is the length of nums.
  A single linear traversal with O(1) hash map lookups and insertions.
- Space Complexity: O(n) auxiliary space to store visited elements in the hash map.
"""

from __future__ import annotations
from typing import List, Dict


def two_sum(nums: List[int], target: int) -> List[int]:
    """Finds indices of the two numbers that add up to target using a one-pass hash map."""
    prev_map: Dict[int, int] = {}  # value -> index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i

    return []


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([0, 4, 3, 0], 0, [0, 3]),
    ]

    print("Running verification for lc_0001_two_sum_solution.py...")
    for idx, (nums, target, expected) in enumerate(test_cases, 1):
        result = two_sum(list(nums), target)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
