"""
LeetCode 338: Counting Bits
Module: 18_bit_manipulation
Difficulty: Easy
Tags: Dynamic Programming, Bit Manipulation

PROBLEM DESCRIPTION:
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.

Example 1:
    Input: n = 2
    Output: [0,1,1]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10

Example 2:
    Input: n = 5
    Output: [0,1,1,2,1,2]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10
    3 --> 11
    4 --> 100
    5 --> 101

Constraints:
    * 0 <= n <= 10^5

Follow up:
    * It is very easy to come up with a solution with a runtime of O(n log n). Can you do
      it in linear time O(n) and possibly in a single pass?
    * Can you do it without using any built-in function (like bin(x).count('1'))?
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Calculates set bits for all numbers 0..n in linear O(N) time using DP.

        State Transition (Right Shift Decomposition):
        Notice that right-shifting any number by 1 bit (`i >> 1`) removes its least significant bit.
        The set-bit count of `i` is identical to `dp[i >> 1]`, plus 1 if `i` is odd (`i & 1 == 1`):
            dp[i] = dp[i >> 1] + (i & 1)

        Alternative (Kernighan DP Transition):
        Since `i & (i - 1)` clears the lowest set bit:
            dp[i] = dp[i & (i - 1)] + 1

        Both transitions guarantee O(N) time across a single pass.

        Time Complexity:  O(N) - One constant-time operation per index from 1 to n.
        Space Complexity: O(1) auxiliary space (excluding the returned array).
        """
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


def test_count_bits():
    solver = Solution()

    # Case 1: n = 2 -> [0, 1, 1]
    assert solver.countBits(2) == [0, 1, 1], "Case 1 failed"

    # Case 2: n = 5 -> [0, 1, 1, 2, 1, 2]
    assert solver.countBits(5) == [0, 1, 1, 2, 1, 2], "Case 2 failed"

    # Case 3: n = 0 -> [0]
    assert solver.countBits(0) == [0], "Case 3 failed"

    # Case 4: n = 8 -> powers of 2 have exactly 1 bit
    res4 = solver.countBits(8)
    assert res4[1] == 1 and res4[2] == 1 and res4[4] == 1 and res4[8] == 1, "Case 4 failed"
    assert res4[7] == 3  # 7 = 0b111 -> 3 bits

    print("All solution tests passed successfully!")


if __name__ == "__main__":
    test_count_bits()
