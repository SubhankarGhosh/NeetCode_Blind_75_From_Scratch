"""
LeetCode 70: Climbing Stairs
Module: 13_1d_dynamic_programming
Difficulty: Easy
Tags: Math, Dynamic Programming, Memoization

PROBLEM DESCRIPTION:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways
can you climb to the top?

Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top:
    1. 1 step + 1 step
    2. 2 steps

Example 2:
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top:
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

Constraints:
    * 1 <= n <= 45
"""

TODO = None


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculates distinct ways to climb n stairs using dynamic programming.

        Recurrence:
        dp[i] = dp[i - 1] + dp[i - 2]
        Ways to reach step i is sum of ways from step i-1 (1 step) and step i-2 (2 steps).

        Time Complexity:  O(N)
        Space Complexity: O(1) space-optimized with two variables
        """
        if n <= 2:
            return n

        # Active Learning:
        # a represents ways to reach step i - 2
        # b represents ways to reach step i - 1
        a, b = 1, 2

        for _ in range(3, n + 1):
            # TODO: Update a and b to advance one step
            a, b = b, a + b

        return b


def test_climb_stairs():
    solver = Solution()

    # Case 1: Base cases
    assert solver.climbStairs(1) == 1, "Case 1 failed"
    assert solver.climbStairs(2) == 2, "Case 2 failed"

    # Case 2: Small steps
    assert solver.climbStairs(3) == 3, "Case 3 failed"
    assert solver.climbStairs(4) == 5, "Case 4 failed"
    assert solver.climbStairs(5) == 8, "Case 5 failed"

    # Case 3: Larger step count
    assert solver.climbStairs(10) == 89, "Case 6 failed"

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_climb_stairs()
