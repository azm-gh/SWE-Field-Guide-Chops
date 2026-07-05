"""
LeetCode 1470: Shuffle the Array
https://leetcode.com/problems/shuffle-the-array/
"""
# Intuition: The array has 2n elements: [x1, x2, ..., xn, y1, y2, ..., yn].
# The result should be [x1, y1, x2, y2, ..., xn, yn]. We interleave the
# first n elements with the last n elements.
# Pattern: Two-pointer approach — we use two pointers, one at i (x-half)
# and one at i + n (y-half), advancing together to interleave the sequences.

from typing import List


def shuffle_naive(nums: List[int], n: int) -> List[int]:
    # Time: O(n) — single pass, one append per element
    # Space: O(n) — result array
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i + n])
    return result


def shuffle_optimized(nums: List[int], n: int) -> List[int]:
    # Time: O(n) — single pass, direct index assignment
    # Space: O(n) — pre-allocated result array
    result = [0] * (2 * n)
    for i in range(n):
        result[2 * i] = nums[i]
        result[2 * i + 1] = nums[i + n]
    return result
