"""LeetCode 217: Contains Duplicate (Reference Solution)

Problem URL: https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Category: Arrays & Hashing

Complexity Analysis:
- Time Complexity: O(n) average case, where n is the number of elements in nums.
  Checking membership and adding to a hash set runs in O(1) expected time.
- Space Complexity: O(n) auxiliary space to store at most n distinct elements in the set.
"""

from __future__ import annotations
from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """Returns True if any value appears at least twice in the array, otherwise False.

    Early-exits on the very first detected duplicate for optimal real-world performance.
    """
    seen = set()
    for x in nums:
        if x in seen:
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

    print("Running verification for lc_0217_contains_duplicate_solution.py...")
    for idx, (nums, expected) in enumerate(test_cases, 1):
        result = contains_duplicate(list(nums))
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
