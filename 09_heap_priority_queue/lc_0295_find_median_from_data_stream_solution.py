"""LeetCode 295: Find Median from Data Stream (Reference Solution)

Problem URL: https://leetcode.com/problems/find-median-from-data-stream/
Difficulty: Hard
Category: Heap / Priority Queue

Complexity Analysis:
- Time Complexity:
  * add_num(num): O(log n) to push and maintain dual heap ordering and balance.
  * find_median(): O(1) instantaneous peek at the root element(s) of the heaps.
- Space Complexity: O(n) auxiliary space to store all n incoming numbers in the heaps.
"""

from __future__ import annotations
import heapq
from typing import List


class MedianFinder:
    """Calculates streaming median in O(log n) insertion and O(1) lookup using balanced dual heaps."""

    def __init__(self):
        # small: Max-Heap (stored as negative values) for numbers <= median
        self.small: List[int] = []
        # large: Min-Heap for numbers >= median
        self.large: List[int] = []

    def add_num(self, num: int) -> None:
        """Adds a number into the data stream, rebalancing the two heaps."""
        # Step 1: Push to max-heap (small)
        heapq.heappush(self.small, -num)

        # Step 2: Maintain order invariant: max(small) <= min(large)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: Maintain size invariant: |len(small) - len(large)| <= 1
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def find_median(self) -> float:
        """Returns the current median in O(1) time."""
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        if len(self.large) > len(self.small):
            return float(self.large[0])

        return (-self.small[0] + self.large[0]) / 2.0


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    mf = MedianFinder()
    mf.add_num(1)
    mf.add_num(2)
    assert mf.find_median() == 1.5, f"Expected 1.5, got {mf.find_median()}"

    mf.add_num(3)
    assert mf.find_median() == 2.0, f"Expected 2.0, got {mf.find_median()}"

    mf.add_num(10)
    assert mf.find_median() == 2.5, f"Expected 2.5, got {mf.find_median()}"

    mf.add_num(5)
    assert mf.find_median() == 3.0, f"Expected 3.0, got {mf.find_median()}"

    mf.add_num(-1)
    mf.add_num(-2)
    assert mf.find_median() == 2.0, f"Expected 2.0, got {mf.find_median()}"

    print("Running verification for lc_0295_find_median_from_data_stream_solution.py...")
    print("  [PASS] Add 1, 2 -> Median: 1.5")
    print("  [PASS] Add 3 -> Median: 2.0")
    print("  [PASS] Add 10 -> Median: 2.5")
    print("  [PASS] Add 5 -> Median: 3.0")
    print("  [PASS] Add -1, -2 -> Median: 2.0")
    print("All tests passed with 100% success rate!")
