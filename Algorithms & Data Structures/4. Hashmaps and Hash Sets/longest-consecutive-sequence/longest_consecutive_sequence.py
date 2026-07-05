"""
LeetCode 128: Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/
"""

# Intuition: Use a hash set for O(1) lookups. A number is the start of a
# consecutive sequence only if num-1 is NOT in the set. From each start, count
# how many consecutive numbers exist. This ensures each number is visited only
# from the start of its sequence, yielding O(n) overall.

from typing import List


def longest_consecutive_naive(nums: List[int]) -> int:
    # Time: O(n^2) worst — for each num, walk forward one at a time
    # Space: O(n) — hash set
    if not nums:
        return 0
    nums_set = set(nums)
    longest = 0
    for num in nums:
        curr = num
        length = 1
        while curr + 1 in nums_set:
            curr += 1
            length += 1
        longest = max(longest, length)
    return longest


def longest_consecutive_optimized(nums: List[int]) -> int:
    # Time: O(n) — each number visited only from the start of its sequence
    # Space: O(n) — hash set
    nums_set = set(nums)
    longest = 0
    for num in nums_set:
        if num - 1 not in nums_set:
            length = 1
            while num + length in nums_set:
                length += 1
            longest = max(longest, length)
    return longest
