"""
LeetCode 33: Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

# Intuition: Modified binary search for a rotated sorted array. Even though the
# array is rotated, one half (left or right of mid) is always fully sorted. We
# check which half the target belongs to by comparing with the sorted half's
# endpoints, and search accordingly. This preserves O(log n) time.

from typing import List


def search_naive(nums: List[int], target: int) -> int:
    # Time: O(n) — linear scan
    # Space: O(1)
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1


def search_optimized(nums: List[int], target: int) -> int:
    # Time: O(log n) — binary search with rotated half detection
    # Space: O(1)
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


# #### Analogy: The "Broken Bookshelf" Analogy
# Imagine a long bookshelf where all the books are sorted by title. Someone picked up a random chunk of the shelf and moved it to the front, so now the shelf is rotated — there's a "break point" where the sequence resets.
# 
# * **The Break Point**: This is where the sorted order jumps (e.g., `[5, 6, 1, 2, 3]` — the break is after 6). Only one side of any midpoint contains this break.
# * **The Sorted Half Trick**: Pick the middle book. The left side (from `left` to `mid`) will be fully sorted if `nums[left] <= nums[mid]`. Otherwise, the right side is fully sorted. You always know exactly which half is reliably ordered.
# * **Narrowing the Search**: If the left half is sorted and your target falls within its range, search left. Otherwise search right. Same logic applies symmetrically for a sorted right half.
# * **Result**: Despite the rotation, you still narrow the search by half each step — giving O(log n) time, just like standard binary search.
