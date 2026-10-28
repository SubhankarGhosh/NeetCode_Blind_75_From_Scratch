"""LeetCode 33: Search in Rotated Sorted Array (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/search-in-rotated-sorted-array/
Difficulty: Medium
Category: Binary Search

Pattern Context:
    An array sorted in ascending order with distinct values is rotated at an unknown pivot.
    Key Invariant:
    - For any midpoint `mid`, at least ONE half (`[left, mid]` or `[mid, right]`) is GUARANTEED
      to be strictly sorted!
    - We check which half is normally sorted:
      1. If `nums[left] <= nums[mid]` (Left half is sorted):
         - If `nums[left] <= target < nums[mid]`, target must be in left: `right = mid - 1`.
         - Else target must be in right: `left = mid + 1`.
      2. Else (Right half is sorted):
         - If `nums[mid] < target <= nums[right]`, target must be in right: `left = mid + 1`.
         - Else target must be in left: `right = mid - 1`.
    - Guarantees strictly O(log n) time.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 05_binary_search/lc_0033_search_in_rotated_sorted_array_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def search(nums: List[int], target: int) -> int:
    """Searches for target in rotated sorted array in O(log n) time.

    Algorithmic Requirements:
    - Time Complexity: O(log n) halving search space each step.
    - Space Complexity: O(1) auxiliary space.

    Steps to implement:
    1. Initialize `left = 0`, `right = len(nums) - 1`.
    2. While `left <= right`:
       - `mid = (left + right) // 2`.
       - If `nums[mid] == target`, return `mid`.
       - Check if left half is sorted (`nums[left] <= nums[mid]`):
         * If `nums[left] <= target < nums[mid]`: search left (`right = mid - 1`).
         * Else: search right (`left = mid + 1`).
       - Else (right half is sorted):
         * If `nums[mid] < target <= nums[right]`: search right (`left = mid + 1`).
         * Else: search left (`right = mid - 1`).
    3. Return -1 if not found.

    -------------------------------------------------------------------------
    TODO: Implement the sorted half detection and target boundary checks below.
    -------------------------------------------------------------------------
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Determine which half is sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted
            # <<< YOUR CODE HERE >>>
            # Hint: Check if target falls within the sorted left interval [nums[left], nums[mid])
            target_in_left = TODO  # Replace with: nums[left] <= target < nums[mid]
            if target_in_left is None:
                raise NotImplementedError("TODO: Check if target is inside sorted left interval.")

            if target_in_left:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            # <<< YOUR CODE HERE >>>
            # Hint: Check if target falls within the sorted right interval (nums[mid], nums[right]]
            target_in_right = TODO  # Replace with: nums[mid] < target <= nums[right]
            if target_in_right is None:
                raise NotImplementedError("TODO: Check if target is inside sorted right interval.")

            if target_in_right:
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

    print("Running verification for lc_0033_search_in_rotated_sorted_array_compact.py...")
    for idx, (nums, target, expected) in enumerate(test_cases, 1):
        result = search(list(nums), target)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
