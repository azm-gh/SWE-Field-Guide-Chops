"""
LeetCode 215: Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/
"""

# Intuition: Min-heap of size k. Maintain the k largest elements seen so far.
# The smallest among them (heap root) is the kth largest. For each new element,
# if it's larger than the root, pop root and push the new element. O(n log k).

from typing import List
import heapq


def find_kth_largest_sort_naive(nums: List[int], k: int) -> int:
    # Time: O(n log n) — full sort
    # Space: O(1) — sort in-place (TimSort uses O(n) in worst case)
    return sorted(nums, reverse=True)[k - 1]


def find_kth_largest_heap_optimized(nums: List[int], k: int) -> int:
    # Time: O(n log k) — min-heap of size k, single pass
    # Space: O(k) — heap
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    return heap[0]
