"""
LeetCode 74: Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
"""

# Intuition: Binary search on a 2D matrix treated as flattened sorted 1D array.
# Map mid index to row = mid // n and col = mid % n. Since each row is sorted
# and the first element of each row > last of previous, the entire matrix is
# row-major sorted. Standard binary search applies.

from typing import List


def search_matrix_naive(matrix: List[List[int]], target: int) -> bool:
    # Time: O(m*n) — scan every element in the matrix
    # Space: O(1)
    for row in matrix:
        for val in row:
            if val == target:
                return True
    return False


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
