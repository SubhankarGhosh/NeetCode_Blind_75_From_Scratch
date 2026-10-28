"""
LeetCode 152: Maximum Product Subarray
Module: 13_1d_dynamic_programming
Difficulty: Medium
Tags: Array, Dynamic Programming

PROBLEM DESCRIPTION:
Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.

Example 2:
    Input: nums = [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
    * 1 <= nums.length <= 2 * 10^4
    * -10 <= nums[i] <= 10
    * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

from typing import List

TODO = None


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Finds maximum contiguous subarray product using dynamic programming.

        Key Insight:
        Because negative numbers flip signs, the minimum product can become the
        maximum product when multiplied by a negative number.
        We track both cur_max and cur_min simultaneously.

        Time Complexity:  O(N)
        Space Complexity: O(1)
        """
        res = max(nums)
        cur_min, cur_max = 1, 1

        for n in nums:
            # Active Learning:
            # When multiplied by n, the candidates for the new cur_max and cur_min are:
            # n, n * cur_max, and n * cur_min
            tmp = cur_max * n
            # TODO: Update cur_max = max(n, tmp, n * cur_min)
            # TODO: Update cur_min = min(n, tmp, n * cur_min)
            # TODO: Update res = max(res, cur_max)
            cur_max = max(n, tmp, n * cur_min)
            cur_min = min(n, tmp, n * cur_min)
            res = max(res, cur_max)

        return res


def test_max_product():
    solver = Solution()

    # Case 1: Standard positive subarray [2, 3] -> 6
    assert solver.maxProduct([2, 3, -2, 4]) == 6, "Case 1 failed"

    # Case 2: Zeros separating negative values
    assert solver.maxProduct([-2, 0, -1]) == 0, "Case 2 failed"

    # Case 3: Two negatives multiplying to positive
    assert solver.maxProduct([-2, 3, -4]) == 24, "Case 3 failed"

    # Case 4: Single negative element
    assert solver.maxProduct([-2]) == -2, "Case 4 failed"

    # Case 5: Odd number of negatives
    assert solver.maxProduct([-1, -2, -3]) == 6, "Case 5 failed"

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_max_product()
