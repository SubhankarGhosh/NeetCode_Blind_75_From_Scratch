"""
LeetCode 5: Longest Palindromic Substring
Module: 13_1d_dynamic_programming
Difficulty: Medium
Tags: Two Pointers, String, Dynamic Programming

PROBLEM DESCRIPTION:
Given a string s, return the longest palindromic substring in s.

Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

Example 2:
    Input: s = "cbbd"
    Output: "bb"

Constraints:
    * 1 <= s.length <= 1000
    * s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring by expanding around centers.

        Every palindrome has a center:
        - An odd-length palindrome has a single center character at index i.
        - An even-length palindrome has a two-character center between indices i and i + 1.
        There are 2N - 1 possible centers across a string of length N. Expanding from
        each center takes O(N) time in the worst case, yielding O(N^2) total time with O(1) space.

        Time Complexity:  O(N^2)
        Space Complexity: O(1) auxiliary space (excluding returned string).
        """
        if not s or len(s) < 2:
            return s

        res = ""
        res_len = 0

        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        for i in range(len(s)):
            # Odd length expansion
            odd = expand(i, i)
            if len(odd) > res_len:
                res = odd
                res_len = len(odd)

            # Even length expansion
            even = expand(i, i + 1)
            if len(even) > res_len:
                res = even
                res_len = len(even)

        return res


def test_longest_palindrome():
    solver = Solution()

    # Case 1: "babad" -> "bab" or "aba"
    res1 = solver.longestPalindrome("babad")
    assert res1 in {"bab", "aba"}, f"Case 1 failed: got {res1}"

    # Case 2: "cbbd" -> "bb"
    assert solver.longestPalindrome("cbbd") == "bb", "Case 2 failed"

    # Case 3: Single character
    assert solver.longestPalindrome("a") == "a", "Case 3 failed"

    # Case 4: Entire string is a palindrome
    assert solver.longestPalindrome("racecar") == "racecar", "Case 4 failed"

    # Case 5: All identical characters
    assert solver.longestPalindrome("aaaa") == "aaaa", "Case 5 failed"

    print("All solution tests passed successfully!")


if __name__ == "__main__":
    test_longest_palindrome()
