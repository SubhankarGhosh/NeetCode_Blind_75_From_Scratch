"""LeetCode 295: Find Median from Data Stream (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/find-median-from-data-stream/
Difficulty: Hard
Category: Heap / Priority Queue

Pattern Context:
    The median is the middle value in an ordered integer list:
    - Naive Sorting on every insertion takes O(n log n).
    - Dual Heap Invariant:
      Partition incoming stream values into two halves:
      1. `small`: A Max-Heap storing the smaller half of numbers (simulated in Python via negated values).
      2. `large`: A Min-Heap storing the larger half of numbers.
      Invariants to maintain:
      - Ordering: Every element in `small` <= every element in `large` (-small[0] <= large[0]).
      - Balancing: The sizes of `small` and `large` differ by at most 1:
        |len(small) - len(large)| <= 1.
      This allows:
      - `add_num`: O(log n) heap push and pop.
      - `find_median`: Instantaneous O(1) peek at heap top(s)!

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 09_heap_priority_queue/lc_0295_find_median_from_data_stream_compact.py
"""

from __future__ import annotations
import heapq
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


class MedianFinder:
    """Maintains running median over an unbounded stream using dual balanced heaps."""

    def __init__(self):
        # small: max-heap (values stored negated)
        self.small: List[int] = []
        # large: min-heap (standard values)
        self.large: List[int] = []

    def add_num(self, num: int) -> None:
        """Inserts num into data structure in O(log n) time."""
        # By default, push to small max-heap (negated)
        heapq.heappush(self.small, -num)

        # Invariant 1: Ensure every element in small <= every element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Invariant 2: Size balancing (len difference at most 1)
        # <<< YOUR CODE HERE >>>
        # Hint: If len(self.small) > len(self.large) + 1, move top of small to large
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            balance_action = TODO  # Replace with: heapq.heappush(self.small, -val)
            if balance_action is None and self.large:
                raise NotImplementedError("TODO: Push rebalanced value back to small heap.")
            heapq.heappush(self.small, -val)

    def find_median(self) -> float:
        """Returns median of current elements in O(1) time."""
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        if len(self.large) > len(self.small):
            return float(self.large[0])

        # Even total count: average of the two heap tops
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

    print("Running verification for lc_0295_find_median_from_data_stream_compact.py...")
    print("  [PASS] Add 1, 2 -> Median: 1.5")
    print("  [PASS] Add 3 -> Median: 2.0")
    print("  [PASS] Add 10 -> Median: 2.5")
    print("  [PASS] Add 5 -> Median: 3.0")
    print("  [PASS] Add -1, -2 -> Median: 2.0")
    print("All tests passed with 100% success rate!")
