# Find the Duplicate Number

**LeetCode:** [https://leetcode.com/problems/find-the-duplicate-number/](https://leetcode.com/problems/find-the-duplicate-number/)
**AlgoMaster Animation:** [https://algomaster.io/animations/dsa/find-the-duplicate-number](https://algomaster.io/animations/dsa/find-the-duplicate-number)

## Intuition

Intuition: The array values (1..n) act as linked list pointers into the
array indices by value. Since there's a duplicate, it creates a cycle.
Floyd's cycle detection (tortoise and hare) finds the cycle entrance,
which is the duplicate value. O(n) time, O(1) space — no extra hashmap needed.

## Solutions

### `find_duplicate_naive` — Naive

```python
def find_duplicate_naive(nums: List[int]) -> int:
    # Time: O(n) — single pass with hash set lookups
    # Space: O(n) — set stores up to n elements
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1
```

### `find_duplicate_optimized` — Optimized

```python
def find_duplicate_optimized(nums: List[int]) -> int:
    # Time: O(n) — Floyd's cycle detection, at most 2n steps
    # Space: O(1)
    slow = 0
    fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
```
