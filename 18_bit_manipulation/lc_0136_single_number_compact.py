"""
LeetCode 136: Single Number
Module: 18_bit_manipulation
Difficulty: Easy
Tags: Array, Bit Manipulation

PROBLEM DESCRIPTION:
Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
    Input: nums = [2,2,1]
    Output: 1

Example 2:
    Input: nums = [4,1,2,1,2]
    Output: 4

Example 3:
    Input: nums = [1]
    Output: 1

Constraints:
    * 1 <= nums.length <= 3 * 10^4
    * -3 * 10^4 <= nums[i] <= 3 * 10^4
    * Each element in the array appears twice except for one element which appears only once.
"""

from typing import List

TODO = None


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Finds the unique element using bitwise XOR cancellation.

        Bitwise Invariant:
        1. Self-cancellation: x ^ x = 0
        2. Identity:          x ^ 0 = x
        3. Commutativity:     a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b

        Time Complexity:  O(N)
        Space Complexity: O(1)
        """
        res = 0

        # Active Learning:
        # XOR all elements in nums together; all pairs cancel to 0
        for n in nums:
            # TODO: Accumulate XOR into res
            res ^= n

        return res


def test_single_number():
    solver = Solution()

    # Case 1: [2, 2, 1] -> 1
    assert solver.singleNumber([2, 2, 1]) == 1, "Case 1 failed"

    # Case 2: [4, 1, 2, 1, 2] -> 4
    assert solver.singleNumber([4, 1, 2, 1, 2]) == 4, "Case 2 failed"

    # Case 3: Single element [1] -> 1
    assert solver.singleNumber([1]) == 1, "Case 3 failed"

    # Case 4: Negative numbers [-1, -1, -2] -> -2
    assert solver.singleNumber([-1, -1, -2]) == -2, "Case 4 failed"

    # Case 5: Larger array with duplicates
    assert solver.singleNumber([10, 20, 30, 20, 10]) == 30, "Case 5 failed"

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_single_number()
