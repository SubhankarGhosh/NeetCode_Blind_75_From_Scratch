"""
LeetCode 746: Min Cost Climbing Stairs
Module: 13_1d_dynamic_programming
Difficulty: Easy
Tags: Array, Dynamic Programming

PROBLEM DESCRIPTION:
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor (index len(cost)).

Example 1:
    Input: cost = [10,15,20]
    Output: 15
    Explanation: You will start at index 1.
    - Pay 15 and climb two steps to reach the top.
    The total cost is 15.

Example 2:
    Input: cost = [1,100,1,1,1,100,1,1,100,1]
    Output: 6
    Explanation: You will start at index 0.
    - Pay 1 and climb two steps to reach index 2.
    - Pay 1 and climb two steps to reach index 4.
    - Pay 1 and climb two steps to reach index 6.
    - Pay 1 and climb one step to reach index 7.
    - Pay 1 and climb two steps to reach index 9.
    - Pay 1 and climb one step to reach the top.
    The total cost is 6.

Constraints:
    * 2 <= cost.length <= 1000
    * 0 <= cost[i] <= 999
"""

from typing import List

TODO = None


class Solution:
    def minCostClimbingStairs(self, cost: List[List[int] | int]) -> int:
        """
        Calculates the minimum cost to reach the top of the staircase.

        Recurrence:
        dp[i] = cost[i] + min(dp[i+1], dp[i+2]) working backwards from the top,
        or moving forward:
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]) for reaching step i.

        Time Complexity:  O(N)
        Space Complexity: O(1) using two variables
        """
        # Active Learning:
        # Let prev2 be the min cost to reach step i - 2, and prev1 to reach step i - 1.
        prev2, prev1 = 0, 0

        for i in range(2, len(cost) + 1):
            # TODO: Transition: curr = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
            curr = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
            prev2 = prev1
            prev1 = curr

        return prev1


def test_min_cost_climbing_stairs():
    solver = Solution()

    # Case 1: 3 steps
    assert solver.minCostClimbingStairs([10, 15, 20]) == 15, "Case 1 failed"

    # Case 2: 10 steps with high cost penalties
    cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    assert solver.minCostClimbingStairs(cost2) == 6, "Case 2 failed"

    # Case 3: Exactly 2 steps
    assert solver.minCostClimbingStairs([0, 0]) == 0, "Case 3 failed"
    assert solver.minCostClimbingStairs([10, 1]) == 1, "Case 4 failed"

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_min_cost_climbing_stairs()
