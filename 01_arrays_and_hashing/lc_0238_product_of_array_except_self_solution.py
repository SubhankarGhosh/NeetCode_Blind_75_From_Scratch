"""LeetCode 238: Product of Array Except Self (Reference Solution)

Problem URL: https://leetcode.com/problems/product-of-array-except-self/
Difficulty: Medium
Category: Arrays & Hashing

Complexity Analysis:
- Time Complexity: O(n) where n is the length of nums.
  One pass from left-to-right (prefix) and one pass from right-to-left (postfix).
- Space Complexity: O(1) auxiliary space beyond the returned result list.
  No division operations used.
"""

from __future__ import annotations
from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    """Calculates product of array except self using two-pass prefix/postfix in-place multiplication."""
    n = len(nums)
    res = [1] * n

    # Step 1: Prefix products
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    # Step 2: Postfix products multiplied directly into res
    postfix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([2, 3], [3, 2]),
        ([0, 0], [0, 0]),
        ([5], [1]),
    ]

    print("Running verification for lc_0238_product_of_array_except_self_solution.py...")
    for idx, (nums, expected) in enumerate(test_cases, 1):
        result = product_except_self(list(nums))
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
