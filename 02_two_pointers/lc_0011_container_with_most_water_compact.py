"""LeetCode 11: Container With Most Water (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/container-with-most-water/
Difficulty: Medium
Category: Two Pointers

Pattern Context:
    Given an integer array `height` representing vertical lines, choose two lines that,
    together with the x-axis, form a container storing the maximum water volume:
        Area = (right - left) * min(height[left], height[right])

    Greedy Two-Pointer Invariant:
    - Start at maximum width: left = 0, right = len(height) - 1.
    - The bottleneck of any container is strictly its SHORTER wall: min(height[left], height[right]).
    - Moving the taller wall inward strictly reduces width while the height remains
      capped by the existing short wall (guaranteeing a strictly smaller or equal area).
    - Therefore, the ONLY way to find a potentially larger area is to advance the
      SHORTER wall's pointer inward, hoping to discover a taller line.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 02_two_pointers/lc_0011_container_with_most_water_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def max_area(height: List[int]) -> int:
    """Finds two vertical lines that form a container holding the maximum water.

    Algorithmic Requirements:
    - Time Complexity: O(n) single pass with inward-converging pointers.
    - Space Complexity: O(1) auxiliary space.

    Steps to implement:
    1. Initialize `max_water = 0`, `left = 0`, `right = len(height) - 1`.
    2. While `left < right`:
       - `width = right - left`.
       - `current_area = width * min(height[left], height[right])`.
       - `max_water = max(max_water, current_area)`.
       - Greedy pointer movement:
         * If `height[left] < height[right]`, increment `left += 1`.
         * Otherwise, decrement `right -= 1`.
    3. Return `max_water`.

    -------------------------------------------------------------------------
    TODO: Implement the greedy two-pointer area maximization below.
    -------------------------------------------------------------------------
    """
    max_water = 0
    left = 0
    right = len(height) - 1

    while left < right:
        width = right - left
        # <<< YOUR CODE HERE >>>
        # Hint: Area is width times the minimum of the two wall heights
        current_area = TODO  # Replace with: width * min(height[left], height[right])
        if current_area is None:
            raise NotImplementedError("TODO: Calculate current water container area.")

        max_water = max(max_water, current_area)

        # Move the pointer pointing to the shorter vertical bar
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

    print("Running verification for lc_0011_container_with_most_water_compact.py...")
    for idx, (height, expected) in enumerate(test_cases, 1):
        result = max_area(list(height))
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
