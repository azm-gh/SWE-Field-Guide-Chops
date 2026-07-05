"""
LeetCode 724: Find Pivot Index
https://leetcode.com/problems/find-pivot-index/
"""

# Intuition: Prefix sum. Compute total sum, then iterate left to right tracking
# the running left sum. At index i, the right sum = total - left_sum - nums[i].
# If left_sum equals right_sum, i is the pivot. One pass after computing total.

from typing import List


def pivot_index_naive(nums: List[int]) -> int:
    # Time: O(n^2) — sum left/right O(n) for each index
    # Space: O(1)
    n = len(nums)
    for i in range(n):
        left_sum = sum(nums[:i])
        right_sum = sum(nums[i + 1:])
        if left_sum == right_sum:
            return i
    return -1


def pivot_index_optimized(nums: List[int]) -> int:
    # Time: O(n) — single pass after computing total
    # Space: O(1)
    total = sum(nums)
    left_sum = 0
    for i, num in enumerate(nums):
        if left_sum == total - left_sum - num:
            return i
        left_sum += num
    return -1
