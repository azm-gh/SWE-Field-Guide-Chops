"""
LeetCode 424: Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/
"""


# Intuition: Variable-size sliding window. The window is valid if
# (window length - max frequency of any char) <= k. Expand right, and if the
# window becomes invalid, shrink left. The key insight: we only need to track
# the max frequency — if it wasn't the bottleneck before, it won't help now.

def character_replacement_naive(s: str, k: int) -> int:
    # Time: O(n^3) — nested loops with inner frequency rebuild
    # Space: O(1) — frequency dict bounded by alphabet size (26)
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i, n):
            freq = {}
            for m in range(i, j + 1):
                freq[s[m]] = freq.get(s[m], 0) + 1
            max_freq = max(freq.values()) if freq else 0
            window_len = j - i + 1
            if window_len - max_freq <= k:
                max_len = max(max_len, window_len)
    return max_len


def character_replacement_optimized(s: str, k: int) -> int:
    # Time: O(n) — single pass sliding window, O(1) per step
    # Space: O(1) — frequency dict bounded by alphabet size (26)
    freq = {}
    left = 0
    max_freq = 0
    max_len = 0
    for right, ch in enumerate(s):
        freq[ch] = freq.get(ch, 0) + 1
        max_freq = max(max_freq, freq[ch])
        window_len = right - left + 1
        if window_len - max_freq > k:
            freq[s[left]] -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
