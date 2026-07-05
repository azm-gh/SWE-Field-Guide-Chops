"""
LeetCode 303: Range Sum Query
https://leetcode.com/problems/range-sum-query-immutable/
"""

# Intuition: Prefix sum array for O(1) range sum queries. Precompute
# prefix[i] = sum of first i elements (prefix[0] = 0). Then
# sum_range(left, right) = prefix[right+1] - prefix[left]. Space-for-time
# tradeoff: O(n) precomputation for O(1) queries.

from typing import List


class NumArrayNaive:
    # Time: O(n) per query — slice sum from scratch
    # Space: O(n) — stores the original array
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sum_range(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])


class NumArrayOptimized:
    # Time: O(1) per query — prefix diff gives range sum instantly
    # Space: O(n) — prefix array
    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + num

    def sum_range(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
