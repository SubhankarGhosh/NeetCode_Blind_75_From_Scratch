"""
LeetCode 73: Set Matrix Zeroes
Module: 17_math_and_geometry
Difficulty: Medium
Tags: Array, Hash Table, Matrix

PROBLEM DESCRIPTION:
Given an m x n integer matrix matrix, if an element is 0, set its entire row
and column to 0's.

You must do it in place.

Example 1:
    Input: matrix = [
      [1,1,1],
      [1,0,1],
      [1,1,1]
    ]
    Output: [
      [1,0,1],
      [0,0,0],
      [1,0,1]
    ]

Example 2:
    Input: matrix = [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    Output: [
      [0,0,0,0],
      [0,4,5,0],
      [0,3,1,0]
    ]

Constraints:
    * m == matrix.length
    * n == matrix[0].length
    * 1 <= m, n <= 200
    * -2^31 <= matrix[i][j] <= 2^31 - 1

Follow up:
    * A straightforward solution using O(mn) space is probably a bad idea.
    * A simple improvement uses O(m + n) space, but still not the best solution.
    * Could you devise a constant space solution?
"""

from typing import List

TODO = None


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Sets rows and columns to zero in-place using O(1) auxiliary space.

        Strategy:
        Use the first row (matrix[0][c]) and first column (matrix[r][0]) as marker arrays.
        Since cell (0, 0) represents the intersection, use a single boolean `row_zero`
        to track whether the first row itself needs to be zeroed out.

        Time Complexity:  O(M * N)
        Space Complexity: O(1) in-place
        """
        rows, cols = len(matrix), len(matrix[0])
        row_zero = False

        # Active Learning:
        # Step 1: Scan matrix and mark zeros in first row and first column
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero = True

        # Step 2: Fill inner cells (r: 1 -> rows - 1, c: 1 -> cols - 1)
        for r in range(1, rows):
            for c in range(1, cols):
                # TODO: Check if row r or col c was marked
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Step 3: Zero out first column if matrix[0][0] was marked
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # Step 4: Zero out first row if row_zero flag is set
        if row_zero:
            for c in range(cols):
                matrix[0][c] = 0


def test_set_matrix_zeroes():
    solver = Solution()

    # Case 1: 3x3 matrix with center zero
    mat1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    solver.setZeroes(mat1)
    assert mat1 == [[1, 0, 1], [0, 0, 0], [1, 0, 1]], f"Case 1 failed: {mat1}"

    # Case 2: 3x4 matrix with multiple zeros
    mat2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    solver.setZeroes(mat2)
    expected2 = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    assert mat2 == expected2, f"Case 2 failed: {mat2}"

    # Case 3: Single element
    mat3 = [[0]]
    solver.setZeroes(mat3)
    assert mat3 == [[0]], "Case 3 failed"

    # Case 4: No zeros present
    mat4 = [[1, 2], [3, 4]]
    solver.setZeroes(mat4)
    assert mat4 == [[1, 2], [3, 4]], "Case 4 failed"

    # Case 5: Zero in first row and first col
    mat5 = [[0, 1], [1, 1]]
    solver.setZeroes(mat5)
    assert mat5 == [[0, 0], [0, 1]], f"Case 5 failed: {mat5}"

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_set_matrix_zeroes()
