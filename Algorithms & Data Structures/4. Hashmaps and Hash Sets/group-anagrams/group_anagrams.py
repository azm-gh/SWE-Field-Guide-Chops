"""
LeetCode 49: Group Anagrams
https://leetcode.com/problems/group-anagrams/
"""

# Intuition: Anagrams have identical sorted character sequences. Use the sorted
# string as a hashmap key. All strings with the same sorted key belong to the
# same group. This is the standard hashmap categorization pattern.

from typing import List


def group_anagrams_naive(strs: List[str]) -> List[List[str]]:
    # Time: O(n^2 * k log k) — compare each pair with sorted keys (k = avg string len)
    # Space: O(n) — visited array + result
    n = len(strs)
    visited = [False] * n
    result = []
    for i in range(n):
        if visited[i]:
            continue
        group = [strs[i]]
        visited[i] = True
        for j in range(i + 1, n):
            if not visited[j] and sorted(strs[i]) == sorted(strs[j]):
                group.append(strs[j])
                visited[j] = True
        result.append(group)
    return result


def group_anagrams_optimized(strs: List[str]) -> List[List[str]]:
    # Time: O(n * k log k) — hashmap insertion with sorted key per string
    # Space: O(n * k) — hashmap stores all strings grouped by key
    groups = {}
    for s in strs:
        key = tuple(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())
