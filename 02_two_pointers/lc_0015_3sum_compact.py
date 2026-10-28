"""LeetCode 15: 3Sum (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/3sum/
Difficulty: Medium
Category: Two Pointers

Pattern Context:
    The 3Sum problem reduces to 2Sum-II (Sorted Array) across n steps:
    1. Sort the input array in O(n log n).
    2. Fix the first element nums[i].
    3. Use two converging pointers (left = i + 1, right = len(nums) - 1) to find
       pairs that satisfy: nums[left] + nums[right] == -nums[i].
    4. Duplicate Handling:
       - Skip identical values of nums[i] when i > 0.
       - Upon finding a valid triplet, advance `left` and skip subsequent identical numbers.
    5. Early Pruning: If nums[i] > 0, three positive numbers cannot sum to 0; break immediately!

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 02_two_pointers/lc_0015_3sum_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def three_sum(nums: List[int]) -> List[List[int]]:
    """Finds all unique triplets [nums[i], nums[j], nums[k]] that sum to 0.

    Algorithmic Requirements:
    - Time Complexity: O(n^2) where n = len(nums).
    - Space Complexity: O(1) auxiliary space (excluding output and sort overhead).

    Steps to implement:
    1. Sort `nums` in ascending order.
    2. Iterate `i` from 0 to len(nums) - 1:
       - Early exit: If `nums[i] > 0`, break.
       - Duplicate check: If `i > 0 and nums[i] == nums[i - 1]`, continue.
       - Set `left = i + 1`, `right = len(nums) - 1`.
       - While `left < right`:
         * `total = nums[i] + nums[left] + nums[right]`.
         * If `total > 0`, decrement `right -= 1`.
         * If `total < 0`, increment `left += 1`.
         * If `total == 0`:
           - Append `[nums[i], nums[left], nums[right]]` to `res`.
           - Increment `left += 1`, decrement `right -= 1`.
           - While `left < right and nums[left] == nums[left - 1]`, increment `left += 1`.
    3. Return `res`.

    -------------------------------------------------------------------------
    TODO: Implement the two-pointer triplet search logic below.
    -------------------------------------------------------------------------
    """
    res: List[List[int]] = []
    nums.sort()

    for i, a in enumerate(nums):
        if a > 0:
            break
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

                # <<< YOUR CODE HERE >>>
                # Hint: Skip duplicate left values while left < right
                while left < right and nums[left] == nums[left - 1]:
                    should_advance = TODO  # Replace with: True
                    if should_advance is None:
                        raise NotImplementedError("TODO: Skip duplicate values for pointer left.")
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

    print("Running verification for lc_0015_3sum_compact.py...")
    for idx, (nums, expected) in enumerate(test_cases, 1):
        result = three_sum(list(nums))
        norm_res = normalize_triplets(result)
        norm_exp = normalize_triplets(expected)
        assert norm_res == norm_exp, f"Case {idx} failed: got {norm_res}, expected {norm_exp}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
