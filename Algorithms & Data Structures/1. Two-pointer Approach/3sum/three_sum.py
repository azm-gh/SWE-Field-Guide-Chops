"""
LeetCode 15: 3Sum (threesome)
https://leetcode.com/problems/3sum/
"""

# Intuition: Two-pointer after sorting. We fix one element (i) then use the
# classic two-pointer technique on the remaining sorted subarray to find pairs
# summing to -nums[i]. Sorting lets us skip duplicates easily and use the
# two-pointer convergence pattern.

from typing import List


def three_sum_naive(nums: List[int]) -> List[List[int]]:
    # Time: O(n^3) — triple nested loop over all triplets
    # Space: O(n) — set stores up to n unique triplets
    n = len(nums)
    result = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result.add(triplet)
    return [list(t) for t in result]


def three_sum_optimized(nums: List[int]) -> List[List[int]]:
    # Time: O(n^2) — two-pointer scan for each fixed element after O(n log n) sort
    # Space: O(1) — result excluded; sorting may use O(log n) stack
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return result
