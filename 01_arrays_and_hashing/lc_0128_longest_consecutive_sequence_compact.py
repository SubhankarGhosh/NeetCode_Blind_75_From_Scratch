"""LeetCode 128: Longest Consecutive Sequence (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/longest-consecutive-sequence/
Difficulty: Medium
Category: Arrays & Hashing

Pattern Context:
    To find the longest consecutive elements sequence in O(n) time (without sorting):
    1. Store all elements in a hash set for O(1) membership lookup.
    2. Sequence Head Invariant:
       A number `n` is the START (head) of a consecutive sequence if and only if
       `n - 1 not in num_set`!
    3. If `n` is a sequence head, count how far the sequence extends: `n + 1`, `n + 2`, ...
    Because inner counting only triggers at sequence heads, each number is visited
    at most twice, ensuring strictly O(n) total runtime!

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 01_arrays_and_hashing/lc_0128_longest_consecutive_sequence_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def longest_consecutive(nums: List[int]) -> int:
    """Finds the length of the longest consecutive elements sequence in O(n) time.

    Algorithmic Requirements:
    - Time Complexity: O(n) linear time.
    - Space Complexity: O(n) auxiliary space for the hash set.

    Steps to implement:
    1. Convert `nums` into a hash set `num_set` for O(1) membership testing.
    2. Initialize `longest = 0`.
    3. For each number `n` in `num_set`:
       - Check if `n` is the start of a sequence: `(n - 1) not in num_set`.
       - If yes, set `length = 1`.
       - While `n + length in num_set`, increment `length += 1`.
       - Update `longest = max(longest, length)`.
    4. Return `longest`.

    -------------------------------------------------------------------------
    TODO: Implement the sequence head detection and streak counting below.
    -------------------------------------------------------------------------
    """
    num_set = set(nums)
    longest = 0

    for n in num_set:
        # <<< YOUR CODE HERE >>>
        # Hint: A number is a sequence start if its predecessor (n - 1) is NOT in num_set.
        is_sequence_head = TODO  # Replace with: (n - 1) not in num_set
        if is_sequence_head is None:
            raise NotImplementedError("TODO: Identify sequence head invariant.")

        if is_sequence_head:
            length = 1
            while (n + length) in num_set:
                length += 1
            longest = max(longest, length)

    return longest


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
        ([9], 1),
        ([1, 2, 0, 1], 3),
        ([-5, -4, -3, 10, 11, 12, 13, 14], 5),
    ]

    print("Running verification for lc_0128_longest_consecutive_sequence_compact.py...")
    for idx, (nums, expected) in enumerate(test_cases, 1):
        result = longest_consecutive(list(nums))
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
