"""LeetCode 238: Product of Array Except Self (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/product-of-array-except-self/
Difficulty: Medium
Category: Arrays & Hashing

Pattern Context:
    For any index i, product except self is:
        result[i] = (product of elements left of i) * (product of elements right of i)
    Without division, we compute prefix products in a forward pass, then multiply
    accumulated postfix products on a reverse pass directly into the output array,
    achieving O(1) auxiliary space!

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 01_arrays_and_hashing/lc_0238_product_of_array_except_self_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def product_except_self(nums: List[int]) -> List[int]:
    """Computes product of all elements except nums[i] without division in O(1) extra space.

    Algorithmic Requirements:
    - Time Complexity: O(n) two linear passes over nums.
    - Space Complexity: O(1) auxiliary space (output array does not count towards extra space).

    Steps to implement:
    1. Initialize `res = [1] * len(nums)`.
    2. Forward pass: maintain `prefix = 1`.
       For i in range(len(nums)):
       - `res[i] = prefix`
       - Update `prefix *= nums[i]`
    3. Reverse pass: maintain `postfix = 1`.
       For i in range(len(nums) - 1, -1, -1):
       - Multiply `res[i] *= postfix`
       - Update `postfix *= nums[i]`
    4. Return `res`.

    -------------------------------------------------------------------------
    TODO: Implement the prefix and postfix running accumulation below.
    -------------------------------------------------------------------------
    """
    n = len(nums)
    res = [1] * n

    prefix = 1
    for i in range(n):
        res[i] = prefix
        # <<< YOUR CODE HERE >>>
        # Hint: Multiply prefix by nums[i]
        new_prefix = TODO  # Replace with: prefix * nums[i]
        if new_prefix is None:
            raise NotImplementedError("TODO: Update prefix product.")
        prefix = new_prefix

    postfix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= postfix
        # <<< YOUR CODE HERE >>>
        # Hint: Multiply postfix by nums[i]
        new_postfix = TODO  # Replace with: postfix * nums[i]
        if new_postfix is None:
            raise NotImplementedError("TODO: Update postfix product.")
        postfix = new_postfix

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

    print("Running verification for lc_0238_product_of_array_except_self_compact.py...")
    for idx, (nums, expected) in enumerate(test_cases, 1):
        result = product_except_self(list(nums))
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
