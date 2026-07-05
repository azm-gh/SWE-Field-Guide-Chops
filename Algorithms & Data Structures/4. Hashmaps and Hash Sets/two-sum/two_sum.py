"""
LeetCode 1: Two Sum
https://leetcode.com/problems/two-sum/
"""

# Intuition: As we iterate, store each number's index in a hashmap. For each
# number, check if its complement (target - num) already exists in the map.
# If yes, we've found the pair. The hashmap gives O(1) lookup, making this
# O(n) instead of O(n^2).

from typing import List


def two_sum_naive(nums: List[int], target: int) -> List[int]:
    # Time: O(n^2) — check every pair
    # Space: O(1)
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_optimized(nums: List[int], target: int) -> List[int]:
    # Time: O(n) — hashmap lookup per element
    # Space: O(n) — hashmap stores up to n elements
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
