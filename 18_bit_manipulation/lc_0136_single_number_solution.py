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


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Finds the unique element using bitwise XOR cancellation.

        Mathematical Invariant:
        Bitwise XOR (^) is commutative and associative:
            x ^ y = y ^ x
            (x ^ y) ^ z = x ^ (y ^ z)
        Every number XOR'd with itself yields 0 (x ^ x = 0), and any number XOR'd with 0
        remains unchanged (x ^ 0 = x).
        Therefore:
            nums[0] ^ nums[1] ^ ... ^ nums[n-1] = (paired terms ^ paired terms) ^ unique_term
                                               = 0 ^ 0 ^ ... ^ unique_term
                                               = unique_term

        Time Complexity:  O(N) - Single linear pass over nums.
        Space Complexity: O(1) - Single accumulator variable.
        """
        res = 0
        for n in nums:
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

    print("All solution tests passed successfully!")


if __name__ == "__main__":
    test_single_number()
