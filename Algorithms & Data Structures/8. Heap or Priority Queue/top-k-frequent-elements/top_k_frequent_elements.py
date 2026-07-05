"""
LeetCode 347: Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/
"""

# Intuition: Count frequencies with a hashmap, then use a min-heap of size k
# to keep the k most frequent elements. The heap is ordered by frequency, so
# the least frequent among the top k is evicted when a more frequent element
# arrives. O(n log k) time.

from typing import List
from collections import Counter
import heapq


def top_k_frequent_sort_naive(nums: List[int], k: int) -> List[int]:
    # Time: O(n log n) — sort all unique elements by frequency
    # Space: O(n) — frequency map
    freq = Counter(nums)
    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_items[:k]]


def top_k_frequent_heap_optimized(nums: List[int], k: int) -> List[int]:
    # Time: O(n log k) — min-heap of size k over unique elements
    # Space: O(n) — frequency map + heap
    freq = Counter(nums)
    heap = []
    for num, count in freq.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for _, num in heap]
