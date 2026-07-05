"""
LeetCode 1011: Capacity To Ship Packages Within D Days
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
"""

# Intuition: Binary search on answer. The capacity must be at least the heaviest
# package and at most the sum of all weights. Binary search within this range.
# For each candidate capacity mid, simulate shipping in order and count days.
# If within D days, try lower capacity; otherwise increase.

from typing import List


def ship_within_days_naive(weights: List[int], days: int) -> int:
    # Time: O(n * range) — linear scan for each candidate capacity
    # Space: O(1)
    left, right = max(weights), sum(weights)
    for cap in range(left, right + 1):
        total = 0
        d = 1
        for w in weights:
            if total + w > cap:
                d += 1
                total = w
            else:
                total += w
        if d <= days:
            return cap
    return right


def ship_within_days_optimized(weights: List[int], days: int) -> int:
    # Time: O(n log range) — binary search + O(n) feasibility check per mid
    # Space: O(1)
    left, right = max(weights), sum(weights)
    while left < right:
        mid = (left + right) // 2
        total = 0
        d = 1
        for w in weights:
            if total + w > mid:
                d += 1
                total = w
            else:
                total += w
        if d <= days:
            right = mid
        else:
            left = mid + 1
    return left
