"""LeetCode 33: Search in Rotated Sorted Array (Reference Solution)

Problem URL: https://leetcode.com/problems/search-in-rotated-sorted-array/
Difficulty: Medium
Category: Binary Search

Complexity Analysis:
- Time Complexity: O(log n) where n is the length of nums.
  At each iteration, one of the two halves is proven strictly sorted, allowing
  an exact range test that halves the search space in O(1) operations.
- Space Complexity: O(1) auxiliary space as only index pointers are maintained.
"""

from __future__ import annotations
from typing import List


def search(nums: List[int], target: int) -> int:
    """Locates target in rotated sorted array in O(log n) time using sorted-half partition checks."""
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Check if left half is normally sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Otherwise, right half is normally sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([3, 1], 1, 1),
        ([5, 1, 3], 5, 0),
        ([5, 1, 3], 3, 2),
        ([6, 7, 1, 2, 3, 4, 5], 6, 0),
    ]

    print("Running verification for lc_0033_search_in_rotated_sorted_array_solution.py...")
    for idx, (nums, target, expected) in enumerate(test_cases, 1):
        result = search(list(nums), target)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
