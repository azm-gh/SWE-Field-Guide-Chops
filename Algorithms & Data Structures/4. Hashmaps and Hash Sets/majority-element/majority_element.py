"""
LeetCode 169: Majority Element
https://leetcode.com/problems/majority-element/
"""

# Intuition: Boyer-Moore voting algorithm works because the majority element
# appears more than n/2 times. We pair different elements together and cancel
# them out. What remains must be the majority. One pass, O(1) space.

from typing import List
from collections import Counter


def majority_element_naive(nums: List[int]) -> int:
    # Time: O(n) — hashmap frequency count
    # Space: O(n) — frequency map
    freq = Counter(nums)
    n = len(nums)
    for num, count in freq.items():
        if count > n // 2:
            return num
    return -1


def majority_element_optimized(nums: List[int]) -> int:
    # Time: O(n) — Boyer-Moore, single pass with cancelation
    # Space: O(1)
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate
