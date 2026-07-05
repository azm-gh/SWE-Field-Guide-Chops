# Move Zeroes

**LeetCode:** [https://leetcode.com/problems/move-zeroes/](https://leetcode.com/problems/move-zeroes/)

**AlgoMaster Animation:** [https://algomaster.io/animations/dsa/move-zeroes](https://algomaster.io/animations/dsa/move-zeroes)

## Intuition

Intuition: Two-pointer is ideal here because we need to rearrange elements
in-place while preserving relative order. The left pointer marks where the
next non-zero should go, and the right pointer scans ahead to find non-zeros.
By swapping, all zeros naturally bubble to the end.

## Solutions

### `move_zeroes_naive` — Naive

```python
def move_zeroes_naive(nums: List[int]) -> List[int]:
    # Time: O(n) — single pass, but uses extra array
    # Space: O(n) — result array
    n = len(nums)
    result = [0] * n
    idx = 0
    for num in nums:
        if num != 0:
            result[idx] = num
            idx += 1
    return result
```

### `move_zeroes_optimized` — Optimized

```python
def move_zeroes_optimized(nums: List[int]) -> None:
    # Time: O(n) — single pass, in-place swaps
    # Space: O(1)
    n = len(nums)
    left = 0
    for right in range(n):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
```

#### Analogy: The "Conveyor Belt Organizer" Analogy
Imagine you are managing a conveyor belt containing packages. Some packages are valuable items (non-zero numbers), and some are empty cardboard boxes (zeroes) that need to be pushed to the very end of the belt. You need to keep the valuable items in their original relative order.

To do this efficiently in-place, you use two pointers:

* **The Organizer (Left Pointer)**: This pointer marks the next slot on the conveyor belt where a valuable package belongs. It starts at index 0.
* **The Scanner (Right Pointer)**: This pointer moves forward, scanning each package one by one from left to right.
* **The Sorting Process**:
  * **Scanning an Empty Box (Zero)**: The Scanner passes right over it and does nothing. The Organizer stays put, waiting for a real package to fill its spot.
  * **Scanning a Valuable Package (Non-Zero)**: The Scanner finds a valuable package. To move it forward, the Scanner swaps this package with the package at the Organizer's position (which is currently occupied by a zero or is the same position).
  * **Advancing the Organizer**: Since the Organizer's spot has now been successfully filled with a valuable package, the Organizer steps forward to the next spot (`left += 1`).
* **Result**: As the Scanner finishes traversing the belt, all valuable items have been shifted forward in order, and all empty boxes (zeroes) have been naturally swapped/pushed to the back.

