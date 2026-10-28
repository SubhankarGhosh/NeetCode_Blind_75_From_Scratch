"""LeetCode 20: Valid Parentheses (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy
Category: Stack

Pattern Context:
    The Last-In-First-Out (LIFO) property of a stack is the canonical paradigm for
    hierarchical matching and syntax parsing:
    - Every closing delimiter must match the most recently opened unclosed delimiter.
    - Using a hash map `close_to_open = {')': '(', '}': '{', ']': '['}`:
      * When an opening bracket arrives: push to stack.
      * When a closing bracket arrives: verify that the stack is non-empty and that
        the top element matches the corresponding opening delimiter.
    - String is valid if and only if all pairs match and stack is completely empty at the end.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 04_stack/lc_0020_valid_parentheses_compact.py
"""

from __future__ import annotations
from typing import List, Dict

# Sentinel placeholder for exercise tasks
TODO = None


def is_valid(s: str) -> bool:
    """Determines if the input string containing brackets '()[]{}' is valid.

    Algorithmic Requirements:
    - Time Complexity: O(n) single linear scan over characters in s.
    - Space Complexity: O(n) auxiliary space for the stack in worst case.

    Steps to implement:
    1. Initialize an empty stack `stack = []`.
    2. Define mapping `close_to_open = {')': '(', '}': '{', ']': '['}`.
    3. For each character `c` in `s`:
       - If `c in close_to_open`:
         * If `stack` is non-empty and `stack[-1] == close_to_open[c]`:
           - Pop top of stack: `stack.pop()`.
         * Otherwise, return False immediately (unmatched closing bracket).
       - Else (`c` is an opening bracket):
         * Push `c` to `stack`.
    4. Return True if and only if `len(stack) == 0`.

    -------------------------------------------------------------------------
    TODO: Implement the stack bracket matching logic below.
    -------------------------------------------------------------------------
    """
    stack: List[str] = []
    close_to_open: Dict[str, str] = {")": "(", "}": "{", "]": "["}

    for c in s:
        if c in close_to_open:
            # <<< YOUR CODE HERE >>>
            # Hint: Check if stack has an element and top matches the required open bracket
            is_matched = TODO  # Replace with: stack and stack[-1] == close_to_open[c]
            if is_matched is None:
                raise NotImplementedError("TODO: Implement stack top match check.")

            if is_matched:
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

    print("Running verification for lc_0020_valid_parentheses_compact.py...")
    for idx, (s, expected) in enumerate(test_cases, 1):
        result = is_valid(s)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
