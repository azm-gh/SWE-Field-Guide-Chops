"""
LeetCode 643: Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/
"""

# Intuition: Fixed-size sliding window. Since k is constant, we slide a window
# of size k across the array, subtracting the outgoing element and adding the
# incoming one. This maintains the window sum in O(1) per step instead of
# recalculating from scratch O(n*k).

from typing import List


def find_max_average_naive(nums: List[int], k: int) -> float:
    # Time: O(n*k) — recompute sum for each window start
    # Space: O(1)
    n = len(nums)
    max_avg = float("-inf")
    for i in range(n - k + 1):
        total = 0
        for j in range(i, i + k):
            total += nums[j]
        max_avg = max(max_avg, total / k)
    return max_avg


def find_max_average_optimized(nums: List[int], k: int) -> float:
    # Time: O(n) — sliding window O(1) per step after initial sum
    # Space: O(1)
    n = len(nums)
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, n):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum / k
