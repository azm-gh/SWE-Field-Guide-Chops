# Two Sum II - Input Array Is Sorted

**LeetCode:** [https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
**AlgoMaster Animation:** [https://algomaster.io/animations/dsa/two-sum-ii-input-array-is-sorted](https://algomaster.io/animations/dsa/two-sum-ii-input-array-is-sorted)

## Intuition

Intuition: Two-pointer works because the array is sorted. Starting with one
pointer at each end, we can adjust the sum: if the sum is too small, move the
left pointer right (increase sum); if too large, move the right pointer left
(decrease sum). We converge toward the target in O(n) time.

## Solutions

### `two_sum_naive` — Naive

```python
def two_sum_naive(numbers: List[int], target: int) -> List[int]:
    # Time: O(n^2) — check every pair
    # Space: O(1)
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
    return []
```

### `two_sum_optimized` — Optimized

```python
def two_sum_optimized(numbers: List[int], target: int) -> List[int]:
    # Time: O(n) — two-pointer converges in one pass (array is sorted)
    # Space: O(1)
    left, right = 0, len(numbers) - 1
    while left < right:
        curr = numbers[left] + numbers[right]
        if curr == target:
            return [left + 1, right + 1]
        if curr < target:
            left += 1
        else:
            right -= 1
    return []
```

#### Analogy: The "Gift Card" Analogy
Imagine you have a gift card for exactly $100 (your target), and you are looking at a catalog of items where the prices are listed in order from cheapest to most expensive (your sorted numbers array). You have to buy exactly two items, and you want to use exactly the full $100.

Here is how you would use your fingers to find the perfect two items:

* **The Starting Point**: You place your left finger on the absolute cheapest item (index 0) and your right finger on the absolute most expensive item (index `len(numbers) - 1`).
* **Checking the Price (curr)**: You add the prices under your two fingers together.
* **Too Cheap (curr < target)**: If your total is, say, $80, you need to spend more money. Moving your right finger is useless because it would only point to something cheaper, lowering your total even more. The only logical move is to slide your left finger up to the next slightly more expensive item (`left += 1`).
* **Too Expensive (curr > target)**: If your total is $120, you went over budget. Moving your left finger to a more expensive item will only make things worse. You have to lower your total, so you slide your right finger down to a slightly cheaper item (`right -= 1`).
* **The Perfect Match (curr == target)**: You hit exactly $100! You return the item numbers (adding +1 because the problem asks for 1-based indexing instead of 0-based).
