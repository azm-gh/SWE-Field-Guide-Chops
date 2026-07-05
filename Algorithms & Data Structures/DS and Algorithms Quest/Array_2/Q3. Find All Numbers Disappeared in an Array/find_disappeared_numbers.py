"""
LeetCode 448: Find All Numbers Disappeared in an Array
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""
# Intuition: The array has values in [1, n] but some numbers are missing.
# The naive approach uses a hash set to track what's present. The optimized
# approach marks visited numbers in-place by negating the value at the
# corresponding index — numbers at unmarked indices are the missing ones.
# This achieves O(1) extra space.
# Pattern: Hashmaps / hash sets — the naive approach directly uses a set
# for "have I seen this before?" The optimized approach implements the same
# concept in-place using the array as a makeshift hash set.

from typing import List


def find_disappeared_numbers_naive(nums: List[int]) -> List[int]:
    # Time: O(n) — set construction + range scan
    # Space: O(n) — hash set
    n = len(nums)
    present = set(nums)
    result = []
    for i in range(1, n + 1):
        if i not in present:
            result.append(i)
    return result


def find_disappeared_numbers_optimized(nums: List[int]) -> List[int]:
    # Time: O(n) — index marking + second pass
    # Space: O(1) — input array reused as marker
    n = len(nums)
    for num in nums:
        idx = abs(num) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]
    result = []
    for i in range(n):
        if nums[i] > 0:
            result.append(i + 1)
    return result
