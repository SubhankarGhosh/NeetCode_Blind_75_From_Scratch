"""
LeetCode 268: Missing Number
Module: 18_bit_manipulation
Difficulty: Easy
Tags: Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting

PROBLEM DESCRIPTION:
Given an array nums containing n distinct numbers in the range [0, n], return the
only number in the range that is missing from the array.

Example 1:
    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
    2 is the missing number in the range since it does not appear in nums.

Example 2:
    Input: nums = [0,1]
    Output: 2
    Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
    2 is the missing number in the range since it does not appear in nums.

Example 3:
    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8
    Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9].
    8 is the missing number in the range since it does not appear in nums.

Constraints:
    * n == nums.length
    * 1 <= n <= 10^4
    * 0 <= nums[i] <= n
    * All the numbers of nums are unique.

Follow up:
    * Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""

from typing import List

TODO = None


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Finds the missing number using bitwise XOR cancellation.

        Bitwise Invariant:
        Every number in range 0..n appears exactly once in the expected sequence,
        and once in nums (except the missing number).
        By computing:
            res = n ^ (0 ^ nums[0]) ^ (1 ^ nums[1]) ^ ... ^ ((n - 1) ^ nums[n - 1])
        all matching numbers annihilate to 0, leaving the missing number.

        Time Complexity:  O(N)
        Space Complexity: O(1)
        """
        res = len(nums)

        # Active Learning:
        # XOR both the index i and the element nums[i]
        for i, n in enumerate(nums):
            # TODO: Accumulate XOR with i and n
            res ^= i ^ n

        return res


def test_missing_number():
    solver = Solution()

    # Case 1: [3, 0, 1] -> 2
    assert solver.missingNumber([3, 0, 1]) == 2, "Case 1 failed"

    # Case 2: [0, 1] -> 2
    assert solver.missingNumber([0, 1]) == 2, "Case 2 failed"

    # Case 3: [9,6,4,2,3,5,7,0,1] -> 8
    assert solver.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8, "Case 3 failed"

    # Case 4: Missing 0 from [1]
    assert solver.missingNumber([1]) == 0, "Case 4 failed"

    # Case 5: Missing last number n
    assert solver.missingNumber([0, 1, 2, 3]) == 4, "Case 5 failed"

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_missing_number()
