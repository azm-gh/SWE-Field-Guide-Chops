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


# #### Analogy: The "Moving Truck" Analogy
# You're moving apartments. You have a stack of boxes in a fixed order (you can't rearrange them — each box must be loaded in sequence), and you need to transport them using a rental truck. The truck has a weight limit, and you have a limited number of trips allowed.
# 
# * **The Truck Capacity (Candidate Mid)**: This is the maximum weight the truck can carry per trip. We need to find the minimum capacity that still gets the job done in the allowed trips.
# * **Fixed Order Loading**: Boxes must be loaded in sequence — you can't skip a heavy box and come back for it later. If the next box exceeds the remaining capacity, you seal the truck and send it off, then start a new trip with that box.
# * **Feasibility Check**: For a given truck capacity, simulate loading: start with trip 1, add boxes until the next one would exceed capacity, then increment the trip counter and keep going. If total trips ≤ allowed days, this capacity works.
# * **Binary Search on Answer**: The minimum possible capacity is the heaviest single box. The maximum is the sum of all boxes (one trip). Binary search this range to find the smallest capacity that fits within the trip limit — just like finding the smallest viable truck.
