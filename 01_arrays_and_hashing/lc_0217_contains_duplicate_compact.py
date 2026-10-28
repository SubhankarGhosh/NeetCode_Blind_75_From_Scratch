"""LeetCode 217: Contains Duplicate (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Category: Arrays & Hashing

Pattern Context:
    Hash Set membership testing offers O(1) average-time lookups. When verifying whether
    an array contains duplicate values, trading O(n) auxiliary space for O(n) linear time
    is the standard optimal trade-off compared to O(n^2) brute-force or O(n log n) sorting.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 01_arrays_and_hashing/lc_0217_contains_duplicate_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def contains_duplicate(nums: List[int]) -> bool:
    """Determines if any value appears at least twice in the array.

    Algorithmic Requirements:
    - Time Complexity: O(n) single linear scan over nums.
    - Space Complexity: O(n) auxiliary memory for the hash set.

    Steps to implement:
    1. Initialize an empty hash set `seen`.
    2. Iterate through each number `x` in `nums`:
       - If `x` already exists in `seen`, return True immediately.
       - Otherwise, insert `x` into `seen`.
    3. If the loop completes without finding duplicates, return False.

    -------------------------------------------------------------------------
    TODO: Implement the single-pass hash set duplicate detection logic below.
    -------------------------------------------------------------------------
    """
    seen = set()
    for x in nums:
        # <<< YOUR CODE HERE >>>
        # Hint: Check if x is in seen. If so, duplicate found! Otherwise, add x.
        is_duplicate = TODO  # Replace with: x in seen
        if is_duplicate is None:
            raise NotImplementedError("TODO: Implement membership check.")
        if is_duplicate:
            return True
        seen.add(x)

    return False


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([], False),
        ([42], False),
        ([-1, -2, -3, -1], True),
    ]

    print("Running verification for lc_0217_contains_duplicate_compact.py...")
    for idx, (nums, expected) in enumerate(test_cases, 1):
        result = contains_duplicate(list(nums))
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
