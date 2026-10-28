"""
LeetCode 417: Pacific Atlantic Water Flow
Module: 11_graphs
Difficulty: Medium
Tags: Array, Depth-First Search, Breadth-First Search, Matrix

PROBLEM DESCRIPTION:
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches
the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix
`heights` where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly
north, south, east, and west if the neighboring cell's height is less than or equal to the
current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water
can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
    Input: heights = [
      [1,2,2,3,5],
      [3,2,3,4,4],
      [2,4,5,3,1],
      [6,7,1,4,5],
      [5,1,1,2,4]
    ]
    Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example 2:
    Input: heights = [[1]]
    Output: [[0,0]]

Constraints:
    * m == heights.length
    * n == heights[r].length
    * 1 <= m, n <= 200
    * 0 <= heights[r][c] <= 10^5
"""

from collections import deque
from typing import List, Set, Tuple


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Multi-source reverse BFS starting from coastal boundaries uphill.
        Instead of simulating downhill flow from each of the M*N cells, we start from the
        coastal boundary cells of Pacific and Atlantic and flow 'uphill' (heights[nr][nc] >= heights[r][c]).

        Time Complexity:  O(M * N) - Each cell is visited at most once per ocean.
        Space Complexity: O(M * N) - Space for the visited sets and queues.
        """
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pac_visited: Set[Tuple[int, int]] = set()
        atl_visited: Set[Tuple[int, int]] = set()

        pac_queue = deque()
        atl_queue = deque()

        # Left / Right boundaries
        for r in range(rows):
            pac_queue.append((r, 0))
            pac_visited.add((r, 0))
            atl_queue.append((r, cols - 1))
            atl_visited.add((r, cols - 1))

        # Top / Bottom boundaries
        for c in range(cols):
            if (0, c) not in pac_visited:
                pac_queue.append((0, c))
                pac_visited.add((0, c))
            if (rows - 1, c) not in atl_visited:
                atl_queue.append((rows - 1, c))
                atl_visited.add((rows - 1, c))

        def bfs(queue: deque, visited: Set[Tuple[int, int]]) -> None:
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while queue:
                curr_r, curr_c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[curr_r][curr_c]
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        bfs(pac_queue, pac_visited)
        bfs(atl_queue, atl_visited)

        # Cells reachable by both oceans
        common_cells = pac_visited & atl_visited
        return [list(coord) for coord in sorted(common_cells)]


def test_pacific_atlantic():
    solver = Solution()

    # Case 1: Standard 5x5 mountain grid
    heights1 = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    expected1 = sorted([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]])
    assert sorted(solver.pacificAtlantic(heights1)) == expected1, "Case 1 failed"

    # Case 2: 1x1 island
    heights2 = [[1]]
    assert solver.pacificAtlantic(heights2) == [[0, 0]], "Case 2 failed"

    # Case 3: Flat 2x2 plateau
    heights3 = [[2, 2], [2, 2]]
    expected3 = sorted([[0, 0], [0, 1], [1, 0], [1, 1]])
    assert sorted(solver.pacificAtlantic(heights3)) == expected3, "Case 3 failed"

    print("All solution tests passed successfully!")


if __name__ == "__main__":
    test_pacific_atlantic()
