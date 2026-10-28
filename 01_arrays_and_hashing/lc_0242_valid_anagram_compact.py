"""LeetCode 242: Valid Anagram (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/valid-anagram/
Difficulty: Easy
Category: Arrays & Hashing

Pattern Context:
    An anagram is formed by rearranging characters of a word using each original
    character exactly once. Two strings s and t are anagrams if and only if their
    character frequency distributions are identical.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 01_arrays_and_hashing/lc_0242_valid_anagram_compact.py
"""

from __future__ import annotations

# Sentinel placeholder for exercise tasks
TODO = None


def is_anagram(s: str, t: str) -> bool:
    """Returns True if t is an anagram of s, and False otherwise.

    Algorithmic Requirements:
    - Time Complexity: O(n) where n = len(s) = len(t).
    - Space Complexity: O(1) auxiliary space if bounded to fixed alphabet (26 lowercase chars).

    Steps to implement:
    1. Quick check: If len(s) != len(t), return False immediately.
    2. Maintain character frequencies using a fixed-size array of length 26 (or hash map).
    3. Increment counts for characters in s, decrement counts for characters in t.
    4. Verify that all final frequencies are 0.

    -------------------------------------------------------------------------
    TODO: Implement character frequency counting logic below.
    -------------------------------------------------------------------------
    """
    if len(s) != len(t):
        return False

    counts = [0] * 26
    for char_s, char_t in zip(s, t):
        # <<< YOUR CODE HERE >>>
        # Hint: Use ord(char) - ord('a') to index into counts.
        idx_s = TODO  # Replace with: ord(char_s) - ord('a')
        idx_t = TODO  # Replace with: ord(char_t) - ord('a')
        if idx_s is None or idx_t is None:
            raise NotImplementedError("TODO: Compute 0-indexed alphabet positions.")
        counts[idx_s] += 1
        counts[idx_t] -= 1

    # Check if all counts are balanced to zero
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

    print("Running verification for lc_0242_valid_anagram_compact.py...")
    for idx, (s, t, expected) in enumerate(test_cases, 1):
        result = is_anagram(s, t)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
