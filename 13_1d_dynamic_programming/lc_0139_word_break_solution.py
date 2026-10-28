"""
LeetCode 139: Word Break
Module: 13_1d_dynamic_programming
Difficulty: Medium
Tags: Array, Hash Table, String, Dynamic Programming, Trie, Memoization

PROBLEM DESCRIPTION:
Given a string s and a dictionary of strings wordDict, return true if s can be
segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
    Input: s = "applepenapple", wordDict = ["apple","pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
    Note that you are allowed to reuse a dictionary word.

Example 3:
    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: false

Constraints:
    * 1 <= s.length <= 300
    * 1 <= wordDict.length <= 1000
    * 1 <= wordDict[i].length <= 20
    * s and wordDict[i] consist of only lowercase English letters.
    * All the strings of wordDict are unique.
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Determines if s can be segmented into words from wordDict using bottom-up DP.

        Let dp[i] represent whether suffix s[i:] can be segmented into dictionary words.
        Base Case:
            dp[len(s)] = True (the empty string suffix requires 0 words to complete)
        Recurrence:
            For each index i from len(s) - 1 down to 0:
                dp[i] = any(dp[i + len(w)] for w in wordDict if s[i : i + len(w)] == w)

        Time Complexity:  O(N * M * K) where N = len(s), M = len(wordDict), K = max word length.
        Space Complexity: O(N) for the dp array.
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for w in wordDict:
                w_len = len(w)
                if i + w_len <= n and s[i : i + w_len] == w:
                    dp[i] = dp[i + w_len]
                if dp[i]:
                    break

        return dp[0]


def test_word_break():
    solver = Solution()

    # Case 1: "leetcode" -> ["leet", "code"]
    assert solver.wordBreak("leetcode", ["leet", "code"]) is True, "Case 1 failed"

    # Case 2: "applepenapple" with word reuse
    assert solver.wordBreak("applepenapple", ["apple", "pen"]) is True, "Case 2 failed"

    # Case 3: "catsandog" -> impossible segmentation
    assert solver.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False, "Case 3 failed"

    # Case 4: Single character repeated
    assert solver.wordBreak("aaaaaaa", ["aaaa", "aaa"]) is True, "Case 4 failed"

    # Case 5: Exact single word match
    assert solver.wordBreak("code", ["code"]) is True, "Case 5 failed"

    print("All solution tests passed successfully!")


if __name__ == "__main__":
    test_word_break()
