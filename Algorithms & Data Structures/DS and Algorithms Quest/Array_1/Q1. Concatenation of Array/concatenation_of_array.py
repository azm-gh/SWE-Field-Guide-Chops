"""
LeetCode 1929: Concatenation of Array
https://leetcode.com/problems/concatenation-of-array/
"""
# Intuition: The problem asks to create an array where ans[i] == nums[i]
# and ans[i + n] == nums[i] for i in [0, n). This is simply the array
# repeated twice. No specific pattern from the 8 — this is a warm-up
# problem focused on basic array allocation and indexing.
# The naive approach appends each element one by one;
# the optimized approach uses Python's list multiplication or extend.

from typing import List


def get_concatenation_naive(nums: List[int]) -> List[int]:
    # Time: O(n) — single pass filling result
    # Space: O(n) — result array (2n)
    n = len(nums)
    ans = [0] * (2 * n)
    for i in range(n):
        ans[i] = nums[i]
        ans[i + n] = nums[i]
    return ans


def get_concatenation_optimized(nums: List[int]) -> List[int]:
    # Time: O(n) — list concatenation copies all elements
    # Space: O(n) — result array (2n)
    return nums + nums
