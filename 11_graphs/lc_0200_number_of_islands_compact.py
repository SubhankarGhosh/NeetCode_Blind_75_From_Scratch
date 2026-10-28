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

TODO = None


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Calculates the number of connected components of '1's.

        Time Complexity:  O(M * N) where M is rows and N is cols
        Space Complexity: O(M * N) worst case for visited set / recursion stack / queue
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r: int, c: int) -> None:
            # Active Learning: Implement BFS queue traversal to mark all connected '1's
            queue = deque([(r, c)])
            visited.add((r, c))
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while queue:
                curr_r, curr_c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc
                    # TODO: Check boundary, land condition ('1'), and not visited
                    # Then add to visited and append to queue
                    pass

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    # TODO: Trigger BFS or DFS traversal and increment islands
                    pass

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

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_num_islands()
