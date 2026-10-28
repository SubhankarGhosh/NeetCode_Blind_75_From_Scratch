"""LeetCode 1: Two Sum (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Category: Arrays & Hashing

Pattern Context:
    The complement property: for any element x, its required partner to sum to
    `target` is exactly `complement = target - x`. Storing previously visited numbers
    and their indices in a hash map allows instantaneous O(1) partner lookup during
    a single pass over the array.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 01_arrays_and_hashing/lc_0001_two_sum_compact.py
"""

from __future__ import annotations
from typing import List, Dict

# Sentinel placeholder for exercise tasks
TODO = None


def two_sum(nums: List[int], target: int) -> List[int]:
    """Finds indices of the two numbers such that they add up to target.

    Algorithmic Requirements:
    - Time Complexity: O(n) single pass through nums.
    - Space Complexity: O(n) auxiliary space for storing visited elements.

    Steps to implement:
    1. Initialize an empty hash map `prev_map` mapping value -> index.
    2. For each index `i` and number `n` in `enumerate(nums)`:
       - Compute `diff = target - n`.
       - If `diff` exists in `prev_map`, return [prev_map[diff], i].
       - Otherwise, store `prev_map[n] = i`.
    3. Return [] if no matching pair exists.

    -------------------------------------------------------------------------
    TODO: Implement the one-pass hash map complement search below.
    -------------------------------------------------------------------------
    """
    prev_map: Dict[int, int] = {}

    for i, n in enumerate(nums):
        # <<< YOUR CODE HERE >>>
        # Hint: What value must we pair with n to reach target?
        diff = TODO  # Replace with: target - n
        if diff is None:
            raise NotImplementedError("TODO: Compute target complement.")

        if diff in prev_map:
            return [prev_map[diff], i]

        prev_map[n] = i

    return []


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([0, 4, 3, 0], 0, [0, 3]),
    ]

    print("Running verification for lc_0001_two_sum_compact.py...")
    for idx, (nums, target, expected) in enumerate(test_cases, 1):
        result = two_sum(list(nums), target)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
