"""LeetCode 15: 3Sum (Reference Solution)

Problem URL: https://leetcode.com/problems/3sum/
Difficulty: Medium
Category: Two Pointers

Complexity Analysis:
- Time Complexity: O(n^2) where n is the length of nums.
  Sorting takes O(n log n).
  The outer loop iterates n times, and the inner two-pointer search takes O(n).
  Overall: O(n log n + n^2) = O(n^2).
- Space Complexity: O(1) auxiliary space (or O(n) depending on Python's Timsort
  internal memory allocation). No extra data structures used for duplicate tracking.
"""

from __future__ import annotations
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """Finds all unique triplets summing to zero in O(n^2) time with sorted two-pointers."""
    res: List[List[int]] = []
    nums.sort()

    for i, a in enumerate(nums):
        # If the smallest number in the triplet is positive, sum cannot be 0
        if a > 0:
            break

        # Skip duplicate values for the first element
        if i > 0 and a == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            three_sum_val = a + nums[left] + nums[right]
            if three_sum_val > 0:
                right -= 1
            elif three_sum_val < 0:
                left += 1
            else:
                res.append([a, nums[left], nums[right]])
                left += 1
                right -= 1

                # Skip duplicate values for the second element
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    return res


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    def normalize_triplets(triplets: List[List[int]]) -> List[List[int]]:
        return sorted([sorted(t) for t in triplets])

    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],
         [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]),
    ]

    print("Running verification for lc_0015_3sum_solution.py...")
    for idx, (nums, expected) in enumerate(test_cases, 1):
        result = three_sum(list(nums))
        norm_res = normalize_triplets(result)
        norm_exp = normalize_triplets(expected)
        assert norm_res == norm_exp, f"Case {idx} failed: got {norm_res}, expected {norm_exp}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
