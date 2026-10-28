"""
LeetCode 190: Reverse Bits
Module: 18_bit_manipulation
Difficulty: Easy
Tags: Divide and Conquer, Bit Manipulation

PROBLEM DESCRIPTION:
Reverse bits of a given 32 bits unsigned integer.

Note:
- Note that in some languages, such as Java, there is no unsigned integer type. In this case,
  both input and output will be given as a signed integer type. They should not affect your
  implementation, as the integer's internal binary representation is the same, whether it is
  signed or unsigned.
- In Java, the compiler represents the signed integers using 2's complement notation.
  Therefore, in Example 2 above, the input represents the signed integer -3 and the output
  represents the signed integer -1073741825.

Example 1:
    Input: n = 00000010100101000001111010011100 (43261596)
    Output:    964176192 (00111001011110000010100101000000)

Example 2:
    Input: n = 11111111111111111111111111111101 (4294967293)
    Output:    3221225471 (10111111111111111111111111111111)

Constraints:
    * The input must be a binary string of length 32
"""

TODO = None


class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Reverses bits of a 32-bit unsigned integer.

        Bitwise Invariant:
        For each bit position i (from 0 to 31):
        1. Extract the bit at index i: (n >> i) & 1
        2. Shift that bit to its mirrored position (31 - i): bit << (31 - i)
        3. Bitwise OR it into the accumulator: res |= (bit << (31 - i))

        Time Complexity:  O(1) strictly 32 constant iterations
        Space Complexity: O(1)
        """
        res = 0

        # Active Learning:
        # Loop through all 32 bit positions
        for i in range(32):
            # TODO: Extract bit at position i
            bit = (n >> i) & 1
            # TODO: Place bit at mirrored position (31 - i)
            res |= bit << (31 - i)

        return res


def test_reverse_bits():
    solver = Solution()

    # Case 1: 43261596 -> 964176192
    assert solver.reverseBits(43261596) == 964176192, "Case 1 failed"

    # Case 2: 4294967293 (all 1s except second bit) -> 3221225471
    assert solver.reverseBits(4294967293) == 3221225471, "Case 2 failed"

    # Case 3: 0 -> 0
    assert solver.reverseBits(0) == 0, "Case 3 failed"

    # Case 4: 1 (0b00...001) -> 2^31 = 2147483648
    assert solver.reverseBits(1) == 2147483648, "Case 4 failed"

    # Case 5: Palindromic bit pattern 0b1000...0001 (1 + 2^31)
    pal = (1 << 31) | 1
    assert solver.reverseBits(pal) == pal, "Case 5 failed"

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_reverse_bits()
