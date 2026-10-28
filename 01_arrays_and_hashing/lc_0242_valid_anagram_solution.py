"""LeetCode 242: Valid Anagram (Reference Solution)

Problem URL: https://leetcode.com/problems/valid-anagram/
Difficulty: Easy
Category: Arrays & Hashing

Complexity Analysis:
- Time Complexity: O(n) where n is the length of string s and t.
  Iterating through the strings takes linear time.
- Space Complexity: O(1) auxiliary space because the alphabet is bounded to 26
  lowercase English letters, requiring a fixed 26-element integer table.
  (In general Unicode environments, a hash map requires O(k) space where k is
  the size of the distinct character alphabet).
"""

from __future__ import annotations


def is_anagram(s: str, t: str) -> bool:
    """Determines whether t is an anagram of s using a 26-element frequency table."""
    if len(s) != len(t):
        return False

    counts = [0] * 26
    for char_s, char_t in zip(s, t):
        counts[ord(char_s) - ord("a")] += 1
        counts[ord(char_t) - ord("a")] -= 1

    return all(c == 0 for c in counts)


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "a", True),
        ("ab", "a", False),
        ("listen", "silent", True),
        ("aabbcc", "bbaacc", True),
        ("aabbc", "aabbd", False),
    ]

    print("Running verification for lc_0242_valid_anagram_solution.py...")
    for idx, (s, t, expected) in enumerate(test_cases, 1):
        result = is_anagram(s, t)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
