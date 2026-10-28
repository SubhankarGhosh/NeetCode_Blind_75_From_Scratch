"""
LeetCode 213: House Robber II
Module: 13_1d_dynamic_programming
Difficulty: Medium
Tags: Array, Dynamic Programming

PROBLEM DESCRIPTION:
You are a professional robber planning to rob houses along a street. Each house has a
certain amount of money stashed. All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one. Meanwhile, adjacent houses
have a security system connected, and it will automatically contact the police if two
adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the
maximum amount of money you can rob tonight without alerting the police.

Example 1:
    Input: nums = [2,3,2]
    Output: 3
    Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
    because they are adjacent houses in a circle.

Example 2:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

Example 3:
    Input: nums = [1,2,3]
    Output: 3

Constraints:
    * 1 <= nums.length <= 100
    * 0 <= nums[i] <= 1000
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Solves circular house robber by reduction to two linear House Robber I subproblems.

        Insight:
        Since house 0 and house n - 1 are adjacent, you can never rob both.
        Therefore, the optimal solution must be either:
        1. Robbing from houses 0 to n - 2 (excluding the last house)
        2. Robbing from houses 1 to n - 1 (excluding the first house)
        Special case: len(nums) == 1, simply return nums[0].

        Time Complexity:  O(N) - Two linear passes over n - 1 elements.
        Space Complexity: O(1) - Two rolling state variables.
        """
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses: List[int]) -> int:
            rob1, rob2 = 0, 0
            for money in houses:
                new_rob = max(rob2, rob1 + money)
                rob1 = rob2
                rob2 = new_rob
            return rob2

        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))


def test_house_robber_ii():
    solver = Solution()

    # Case 1: 3 houses in a circle
    assert solver.rob([2, 3, 2]) == 3, "Case 1 failed"

    # Case 2: 4 houses
    assert solver.rob([1, 2, 3, 1]) == 4, "Case 2 failed"

    # Case 3: 3 ascending houses
    assert solver.rob([1, 2, 3]) == 3, "Case 3 failed"

    # Case 4: Single house
    assert solver.rob([7]) == 7, "Case 4 failed"

    # Case 5: Two houses
    assert solver.rob([1, 2]) == 2, "Case 5 failed"

    print("All solution tests passed successfully!")


if __name__ == "__main__":
    test_house_robber_ii()
