# Search a 2D Matrix

**LeetCode:** [https://leetcode.com/problems/search-a-2d-matrix/](https://leetcode.com/problems/search-a-2d-matrix/)
**AlgoMaster Animation:** [https://algomaster.io/animations/dsa/search-a-2d-matrix](https://algomaster.io/animations/dsa/search-a-2d-matrix)

## Intuition

Intuition: Binary search on a 2D matrix treated as flattened sorted 1D array.
Map mid index to row = mid // n and col = mid % n. Since each row is sorted
and the first element of each row > last of previous, the entire matrix is
row-major sorted. Standard binary search applies.

## Solutions

### `search_matrix_naive` — Naive

```python
def search_matrix_naive(matrix: List[List[int]], target: int) -> bool:
    # Time: O(m*n) — scan every element in the matrix
    # Space: O(1)
    for row in matrix:
        for val in row:
            if val == target:
                return True
    return False
```

### `search_matrix_optimized` — Optimized

```python
def search_matrix_optimized(matrix: List[List[int]], target: int) -> bool:
    # Time: O(log(m*n)) — binary search on flattened matrix
    # Space: O(1)
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    while left <= right:
        mid = (left + right) // 2
        val = matrix[mid // n][mid % n]
        if val == target:
            return True
        if val < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
```

#### Analogy: The "Cinema Seat Finder" Analogy
Imagine a cinema with rows of seats, each row sorted by seat number from left to right. The rows themselves are ordered — row 2 starts where row 1 ends (no gaps). An usher has a single ticket with a seat number and needs to find it fast.

* **The Flattened Row (1D Mapping)**: Instead of walking row by row, the usher treats all seats as one continuous line from 1 to total seats. This is the key insight — the 2D grid is really one sorted list in disguise.
* **The Row & Col Calculation**: Given a "virtual index" `mid` in the flattened line, the usher computes `row = mid // (seats_per_row)` and `col = mid % (seats_per_row)` to locate the exact physical seat.
* **Standard Binary Search**: Once flattened conceptually, it's textbook binary search — compare the seat number at `mid` with the target, eliminate the wrong half, and repeat.
* **Result**: You find the target in O(log(m\*n)) time, never needing to scan every seat.
