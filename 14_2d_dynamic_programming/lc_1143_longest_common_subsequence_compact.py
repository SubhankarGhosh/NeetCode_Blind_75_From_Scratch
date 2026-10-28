"""
LeetCode 1143: Longest Common Subsequence
Module: 14_2d_dynamic_programming
Difficulty: Medium
Tags: String, Dynamic Programming

PROBLEM DESCRIPTION:
Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some
characters (can be none) deleted without changing the relative order of the remaining
characters.
- For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
    Input: text1 = "abcde", text2 = "ace"
    Output: 3
    Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
    Input: text1 = "abc", text2 = "abc"
    Output: 3
    Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
    Input: text1 = "abc", text2 = "def"
    Output: 0
    Explanation: There is no such common subsequence, so the result is 0.

Constraints:
    * 1 <= text1.length, text2.length <= 1000
    * text1 and text2 consist of only lowercase English characters.
"""

TODO = None


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Calculates LCS length using space-optimized 2D Dynamic Programming.

        Recurrence:
        If text1[i] == text2[j]:
            dp[i][j] = 1 + dp[i + 1][j + 1]
        Else:
            dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        Time Complexity:  O(M * N)
        Space Complexity: O(min(M, N))
        """
        # Ensure text2 is the shorter string for minimum row space
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        m, n = len(text1), len(text2)

        # Active Learning:
        # dp stores the LCS results for the next row (i + 1)
        prev_row = [0] * (n + 1)

        for i in range(m - 1, -1, -1):
            curr_row = [0] * (n + 1)
            for j in range(n - 1, -1, -1):
                # TODO: Check character match
                if text1[i] == text2[j]:
                    curr_row[j] = 1 + prev_row[j + 1]
                else:
                    curr_row[j] = max(prev_row[j], curr_row[j + 1])
            prev_row = curr_row

        return prev_row[0]


def test_longest_common_subsequence():
    solver = Solution()

    # Case 1: Standard match "abcde" and "ace" -> 3
    assert solver.longestCommonSubsequence("abcde", "ace") == 3, "Case 1 failed"

    # Case 2: Identical strings
    assert solver.longestCommonSubsequence("abc", "abc") == 3, "Case 2 failed"

    # Case 3: Completely disjoint strings
    assert solver.longestCommonSubsequence("abc", "def") == 0, "Case 3 failed"

    # Case 4: Interleaved subsequence "ezupkr" and "ubmrapg" -> 2 ("up" or "ur")
    assert solver.longestCommonSubsequence("ezupkr", "ubmrapg") == 2, "Case 4 failed"

    # Case 5: Single character match
    assert solver.longestCommonSubsequence("a", "a") == 1, "Case 5 failed"
    assert solver.longestCommonSubsequence("a", "b") == 0, "Case 6 failed"

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_longest_common_subsequence()
