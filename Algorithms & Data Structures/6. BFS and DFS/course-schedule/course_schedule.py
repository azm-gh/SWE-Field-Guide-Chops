"""
LeetCode 207: Course Schedule
https://leetcode.com/problems/course-schedule/
"""

# Intuition: Detect cycle in a directed graph. DFS with states (unvisited,
# in-progress, done) detects back edges that indicate cycles. BFS (Kahn's
# algorithm) removes nodes with 0 indegree; if all nodes are processed, there's
# no cycle. Both are valid for topological ordering problems.

from typing import List
from collections import deque


def can_finish_dfs_naive(num_courses: int, prerequisites: List[List[int]]) -> bool:
    # Time: O(V+E) — DFS visits each node and edge once
    # Space: O(V+E) — adjacency list + recursion stack up to V
    graph = [[] for _ in range(num_courses)]
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    state = [0] * num_courses

    def has_cycle(v):
        if state[v] == 1:
            return True
        if state[v] == 2:
            return False
        state[v] = 1
        for nbr in graph[v]:
            if has_cycle(nbr):
                return True
        state[v] = 2
        return False

    for v in range(num_courses):
        if has_cycle(v):
            return False
    return True


def can_finish_bfs_optimized(num_courses: int, prerequisites: List[List[int]]) -> bool:
    # Time: O(V+E) — Kahn's algorithm processes each node and edge once
    # Space: O(V+E) — adjacency list + indegree array + queue
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    q = deque([v for v in range(num_courses) if indegree[v] == 0])
    count = 0
    while q:
        v = q.popleft()
        count += 1
        for nbr in graph[v]:
            indegree[nbr] -= 1
            if indegree[nbr] == 0:
                q.append(nbr)
    return count == num_courses
