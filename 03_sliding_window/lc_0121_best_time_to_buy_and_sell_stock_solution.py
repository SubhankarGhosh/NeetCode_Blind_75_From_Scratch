"""LeetCode 121: Best Time to Buy and Sell Stock (Reference Solution)

Problem URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy
Category: Sliding Window

Complexity Analysis:
- Time Complexity: O(n) where n is the number of trading days in prices.
  A single pass through the price array with O(1) arithmetic operations per day.
- Space Complexity: O(1) auxiliary space as only two scalar indices/prices are maintained.
"""

from __future__ import annotations
from typing import List


def max_profit(prices: List[int]) -> int:
    """Computes the maximum single-trade profit using dynamic two-pointer window shift."""
    max_p = 0
    left = 0  # Buy day index

    for right in range(1, len(prices)):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            if profit > max_p:
                max_p = profit
        else:
            # We found a cheaper buy price, shift buy window directly to right
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

    print("Running verification for lc_0121_best_time_to_buy_and_sell_stock_solution.py...")
    for idx, (prices, expected) in enumerate(test_cases, 1):
        result = max_profit(list(prices))
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
