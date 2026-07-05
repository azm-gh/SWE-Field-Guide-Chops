"""
LeetCode 645: Set Mismatch
https://leetcode.com/problems/set-mismatch/
"""
# Intuition: The array contains numbers from 1 to n, but one is duplicated
# and one is missing. The naive approach uses a frequency count. The
# optimized approach uses the math property: sum(nums) - sum(set(nums))
# gives the duplicate, and sum(1..n) - sum(set(nums)) gives the missing.
# Pattern: Hashmaps / hash sets — frequency counting matches the "counting
# frequencies" signal from the hashmap pattern.

from typing import List


def find_error_nums_naive(nums: List[int]) -> List[int]:
    # Time: O(n) — frequency array counting
    # Space: O(n) — frequency array
    n = len(nums)
    freq = [0] * (n + 1)
    for num in nums:
        freq[num] += 1
    duplicate = missing = -1
    for i in range(1, n + 1):
        if freq[i] == 2:
            duplicate = i
        elif freq[i] == 0:
            missing = i
    return [duplicate, missing]


def find_error_nums_optimized(nums: List[int]) -> List[int]:
    # Time: O(n) — set construction + arithmetic
    # Space: O(n) — set of nums
    n = len(nums)
    set_sum = sum(set(nums))
    actual_sum = sum(nums)
    expected_sum = n * (n + 1) // 2
    duplicate = actual_sum - set_sum
    missing = expected_sum - set_sum
    return [duplicate, missing]
