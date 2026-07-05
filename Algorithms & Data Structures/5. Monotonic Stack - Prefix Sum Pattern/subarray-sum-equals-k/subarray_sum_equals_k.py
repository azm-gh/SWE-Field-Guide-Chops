"""
LeetCode 560: Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/
"""

# Intuition: Prefix sum with hashmap. A subarray sum equals k when
# prefix[j] - prefix[i-1] = k, i.e., prefix[i-1] = prefix[j] - k.
# As we build the prefix sum, check if (current_prefix - k) has been seen
# before; the count of such occurrences is the number of subarrays ending here.

from typing import List


def subarray_sum_naive(nums: List[int], k: int) -> int:
    # Time: O(n^2) — enumerate all subarrays
    # Space: O(1)
    n = len(nums)
    count = 0
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total == k:
                count += 1
    return count


def subarray_sum_optimized(nums: List[int], k: int) -> int:
    # Time: O(n) — hashmap of prefix sums for O(1) lookup
    # Space: O(n) — hashmap stores prefix frequency
    prefix_sum = {0: 1}
    total = 0
    count = 0
    for num in nums:
        total += num
        if total - k in prefix_sum:
            count += prefix_sum[total - k]
        prefix_sum[total] = prefix_sum.get(total, 0) + 1
    return count
