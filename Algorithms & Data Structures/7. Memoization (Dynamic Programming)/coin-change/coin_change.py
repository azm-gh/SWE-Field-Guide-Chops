"""
LeetCode 322: Coin Change
https://leetcode.com/problems/coin-change/
"""

# Intuition: DP — unbounded knapsack. dp[i] = minimum coins to make amount i.
# For each coin, dp[i] = min(dp[i], dp[i - coin] + 1). Solve bottom-up from 0
# to amount. The recursive approach re-explores the same subproblems repeatedly.

from typing import List


def coin_change_recursive_naive(coins: List[int], amount: int) -> int:
    # Time: O(n^amount) — exponential branching over coin choices
    # Space: O(amount) — recursion stack depth
    if amount < 0:
        return -1
    if amount == 0:
        return 0
    min_coins = float("inf")
    for coin in coins:
        res = coin_change_recursive_naive(coins, amount - coin)
        if res != -1:
            min_coins = min(min_coins, 1 + res)
    return -1 if min_coins == float("inf") else int(min_coins)


def coin_change_dp_optimized(coins: List[int], amount: int) -> int:
    # Time: O(n * amount) — nested loop over coins and sub-amounts
    # Space: O(amount) — DP table
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return -1 if dp[amount] == float("inf") else dp[amount]
