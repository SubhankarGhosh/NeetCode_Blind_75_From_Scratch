"""LeetCode 125: Valid Palindrome (Reference Solution)

Problem URL: https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy
Category: Two Pointers

Complexity Analysis:
- Time Complexity: O(n) where n is the length of string s.
  Each pointer moves inward at most n steps across the string.
- Space Complexity: O(1) auxiliary space as character validation and comparison
  occur directly in-place without allocating filtered strings.
"""

from __future__ import annotations


def is_palindrome(s: str) -> bool:
    """Verifies palindromic symmetry in-place using inward-converging pointers."""
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
        ("a.", True),
        (".,", True),
        ("Was it a car or a cat I saw?", True),
        ("tab a cat", False),
    ]

    print("Running verification for lc_0125_valid_palindrome_solution.py...")
    for idx, (s, expected) in enumerate(test_cases, 1):
        result = is_palindrome(s)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
