"""
LeetCode 322: Coin Change
Module: 13_1d_dynamic_programming
Difficulty: Medium
Tags: Array, Dynamic Programming, Breadth-First Search

PROBLEM DESCRIPTION:
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that
amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1 (3 coins)

Example 2:
    Input: coins = [2], amount = 3
    Output: -1

Example 3:
    Input: coins = [1], amount = 0
    Output: 0

Constraints:
    * 1 <= coins.length <= 12
    * 1 <= coins[i] <= 2^31 - 1
    * 0 <= amount <= 10^4
"""

from typing import List

TODO = None


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Calculates the minimum number of coins needed for target amount.

        Recurrence:
        dp[a] = min(dp[a], dp[a - c] + 1) for all c in coins where a >= c
        Base case: dp[0] = 0

        Time Complexity:  O(amount * len(coins))
        Space Complexity: O(amount)
        """
        # Active Learning:
        # Initialize dp array with infinity (amount + 1 is an unreachable sentinel)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a >= c:
                    # TODO: Update dp[a] with min(dp[a], dp[a - c] + 1)
                    dp[a] = min(dp[a], dp[a - c] + 1)

        # TODO: Return dp[amount] if valid, else -1
        return dp[amount] if dp[amount] <= amount else -1


def test_coin_change():
    solver = Solution()

    # Case 1: Standard [1, 2, 5], 11 -> 3
    assert solver.coinChange([1, 2, 5], 11) == 3, "Case 1 failed"

    # Case 2: Impossible combination
    assert solver.coinChange([2], 3) == -1, "Case 2 failed"

    # Case 3: Zero amount
    assert solver.coinChange([1], 0) == 0, "Case 3 failed"

    # Case 4: Large denomination with non-greedy optimal solution
    # Greedy picks 4 + 1 + 1 (3 coins), optimal is 3 + 3 (2 coins)
    assert solver.coinChange([1, 3, 4], 6) == 2, "Case 4 failed"

    # Case 5: Single coin exact match
    assert solver.coinChange([5], 5) == 1, "Case 5 failed"

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_coin_change()
