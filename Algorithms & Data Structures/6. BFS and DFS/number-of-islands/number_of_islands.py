"""
LeetCode 200: Number of Islands
https://leetcode.com/problems/number-of-islands/
"""

# Intuition: Grid traversal problem — each '1' is a node in a graph (4-dir
# neighbors). DFS recursively floods all connected land, BFS uses a queue.
# Every time we start a new traversal from an unvisited '1', we've found a new
# island. Both approaches are O(m * n).

from typing import List
from collections import deque


def num_islands_dfs_naive(grid: List[List[str]]) -> int:
    # Time: O(m*n) — each cell visited at most once
    # Space: O(m*n) — recursion stack in worst case (all land)
    if not grid:
        return 0

    def dfs(r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)
    return count


def num_islands_bfs_optimized(grid: List[List[str]]) -> int:
    # Time: O(m*n) — each cell visited at most once
    # Space: O(min(m,n)) — queue holds at most the grid's diagonal
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    count = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == "1":
                count += 1
                q = deque([(r, c)])
                grid[r][c] = "0"
                while q:
                    cr, cc = q.popleft()
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                            grid[nr][nc] = "0"
                            q.append((nr, nc))
    return count
