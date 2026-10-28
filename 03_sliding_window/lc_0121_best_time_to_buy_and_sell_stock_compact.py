"""LeetCode 121: Best Time to Buy and Sell Stock (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy
Category: Sliding Window

Pattern Context:
    We must maximize profit by picking a buy day and a future sell day (i < j).
    This forms a dynamic 2-pointer / sliding window where:
    - Pointer `left` tracks the minimum purchase price discovered so far.
    - Pointer `right` scans through future selling days.
    - If `prices[right] < prices[left]`, we immediately reset our buy day (`left = right`),
      as buying at this lower price can only yield higher future profits.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 03_sliding_window/lc_0121_best_time_to_buy_and_sell_stock_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def max_profit(prices: List[int]) -> int:
    """Finds maximum profit from buying and selling stock once.

    Algorithmic Requirements:
    - Time Complexity: O(n) single pass over prices.
    - Space Complexity: O(1) auxiliary space.

    Steps to implement:
    1. Initialize `max_p = 0`, `left = 0` (buy index), and scan `right` from 1 to len(prices)-1.
    2. At each day `right`:
       - If `prices[left] < prices[right]`:
         * Calculate `profit = prices[right] - prices[left]`.
         * Update `max_p = max(max_p, profit)`.
       - Else (`prices[right] <= prices[left]`):
         * Shift buy day: `left = right`.
    3. Return `max_p`.

    -------------------------------------------------------------------------
    TODO: Implement the sliding window profit tracking logic below.
    -------------------------------------------------------------------------
    """
    max_p = 0
    left = 0

    for right in range(1, len(prices)):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            # <<< YOUR CODE HERE >>>
            # Hint: Update max_p with the maximum profit seen
            updated_profit = TODO  # Replace with: max(max_p, profit)
            if updated_profit is None:
                raise NotImplementedError("TODO: Update max profit.")
            max_p = updated_profit
        else:
            # Found a new lower minimum buy price
            left = right

    return max_p


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2], 1),
        ([2, 4, 1], 2),
        ([3, 2, 6, 5, 0, 3], 4),
        ([], 0),
        ([5], 0),
    ]

    print("Running verification for lc_0121_best_time_to_buy_and_sell_stock_compact.py...")
    for idx, (prices, expected) in enumerate(test_cases, 1):
        result = max_profit(list(prices))
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
