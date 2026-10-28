"""LeetCode 153: Find Minimum in Rotated Sorted Array (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Difficulty: Medium
Category: Binary Search

Pattern Context:
    An array sorted in ascending order of unique elements is rotated between 1 and n times.
    To locate the global minimum in O(log n) time:
    - Compare `nums[mid]` against `nums[right]` (the boundary element of the current search space):
      * If `nums[mid] > nums[right]`: the pivot / inflection point (and hence the minimum element)
        must lie strictly in the right subarray `[mid + 1, right]`. Thus `left = mid + 1`.
      * If `nums[mid] <= nums[right]`: the right half is sorted, meaning `nums[mid]` could itself
        be the minimum or the minimum lies to its left. Thus `right = mid`.
    - Terminate when `left == right`, returning `nums[left]`.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 05_binary_search/lc_0153_find_minimum_in_rotated_sorted_array_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def find_min(nums: List[int]) -> int:
    """Finds the minimum element in a rotated sorted array in O(log n) time.

    Algorithmic Requirements:
    - Time Complexity: O(log n) logarithmic reduction of the search window.
    - Space Complexity: O(1) auxiliary space.

    Steps to implement:
    1. Initialize `left = 0`, `right = len(nums) - 1`.
    2. While `left < right`:
       - `mid = (left + right) // 2`.
       - If `nums[mid] > nums[right]`:
         * The minimum lies strictly to the right: `left = mid + 1`.
       - Else:
         * The minimum is at `mid` or to the left: `right = mid`.
    3. Return `nums[left]`.

    -------------------------------------------------------------------------
    TODO: Implement the binary search inflection point logic below.
    -------------------------------------------------------------------------
    """
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # <<< YOUR CODE HERE >>>
        # Hint: Compare nums[mid] with nums[right] to determine which half contains the pivot
        is_pivot_in_right_half = TODO  # Replace with: nums[mid] > nums[right]
        if is_pivot_in_right_half is None:
            raise NotImplementedError("TODO: Check if rotation inflection lies in right half.")

        if is_pivot_in_right_half:
            left = mid + 1
        else:
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

    print("Running verification for lc_0153_find_minimum_in_rotated_sorted_array_compact.py...")
    for idx, (nums, expected) in enumerate(test_cases, 1):
        result = find_min(list(nums))
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
