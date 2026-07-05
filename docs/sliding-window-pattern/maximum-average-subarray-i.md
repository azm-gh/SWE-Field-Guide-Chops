# Maximum Average Subarray I

**LeetCode:** [https://leetcode.com/problems/maximum-average-subarray-i/](https://leetcode.com/problems/maximum-average-subarray-i/)
**AlgoMaster Animation:** [https://algomaster.io/animations/dsa/maximum-average-subarray-i](https://algomaster.io/animations/dsa/maximum-average-subarray-i)

## Intuition

Intuition: Fixed-size sliding window. Since k is constant, we slide a window
of size k across the array, subtracting the outgoing element and adding the
incoming one. This maintains the window sum in O(1) per step instead of
recalculating from scratch O(n*k).

## Solutions

### `find_max_average_naive` — Naive

```python
def find_max_average_naive(nums: List[int], k: int) -> float:
    # Time: O(n*k) — recompute sum for each window start
    # Space: O(1)
    n = len(nums)
    max_avg = float("-inf")
    for i in range(n - k + 1):
        total = 0
        for j in range(i, i + k):
            total += nums[j]
        max_avg = max(max_avg, total / k)
    return max_avg
```

### `find_max_average_optimized` — Optimized

```python
def find_max_average_optimized(nums: List[int], k: int) -> float:
    # Time: O(n) — sliding window O(1) per step after initial sum
    # Space: O(1)
    n = len(nums)
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, n):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum / k
```

#### Analogy: The "Bus Passengers" Analogy
Imagine a bus that can hold exactly `k` passengers (our fixed window size). As the bus drives along a road (the array of numbers), people stand in a line.

To find the segment of `k` consecutive people with the highest average weight, we use a rolling calculation:

* **The First Bus Load**: We load the first `k` people onto the bus at the starting terminal (`nums[:k]`). We sum up their weights. This is our initial record to beat.
* **Driving Forward**: At each subsequent stop along the road, one new person is waiting to get on the bus (`nums[i]`), and the person who has been on the bus the longest must exit the bus (`nums[i - k]`).
* **Updating the Total (O(1) updates)**: Instead of weighing all `k` people on the bus from scratch at every stop, we simply take our current total weight, add the weight of the new person getting on, and subtract the weight of the person getting off: `window_sum += incoming - outgoing`.
* **Recording the Record**: We compare this new total weight to our all-time record (`max_sum = max(max_sum, window_sum)`).
* **The Final Average**: After driving to the end of the line, we take the highest total weight found and divide it by `k` to get the maximum average weight.
