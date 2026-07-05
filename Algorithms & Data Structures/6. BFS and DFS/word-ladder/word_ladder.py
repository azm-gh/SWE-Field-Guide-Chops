"""
LeetCode 127: Word Ladder
https://leetcode.com/problems/word-ladder/
"""

# Intuition: Shortest path in an unweighted graph = BFS. Each word is a node,
# edges connect words differing by one letter. BFS finds shortest path from
# beginWord to endWord. Bidirectional BFS meets in the middle, reducing the
# branching factor from O(26^L) to ~O(2 * 26^(L/2)).

from typing import List
from collections import deque


def ladder_length_bfs_naive(begin_word: str, end_word: str, word_list: List[str]) -> int:
    # Time: O(n * L * 26) — BFS explores up to n nodes, each generates 26*L neighbors
    # Space: O(n) — word set + queue
    word_set = set(word_list)
    if end_word not in word_set:
        return 0

    q = deque([(begin_word, 1)])
    while q:
        word, length = q.popleft()
        if word == end_word:
            return length
        for i in range(len(word)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                nxt = word[:i] + ch + word[i + 1:]
                if nxt in word_set:
                    word_set.remove(nxt)
                    q.append((nxt, length + 1))
    return 0


def ladder_length_bidirectional_optimized(begin_word: str, end_word: str, word_list: List[str]) -> int:
    # Time: O(n * L * 26) — bidirectional halves search depth
    # Space: O(n) — two frontier sets + word set
    word_set = set(word_list)
    if end_word not in word_set:
        return 0

    forward = {begin_word}
    backward = {end_word}
    word_set.discard(begin_word)
    word_set.discard(end_word)
    length = 1

    while forward and backward:
        if len(forward) > len(backward):
            forward, backward = backward, forward
        next_set = set()
        for word in forward:
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    nxt = word[:i] + ch + word[i + 1:]
                    if nxt in backward:
                        return length + 1
                    if nxt in word_set:
                        word_set.remove(nxt)
                        next_set.add(nxt)
        forward = next_set
        length += 1
    return 0
