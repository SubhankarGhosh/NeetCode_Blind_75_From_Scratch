"""
LeetCode 191: Number of 1 Bits
Module: 18_bit_manipulation
Difficulty: Easy
Tags: Divide and Conquer, Bit Manipulation

PROBLEM DESCRIPTION:
Given a positive integer n, write a function that returns the number of
set bits it has (also known as the Hamming weight).

Example 1:
    Input: n = 11
    Output: 3
    Explanation: The input binary string 1011 has a total of three set bits.

Example 2:
    Input: n = 128
    Output: 1
    Explanation: The input binary string 10000000 has a total of one set bit.

Example 3:
    Input: n = 2147483645
    Output: 30
    Explanation: The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

Constraints:
    * 1 <= n <= 2^31 - 1
"""

TODO = None


class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Counts set bits using Brian Kernighan's Algorithm.

        Bitwise Property:
        n & (n - 1) clears the lowest (least significant) set bit of n.
        Instead of iterating 32 times, the loop executes exactly as many times
        as there are set bits (1s) in n.

        Time Complexity:  O(K) where K is the number of 1-bits (at most 32)
        Space Complexity: O(1)
        """
        count = 0

        # Active Learning:
        # Loop while n > 0
        while n > 0:
            # TODO: Clear lowest set bit: n = n & (n - 1)
            # TODO: Increment count
            n &= n - 1
            count += 1

        return count


def test_hamming_weight():
    solver = Solution()

    # Case 1: 11 (binary 1011) -> 3
    assert solver.hammingWeight(11) == 3, "Case 1 failed"

    # Case 2: 128 (binary 10000000) -> 1
    assert solver.hammingWeight(128) == 1, "Case 2 failed"

    # Case 3: 0 (no set bits)
    assert solver.hammingWeight(0) == 0, "Case 3 failed"

    # Case 4: 7 (binary 111) -> 3
    assert solver.hammingWeight(7) == 3, "Case 4 failed"

    # Case 5: 2^31 - 1 (31 ones)
    assert solver.hammingWeight((1 << 31) - 1) == 31, "Case 5 failed"

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_hamming_weight()
