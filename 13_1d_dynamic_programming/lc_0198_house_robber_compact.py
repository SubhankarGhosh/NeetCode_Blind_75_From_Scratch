"""
LeetCode 198: House Robber
Module: 13_1d_dynamic_programming
Difficulty: Medium
Tags: Array, Dynamic Programming

PROBLEM DESCRIPTION:
You are a professional robber planning to rob houses along a street. Each house has a
certain amount of money stashed, the only constraint stopping you from robbing each of
them is that adjacent houses have security systems connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the
maximum amount of money you can rob tonight without alerting the police.

Example 1:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

Example 2:
    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
    * 1 <= nums.length <= 100
    * 0 <= nums[i] <= 400
"""

from typing import List

TODO = None


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Calculates maximum loot without robbing adjacent houses.

        Recurrence:
        rob[i] = max(rob[i - 1], rob[i - 2] + nums[i])
        At house i, you either:
        1. Skip house i -> loot is rob[i - 1]
        2. Rob house i -> loot is rob[i - 2] + nums[i]

        Time Complexity:  O(N)
        Space Complexity: O(1) rolling variables
        """
        # Active Learning:
        # rob1: max money robbing from houses up to i - 2
        # rob2: max money robbing from houses up to i - 1
        rob1, rob2 = 0, 0

        for n in nums:
            # TODO: Compute new max loot and roll variables
            new_rob = max(rob2, rob1 + n)
            rob1 = rob2
            rob2 = new_rob

        return rob2


def test_house_robber():
    solver = Solution()

    # Case 1: Standard 4 houses
    assert solver.rob([1, 2, 3, 1]) == 4, "Case 1 failed"

    # Case 2: 5 houses
    assert solver.rob([2, 7, 9, 3, 1]) == 12, "Case 2 failed"

    # Case 3: Single house
    assert solver.rob([5]) == 5, "Case 3 failed"

    # Case 4: Two houses
    assert solver.rob([2, 3]) == 3, "Case 4 failed"

    # Case 5: All zeros
    assert solver.rob([0, 0, 0]) == 0, "Case 5 failed"

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_house_robber()
