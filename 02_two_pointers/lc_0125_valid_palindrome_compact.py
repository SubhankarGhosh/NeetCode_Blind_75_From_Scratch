"""LeetCode 125: Valid Palindrome (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy
Category: Two Pointers

Pattern Context:
    A phrase is a palindrome if, after converting all uppercase letters into lowercase
    letters and removing all non-alphanumeric characters, it reads the same forward
    and backward.
    While filtering into a new string takes O(n) auxiliary space, an in-place two-pointer
    approach achieves optimal O(1) space by skipping non-alphanumeric characters on the fly.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 02_two_pointers/lc_0125_valid_palindrome_compact.py
"""

from __future__ import annotations

# Sentinel placeholder for exercise tasks
TODO = None


def is_palindrome(s: str) -> bool:
    """Determines if string s is a palindrome considering only alphanumeric characters.

    Algorithmic Requirements:
    - Time Complexity: O(n) single pass with inward-converging pointers.
    - Space Complexity: O(1) auxiliary space (no extra strings or arrays created).

    Steps to implement:
    1. Initialize `left = 0` and `right = len(s) - 1`.
    2. While `left < right`:
       - Advance `left` forward while `left < right` and `not s[left].isalnum()`.
       - Move `right` backward while `left < right` and `not s[right].isalnum()`.
       - Compare characters case-insensitively: `s[left].lower() != s[right].lower()`.
         If they differ, return False immediately.
       - Advance both pointers: `left += 1`, `right -= 1`.
    3. Return True if pointers cross without mismatch.

    -------------------------------------------------------------------------
    TODO: Implement the in-place two-pointer palindrome check below.
    -------------------------------------------------------------------------
    """
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        # <<< YOUR CODE HERE >>>
        # Hint: Check if characters match case-insensitively
        mismatch = TODO  # Replace with: s[left].lower() != s[right].lower()
        if mismatch is None:
            raise NotImplementedError("TODO: Compare characters case-insensitively.")
        if mismatch:
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

    print("Running verification for lc_0125_valid_palindrome_compact.py...")
    for idx, (s, expected) in enumerate(test_cases, 1):
        result = is_palindrome(s)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
