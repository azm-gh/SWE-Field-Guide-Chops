"""
LeetCode 1046: Last Stone Weight
https://leetcode.com/problems/last-stone-weight/
"""

# Intuition: Max heap — always smash the two heaviest stones. Python's heapq
# is a min-heap, so store negative values to simulate max-heap. Repeatedly pop
# two largest, smash them, and push back if any weight remains. O(n log n).

from typing import List
import heapq


def last_stone_weight_sort_naive(stones: List[int]) -> int:
    # Time: O(n^2 log n) — sort each iteration (n times)
    # Space: O(n) — copy of array
    stones = stones[:]
    while len(stones) > 1:
        stones.sort()
        y = stones.pop()
        x = stones.pop()
        if x != y:
            stones.append(y - x)
    return stones[0] if stones else 0


def last_stone_weight_heap_optimized(stones: List[int]) -> int:
    # Time: O(n log n) — heap operations, each pop/push is O(log n)
    # Space: O(n) — heap stores all stones
    heap = [-s for s in stones]
    heapq.heapify(heap)
    while len(heap) > 1:
        y = -heapq.heappop(heap)
        x = -heapq.heappop(heap)
        if x != y:
            heapq.heappush(heap, -(y - x))
    return -heap[0] if heap else 0
