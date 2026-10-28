"""
LeetCode 62: Unique Paths
Module: 14_2d_dynamic_programming
Difficulty: Medium
Tags: Math, Dynamic Programming, Combinatorics

PROBLEM DESCRIPTION:
There is a robot on an m x n grid. The robot is initially located at the top-left
corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner
(i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the
robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

Example 1:
    Input: m = 3, n = 7
    Output: 28

Example 2:
    Input: m = 3, n = 2
    Output: 3
    Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Down -> Down
    2. Down -> Down -> Right
    3. Down -> Right -> Down

Constraints:
    * 1 <= m, n <= 100
"""

TODO = None


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Calculates unique paths using 1D space-optimized dynamic programming.

        Recurrence:
        dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        Can be compressed to a single row array of size n:
        dp[c] = dp[c] (from row above) + dp[c - 1] (from left)

        Time Complexity:  O(M * N)
        Space Complexity: O(min(M, N))
        """
        # Ensure n is the smaller dimension for minimum space
        if m < n:
            m, n = n, m

        # Active Learning:
        # dp[c] stores the number of paths to cell in current row at column c
        # The first row is all 1s (only one way to move purely right)
        dp = [1] * n

        for r in range(1, m):
            for c in range(1, n):
                # TODO: Transition: dp[c] = dp[c] (paths from cell above) + dp[c - 1] (paths from left cell)
                dp[c] += dp[c - 1]

        return dp[n - 1]


def test_unique_paths():
    solver = Solution()

    # Case 1: 3x7 grid -> 28
    assert solver.uniquePaths(3, 7) == 28, "Case 1 failed"

    # Case 2: 3x2 grid -> 3
    assert solver.uniquePaths(3, 2) == 3, "Case 2 failed"

    # Case 3: 1x1 grid (already at destination)
    assert solver.uniquePaths(1, 1) == 1, "Case 3 failed"

    # Case 4: 1xN linear corridor
    assert solver.uniquePaths(1, 10) == 1, "Case 4 failed"

    # Case 5: Symmetric grid 3x3 -> 6
    assert solver.uniquePaths(3, 3) == 6, "Case 5 failed"

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_unique_paths()
