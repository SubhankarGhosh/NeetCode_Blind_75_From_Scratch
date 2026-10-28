"""
LeetCode 54: Spiral Matrix
Module: 17_math_and_geometry
Difficulty: Medium
Tags: Array, Matrix, Simulation

PROBLEM DESCRIPTION:
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
    Input: matrix = [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ]
    Output: [1,2,3,6,9,8,7,4,5]

Example 2:
    Input: matrix = [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
    * m == matrix.length
    * n == matrix[i].length
    * 1 <= m, n <= 10
    * -100 <= matrix[i][j] <= 100
"""

from typing import List

TODO = None


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Traverses matrix in clockwise spiral order using shrinking boundary pointers.

        Time Complexity:  O(M * N)
        Space Complexity: O(1) auxiliary space (excluding result list)
        """
        res: List[int] = []
        if not matrix or not matrix[0]:
            return res

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while left <= right and top <= bottom:
            # Active Learning:
            # 1. Traverse from left to right along top row
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # 2. Traverse from top to bottom along right column
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # TODO: Guard against single row/column over-traversal
            if not (left <= right and top <= bottom):
                break

            # 3. Traverse from right to left along bottom row
            for col in range(right, left - 1, -1):
                res.append(matrix[bottom][col])
            bottom -= 1

            # 4. Traverse from bottom to top along left column
            for row in range(bottom, top - 1, -1):
                res.append(matrix[row][left])
            left += 1

        return res


def test_spiral_matrix():
    solver = Solution()

    # Case 1: 3x3 square matrix
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert solver.spiralOrder(mat1) == [1, 2, 3, 6, 9, 8, 7, 4, 5], "Case 1 failed"

    # Case 2: 3x4 rectangular matrix
    mat2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert solver.spiralOrder(mat2) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], "Case 2 failed"

    # Case 3: Single element
    assert solver.spiralOrder([[1]]) == [1], "Case 3 failed"

    # Case 4: 1xN single row corridor
    assert solver.spiralOrder([[1, 2, 3, 4]]) == [1, 2, 3, 4], "Case 4 failed"

    # Case 5: Mx1 single column corridor
    assert solver.spiralOrder([[1], [2], [3], [4]]) == [1, 2, 3, 4], "Case 5 failed"

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_spiral_matrix()
