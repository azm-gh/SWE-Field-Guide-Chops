"""
LeetCode 283: Move Zeroes
https://leetcode.com/problems/move-zeroes/
"""

# Intuition: Two-pointer is ideal here because we need to rearrange elements
# in-place while preserving relative order. The left pointer marks where the
# next non-zero should go, and the right pointer scans ahead to find non-zeros.
# By swapping, all zeros naturally bubble to the end.

from typing import List


def move_zeroes_naive(nums: List[int]) -> List[int]:
    # Time: O(n) — single pass, but uses extra array
    # Space: O(n) — result array
    n = len(nums)
    result = [0] * n
    idx = 0
    for num in nums:
        if num != 0:
            result[idx] = num
            idx += 1
    return result


def move_zeroes_optimized(nums: List[int]) -> None:
    # Time: O(n) — single pass, in-place swaps
    # Space: O(1)
    n = len(nums)
    left = 0
    for right in range(n):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
