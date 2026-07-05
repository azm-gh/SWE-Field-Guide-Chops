# Koko Eating Bananas (Coco)

**LeetCode:** [https://leetcode.com/problems/koko-eating-bananas/](https://leetcode.com/problems/koko-eating-bananas/)
**AlgoMaster Animation:** [https://algomaster.io/animations/dsa/koko-eating-bananas](https://algomaster.io/animations/dsa/koko-eating-bananas)

## Intuition

Intuition: Binary search on the answer (speed k). The search space is
[1, max(piles)]. At each mid, we check feasibility: can Koko eat all bananas
within h hours at speed mid? If yes, try a lower speed (right = mid); if no,
increase speed (left = mid + 1). Classical "binary search on answer" pattern.

## Solutions

### `min_eating_speed_naive` — Naive

```python
def min_eating_speed_naive(piles: List[int], h: int) -> int:
    # Time: O(n * range) — linear scan for each candidate speed
    # Space: O(1)
    max_speed = max(piles)
    for speed in range(1, max_speed + 1):
        total_hours = 0
        for p in piles:
            total_hours += math.ceil(p / speed)
        if total_hours <= h:
            return speed
    return max_speed
```

### `min_eating_speed_optimized` — Optimized

```python
def min_eating_speed_optimized(piles: List[int], h: int) -> int:
    # Time: O(n log max(piles)) — binary search + O(n) feasibility per mid
    # Space: O(1)
    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        total_hours = 0
        for p in piles:
            total_hours += (p + mid - 1) // mid
        if total_hours <= h:
            right = mid
        else:
            left = mid + 1
    return left
```
