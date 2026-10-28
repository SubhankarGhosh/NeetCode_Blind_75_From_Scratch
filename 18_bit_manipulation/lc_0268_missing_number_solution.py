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


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Finds the missing number using bitwise XOR cancellation.

        Mathematical Invariant:
        Every value in [0, n] should appear in the complete array.
        Because nums has length n, exactly one integer is absent.
        By XORing all indices 0..n-1 with all values nums[0..n-1], alongside value n:
            res = n ^ (0 ^ nums[0]) ^ (1 ^ nums[1]) ^ ... ^ ((n - 1) ^ nums[n - 1])
        Every present number appears twice (once as an index or value n, and once in nums)
        and cancels to 0. The missing number appears only once and survives.

        Why XOR over Gauss Sum (n*(n+1)//2 - sum(nums))?
        While both run in O(N) time and O(1) space, XOR avoids intermediate arithmetic
        overflow in fixed-width 32/64-bit integer environments.

        Time Complexity:  O(N) - Linear pass through nums.
        Space Complexity: O(1) - Constant accumulator storage.
        """
        res = len(nums)
        for i, n in enumerate(nums):
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

    print("All solution tests passed successfully!")


if __name__ == "__main__":
    test_missing_number()
