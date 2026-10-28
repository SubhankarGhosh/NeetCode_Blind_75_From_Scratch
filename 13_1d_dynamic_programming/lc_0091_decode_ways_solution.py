"""
LeetCode 91: Decode Ways
Module: 13_1d_dynamic_programming
Difficulty: Medium
Tags: String, Dynamic Programming

PROBLEM DESCRIPTION:
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into
letters using the reverse of the mapping above (there may be multiple ways).
For example, "11106" can be mapped into:
- "AAJF" with the grouping (1 1 10 6)
- "KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F'
since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
    Input: s = "12"
    Output: 2
    Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
    Input: s = "226"
    Output: 3
    Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
    Input: s = "06"
    Output: 0
    Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

Constraints:
    * 1 <= s.length <= 100
    * s contains only digits and may contain leading zero(s).
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Calculates valid decodings using 1D dynamic programming with rolling state.

        Let dp[i] be the number of ways to decode prefix s[:i].
        Transitions at character index i (1-indexed):
        1. Single digit transition: s[i - 1] in '1'..'9':
           dp[i] += dp[i - 1]
        2. Two digit transition: s[i-2:i] represents an integer in 10..26:
           dp[i] += dp[i - 2]

        Time Complexity:  O(N) - Linear pass through the string.
        Space Complexity: O(1) - Two variables for dp[i - 1] and dp[i - 2].
        """
        if not s or s[0] == "0":
            return 0

        prev2 = 1  # dp[0]: empty string has 1 valid decoding
        prev1 = 1  # dp[1]: valid first character has 1 decoding

        for i in range(2, len(s) + 1):
            curr = 0

            # Single digit decode
            if s[i - 1] != "0":
                curr += prev1

            # Two digit decode
            two_digit = int(s[i - 2 : i])
            if 10 <= two_digit <= 26:
                curr += prev2

            prev2 = prev1
            prev1 = curr

        return prev1


def test_decode_ways():
    solver = Solution()

    # Case 1: "12" -> "AB", "L"
    assert solver.numDecodings("12") == 2, "Case 1 failed"

    # Case 2: "226" -> 3 ways
    assert solver.numDecodings("226") == 3, "Case 2 failed"

    # Case 3: Leading zero
    assert solver.numDecodings("06") == 0, "Case 3 failed"

    # Case 4: Zero in the middle (valid: "10")
    assert solver.numDecodings("10") == 1, "Case 4 failed"

    # Case 5: Zero in the middle (valid: "2101")
    assert solver.numDecodings("2101") == 1, "Case 5 failed"

    # Case 6: Invalid zeros
    assert solver.numDecodings("0") == 0, "Case 6 failed"
    assert solver.numDecodings("100") == 0, "Case 7 failed"

    print("All solution tests passed successfully!")


if __name__ == "__main__":
    test_decode_ways()
