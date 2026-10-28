"""LeetCode 11: Container With Most Water (Reference Solution)

Problem URL: https://leetcode.com/problems/container-with-most-water/
Difficulty: Medium
Category: Two Pointers

Complexity Analysis:
- Time Complexity: O(n) where n is the length of height.
  Each iteration strictly advances left or decrements right by 1,
  guaranteeing the loop executes at most n times.
- Space Complexity: O(1) auxiliary space as only scalar integer pointers are maintained.
"""

from __future__ import annotations
from typing import List


def max_area(height: List[int]) -> int:
    """Computes maximum water area using the optimal greedy inward-converging two pointers."""
    max_water = 0
    left = 0
    right = len(height) - 1

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        current_area = width * h
        if current_area > max_water:
            max_water = current_area

        # Greedily eliminate the shorter wall
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([2, 3, 4, 5, 18, 17, 6], 17),
    ]

    print("Running verification for lc_0011_container_with_most_water_solution.py...")
    for idx, (height, expected) in enumerate(test_cases, 1):
        result = max_area(list(height))
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
