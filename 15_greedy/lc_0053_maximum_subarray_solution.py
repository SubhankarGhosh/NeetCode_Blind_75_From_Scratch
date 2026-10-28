"""
LeetCode 53: Maximum Subarray
Module: 15_greedy
Difficulty: Medium
Tags: Array, Divide and Conquer, Dynamic Programming, Greedy

PROBLEM DESCRIPTION:
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
    Input: nums = [1]
    Output: 1
    Explanation: The subarray [1] has the largest sum 1.

Example 3:
    Input: nums = [5,4,-1,7,8]
    Output: 23
    Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
    * 1 <= nums.length <= 10^5
    * -10^4 <= nums[i] <= 10^4
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Finds the maximum subarray sum using Kadane's Algorithm.

        Greedy Invariant:
        At every index i, the maximum contiguous subarray sum ending at i is:
            cur_sum = max(nums[i], cur_sum + nums[i])
        Equivalently, whenever cur_sum becomes negative, any future subarray is better
        off starting afresh rather than chaining with a negative prefix.

        Time Complexity:  O(N) - Single linear pass over nums.
        Space Complexity: O(1) - Constant auxiliary storage.
        """
        max_sum = nums[0]
        cur_sum = 0

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            max_sum = max(max_sum, cur_sum)

        return max_sum


def test_max_subarray():
    solver = Solution()

    # Case 1: Standard mixed array -> [4, -1, 2, 1] sum = 6
    assert solver.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, "Case 1 failed"

    # Case 2: Single element
    assert solver.maxSubArray([1]) == 1, "Case 2 failed"

    # Case 3: All positive numbers
    assert solver.maxSubArray([5, 4, -1, 7, 8]) == 23, "Case 3 failed"

    # Case 4: All negative numbers (must pick maximum single element)
    assert solver.maxSubArray([-5, -2, -8, -1]) == -1, "Case 4 failed"

    # Case 5: Two elements
    assert solver.maxSubArray([-2, 1]) == 1, "Case 5 failed"

    print("All solution tests passed successfully!")


if __name__ == "__main__":
    test_max_subarray()
