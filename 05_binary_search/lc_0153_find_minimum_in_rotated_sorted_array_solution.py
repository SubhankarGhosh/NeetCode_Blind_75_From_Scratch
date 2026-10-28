"""LeetCode 153: Find Minimum in Rotated Sorted Array (Reference Solution)

Problem URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Difficulty: Medium
Category: Binary Search

Complexity Analysis:
- Time Complexity: O(log n) where n is the length of nums.
  At each iteration, the search interval [left, right] is halved.
- Space Complexity: O(1) auxiliary space as only index pointers are maintained.
"""

from __future__ import annotations
from typing import List


def find_min(nums: List[int]) -> int:
    """Locates the minimum element in O(log n) time using binary search on rotation pivot."""
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # If mid element is strictly greater than right element,
        # the rotation drop-off must lie strictly to the right of mid.
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Otherwise, the minimum lies at mid or to the left of mid.
            right = mid

    return nums[left]


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        ([2, 1], 1),
        ([1], 1),
        ([3, 1, 2], 1),
        ([5, 1, 2, 3, 4], 1),
    ]

    print("Running verification for lc_0153_find_minimum_in_rotated_sorted_array_solution.py...")
    for idx, (nums, expected) in enumerate(test_cases, 1):
        result = find_min(list(nums))
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
