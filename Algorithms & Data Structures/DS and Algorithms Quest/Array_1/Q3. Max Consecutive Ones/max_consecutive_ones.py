"""
LeetCode 485: Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/
"""
# Intuition: Scan the array tracking the current run of 1s. When we hit a 0,
# the run resets. Keep a max of all observed runs.
# Pattern: Sliding window (variable-size) — the window is the current run
# of consecutive 1s. It expands on 1s and resets on 0s. We track the max
# window length seen.

from typing import List


def find_max_consecutive_ones_naive(nums: List[int]) -> int:
    # Time: O(n) — single scan with inner while for each run
    # Space: O(1)
    n = len(nums)
    max_len = 0
    i = 0
    while i < n:
        if nums[i] == 1:
            j = i
            while j < n and nums[j] == 1:
                j += 1
            max_len = max(max_len, j - i)
            i = j
        else:
            i += 1
    return max_len


def find_max_consecutive_ones_optimized(nums: List[int]) -> int:
    # Time: O(n) — single pass, no inner loops
    # Space: O(1)
    count = 0
    max_count = 0
    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count
