"""
LeetCode 200: Number of Islands
Module: 11_graphs
Difficulty: Medium
Tags: Graph, Breadth-First Search, Depth-First Search, Matrix, Union-Find

PROBLEM DESCRIPTION:
Given an m x n 2D binary grid `grid` which represents a map of '1's (land)
and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are
surrounded by water.

Example 1:
    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1

Example 2:
    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3

Constraints:
    * m == grid.length
    * n == grid[i].length
    * 1 <= m, n <= 300
    * grid[i][j] is '0' or '1'.
"""

from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Calculates the number of connected components of '1's using BFS.
        To avoid mutating the input or exceeding recursion limits on large grids,
        we maintain an explicit visited set (or can mutate a local copy).

        Time Complexity:  O(M * N) - Every cell is visited at most a constant number of times.
        Space Complexity: O(min(M, N)) queue space for BFS; O(M * N) for the visited set.
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(r: int, c: int) -> None:
            queue = deque([(r, c)])
            visited.add((r, c))

            while queue:
                curr_r, curr_c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands


def test_num_islands():
    solver = Solution()

    # Case 1: Single giant island
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert solver.numIslands(grid1) == 1, "Case 1 failed"

    # Case 2: 3 disconnected islands
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert solver.numIslands(grid2) == 3, "Case 2 failed"

    # Case 3: All water
    grid3 = [["0", "0"], ["0", "0"]]
    assert solver.numIslands(grid3) == 0, "Case 3 failed"

    # Case 4: 1x1 island
    grid4 = [["1"]]
    assert solver.numIslands(grid4) == 1, "Case 4 failed"

    # Case 5: Checkerboard pattern (diagonal does not connect)
    grid5 = [
        ["1", "0", "1"],
        ["0", "1", "0"],
        ["1", "0", "1"],
    ]
    assert solver.numIslands(grid5) == 5, "Case 5 failed"

    print("All solution tests passed successfully!")


if __name__ == "__main__":
    test_num_islands()
