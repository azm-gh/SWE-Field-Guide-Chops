"""
LeetCode 198: House Robber
https://leetcode.com/problems/house-robber/
"""

# Intuition: DP — at each house, decide to rob or skip. If you rob, add
# nums[i] + profit from i-2. If you skip, take profit from i-1.
# dp[i] = max(dp[i-1], nums[i] + dp[i-2]). Can be optimized to O(1) space.

from typing import List


def rob_recursive_naive(nums: List[int]) -> int:
    # Time: O(2^n) — two branches per house (rob/skip)
    # Space: O(n) — recursion stack depth
    def helper(i):
        if i >= len(nums):
            return 0
        return max(nums[i] + helper(i + 2), helper(i + 1))
    return helper(0)


def rob_dp_optimized(nums: List[int]) -> int:
    # Time: O(n) — single pass, bottom-up DP
    # Space: O(1)
    prev, curr = 0, 0
    for num in nums:
        prev, curr = curr, max(curr, prev + num)
    return curr
