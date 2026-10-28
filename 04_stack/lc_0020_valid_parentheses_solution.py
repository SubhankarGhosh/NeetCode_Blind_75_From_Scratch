"""LeetCode 20: Valid Parentheses (Reference Solution)

Problem URL: https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy
Category: Stack

Complexity Analysis:
- Time Complexity: O(n) where n is the length of string s.
  Each character is pushed and popped from the stack at most once in O(1) time.
- Space Complexity: O(n) auxiliary space to store unmatched open brackets on the stack
  (e.g., input string containing all opening brackets "(((((").
"""

from __future__ import annotations
from typing import List, Dict


def is_valid(s: str) -> bool:
    """Verifies bracket closure validity using a LIFO stack and hash map lookup."""
    stack: List[str] = []
    close_to_open: Dict[str, str] = {")": "(", "}": "{", "]": "["}

    for c in s:
        if c in close_to_open:
            if stack and stack[-1] == close_to_open[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return len(stack) == 0


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("]", False),
        ("(", False),
        ("((((((", False),
        ("{[()]}", True),
    ]

    print("Running verification for lc_0020_valid_parentheses_solution.py...")
    for idx, (s, expected) in enumerate(test_cases, 1):
        result = is_valid(s)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
