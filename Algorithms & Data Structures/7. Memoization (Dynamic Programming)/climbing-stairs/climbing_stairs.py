"""
LeetCode 70: Climbing Stairs
https://leetcode.com/problems/climbing-stairs/
"""


# Intuition: Classic DP — Fibonacci pattern. To reach step n, you can come from
# step n-1 (one step) or step n-2 (two steps). So ways(n) = ways(n-1) + ways(n-2).
# Bottom-up DP avoids repeated subproblem computation, reducing from O(2^n) to O(n).


def climb_stairs_recursive_naive(n: int) -> int:
    # Time: O(2^n) — two recursive branches per call, exponential
    # Space: O(n) — recursion stack depth
    if n <= 2:
        return n
    return climb_stairs_recursive_naive(n - 1) + climb_stairs_recursive_naive(n - 2)


def climb_stairs_dp_optimized(n: int) -> int:
    # Time: O(n) — single loop, bottom-up Fibonacci
    # Space: O(1)
    if n <= 2:
        return n
    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr
