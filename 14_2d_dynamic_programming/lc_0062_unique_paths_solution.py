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


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Calculates unique paths using 1D space-optimized dynamic programming.

        Mathematical Invariant:
        Paths to cell (r, c) come exclusively from the cell above (r - 1, c) and the cell to the left (r, c - 1):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        Space Optimization:
        Notice that calculating row r only requires the values of row r - 1 and the current row's left neighbor.
        Thus, we can collapse the entire M x N table into a single 1D array of size min(M, N):
            dp[c] = dp[c] (value from previous row) + dp[c - 1] (value from current row's left cell).

        Time Complexity:  O(M * N) - Computes each grid cell exactly once.
        Space Complexity: O(min(M, N)) - Storing only a single row/column.
        """
        # Optimize space by allocating for the smaller dimension
        if m < n:
            m, n = n, m

        dp = [1] * n

        for r in range(1, m):
            for c in range(1, n):
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

    print("All solution tests passed successfully!")


if __name__ == "__main__":
    test_unique_paths()
