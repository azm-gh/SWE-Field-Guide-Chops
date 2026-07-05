"""
LeetCode 76: Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/
"""

# Intuition: Variable-size sliding window with two maps. Expand right until
# the window contains all characters of t (formed == required). Then shrink
# left while the window still satisfies the condition, tracking the minimum
# length. This is the classic "minimum window" sliding window template.

from collections import Counter


def min_window_naive(s: str, t: str) -> str:
    # Time: O(n^2 * m) — check every substring, count chars in t each time
    # Space: O(m) — target dict for t
    n = len(s)
    target = Counter(t)
    min_len = float("inf")
    result = ""
    for i in range(n):
        for j in range(i, n):
            window = s[i:j + 1]
            if all(window.count(ch) >= cnt for ch, cnt in target.items()):
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    result = window
    return result


def min_window_optimized(s: str, t: str) -> str:
    # Time: O(n) — sliding window, each char visited at most twice
    # Space: O(m) — window and target dicts (m = size of t's distinct chars)
    if not s or not t:
        return ""

    target = Counter(t)
    required = len(target)
    formed = 0
    window_counts = {}
    left = 0
    min_len = float("inf")
    result = ""

    for right, ch in enumerate(s):
        window_counts[ch] = window_counts.get(ch, 0) + 1
        if ch in target and window_counts[ch] == target[ch]:
            formed += 1

        while left <= right and formed == required:
            window_len = right - left + 1
            if window_len < min_len:
                min_len = window_len
                result = s[left:right + 1]

            left_ch = s[left]
            window_counts[left_ch] -= 1
            if left_ch in target and window_counts[left_ch] < target[left_ch]:
                formed -= 1
            left += 1

    return result
