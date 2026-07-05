"""
LeetCode 875: Koko Eating Bananas (Coco)
https://leetcode.com/problems/koko-eating-bananas/
"""

# Intuition: Binary search on the answer (speed k). The search space is
# [1, max(piles)]. At each mid, we check feasibility: can Koko eat all bananas
# within h hours at speed mid? If yes, try a lower speed (right = mid); if no,
# increase speed (left = mid + 1). Classical "binary search on answer" pattern.

from typing import List
import math


def min_eating_speed_naive(piles: List[int], h: int) -> int:
    # Time: O(n * range) — linear scan for each candidate speed
    # Space: O(1)
    max_speed = max(piles)
    for speed in range(1, max_speed + 1):
        total_hours = 0
        for p in piles:
            total_hours += math.ceil(p / speed)
        if total_hours <= h:
            return speed
    return max_speed


def min_eating_speed_optimized(piles: List[int], h: int) -> int:
    # Time: O(n log max(piles)) — binary search + O(n) feasibility per mid
    # Space: O(1)
    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        total_hours = 0
        for p in piles:
            total_hours += (p + mid - 1) // mid
        if total_hours <= h:
            right = mid
        else:
            left = mid + 1
    return left


# #### Analogy: The "Buffet Speed Check" Analogy
# Imagine you have a huge pile of sliced bread to toast for a party, and only one old toaster that can fit a certain number of slices per batch. You have a strict deadline.
# 
# * **The Toast Capacity (Speed k)**: This is your candidate eating speed — how many bananas Koko can eat per hour. In our analogy, it's how many bread slices you can toast per batch in the toaster.
# * **The Piles (Stacks of Bread)**: Each pile is a different size (number of bananas). You must finish one entire pile before moving to the next, just like you must toast all the slices in one stack before starting the next.
# * **The Feasibility Check**: For a given toaster capacity, you calculate how many toaster cycles each bread stack requires. If the total cycles fit within your available time (h hours), the capacity is feasible — try a smaller one.
# * **Binary Search on Answer**: Instead of testing every possible toaster capacity from 1 to the biggest stack, you binary search the range. If a mid-sized capacity works, look lower to find the minimal viable toaster; if not, you need a bigger toaster.
