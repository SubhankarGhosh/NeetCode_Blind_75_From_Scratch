"""
LeetCode 647: Palindromic Substrings
Module: 13_1d_dynamic_programming
Difficulty: Medium
Tags: Two Pointers, String, Dynamic Programming

PROBLEM DESCRIPTION:
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:
    Input: s = "abc"
    Output: 3
    Explanation: Three palindromic substrings: "a", "b", "c".

Example 2:
    Input: s = "aaa"
    Output: 6
    Explanation: Six palindromic substrings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:
    * 1 <= s.length <= 1000
    * s consists of lowercase English letters.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Counts total palindromic substrings by expanding around all 2N - 1 centers.

        Every substring is determined by its center:
        - N single-character centers (odd length palindromes)
        - N - 1 two-character centers (even length palindromes)
        For each center, expand symmetrically outwards until characters differ or boundary is hit.
        Every successful step corresponds to exactly one unique palindromic substring.

        Time Complexity:  O(N^2) - At most N steps from each of the 2N - 1 centers.
        Space Complexity: O(1) - Constant auxiliary space.
        """
        total = 0

        def count_palindromes(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(len(s)):
            # Odd length center: s[i]
            total += count_palindromes(i, i)
            # Even length center: s[i] and s[i + 1]
            total += count_palindromes(i, i + 1)

        return total


def test_palindromic_substrings():
    solver = Solution()

    # Case 1: All distinct
    assert solver.countSubstrings("abc") == 3, "Case 1 failed"

    # Case 2: All identical
    assert solver.countSubstrings("aaa") == 6, "Case 2 failed"

    # Case 3: Single character
    assert solver.countSubstrings("a") == 1, "Case 3 failed"

    # Case 4: Palindrome with mixed characters
    assert solver.countSubstrings("aba") == 4, "Case 4 failed"

    # Case 5: 4 identical characters ("aaaa" -> 4 single, 3 double, 2 triple, 1 quad = 10)
    assert solver.countSubstrings("aaaa") == 10, "Case 5 failed"

    print("All solution tests passed successfully!")


if __name__ == "__main__":
    test_palindromic_substrings()
