"""
LeetCode 48: Rotate Image
Module: 17_math_and_geometry
Difficulty: Medium
Tags: Array, Math, Matrix

PROBLEM DESCRIPTION:
You are given an n x n 2D matrix representing an image, rotate the image
by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D
matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
    Input: matrix = [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ]
    Output: [
      [7,4,1],
      [8,5,2],
      [9,6,3]
    ]

Example 2:
    Input: matrix = [
      [ 5, 1, 9,11],
      [ 2, 4, 8,10],
      [13, 3, 6, 7],
      [15,14,12,16]
    ]
    Output: [
      [15,13, 2, 5],
      [14, 3, 4, 1],
      [12, 6, 8, 9],
      [16, 7,10,11]
    ]

Constraints:
    * n == matrix.length == matrix[i].length
    * 1 <= n <= 20
    * -1000 <= matrix[i][j] <= 1000
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotates the n x n matrix 90 degrees clockwise in-place.

        Linear Algebra Decomposition:
        A 90-degree clockwise rotation R_90 can be decomposed into:
            R_90 = Horizontal Reflection o Transpose
        1. Transpose: matrix[i][j] <-> matrix[j][i] reflects elements along the main diagonal.
        2. Horizontal Reflection: Reversing each row inverts column coordinates (matrix[i][j] <-> matrix[i][n - 1 - j]).
        Together: (r, c) -> (c, r) -> (c, n - 1 - r), which is the exact mapping of a 90-degree rotation.

        Time Complexity:  O(N^2) - Transpose visits N*(N-1)/2 pairs; reversal visits N*N/2 pairs.
        Space Complexity: O(1) - Pure in-place coordinate swaps.
        """
        n = len(matrix)

        # Step 1: Transpose matrix across the main diagonal
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each individual row horizontally
        for row in matrix:
            row.reverse()


def test_rotate_image():
    solver = Solution()

    # Case 1: 3x3 matrix
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solver.rotate(mat1)
    assert mat1 == [[7, 4, 1], [8, 5, 2], [9, 6, 3]], f"Case 1 failed: {mat1}"

    # Case 2: 4x4 matrix
    mat2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16],
    ]
    expected2 = [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11],
    ]
    solver.rotate(mat2)
    assert mat2 == expected2, f"Case 2 failed: {mat2}"

    # Case 3: 1x1 matrix
    mat3 = [[1]]
    solver.rotate(mat3)
    assert mat3 == [[1]], "Case 3 failed"

    # Case 4: 2x2 matrix
    mat4 = [[1, 2], [3, 4]]
    solver.rotate(mat4)
    assert mat4 == [[3, 1], [4, 2]], f"Case 4 failed: {mat4}"

    print("All solution tests passed successfully!")


if __name__ == "__main__":
    test_rotate_image()
