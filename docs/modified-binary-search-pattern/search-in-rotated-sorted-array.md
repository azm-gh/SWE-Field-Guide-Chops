# Search in Rotated Sorted Array

**LeetCode:** [https://leetcode.com/problems/search-in-rotated-sorted-array/](https://leetcode.com/problems/search-in-rotated-sorted-array/)
**AlgoMaster Animation:** [https://algomaster.io/animations/dsa/search-in-rotated-sorted-array](https://algomaster.io/animations/dsa/search-in-rotated-sorted-array)

## Intuition

Intuition: Modified binary search for a rotated sorted array. Even though the
array is rotated, one half (left or right of mid) is always fully sorted. We
check which half the target belongs to by comparing with the sorted half's
endpoints, and search accordingly. This preserves O(log n) time.

## Solutions

### `search_naive` — Naive

```python
def search_naive(nums: List[int], target: int) -> int:
    # Time: O(n) — linear scan
    # Space: O(1)
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1
```

### `search_optimized` — Optimized

```python
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
```
