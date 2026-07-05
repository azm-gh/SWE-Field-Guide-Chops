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


# #### Analogy: The "Theme Party Wildcards" Analogy
# Imagine you are hosting a theme party where guests should ideally wear the same color (representing identical characters). However, you have exactly `k` "wildcard tickets" (replacement budget) that you can hand out to guests wearing different colors to magically change their outfit to match the majority color of the group.
# 
# To find the longest continuous group of guests you can accommodate in a single room:
# 
# * **Expanding the Guest List (Right Pointer)**: You let guests into the room one by one. You keep track of the count of each clothing color in the room (`freq`), and note the count of the most popular color present (`max_freq`).
# * **Checking the Wildcard Budget**: The total number of guests in the room is `window_len`. The number of guests wearing different/minority colors who need a wildcard ticket to match the majority is `window_len - max_freq`.
# * **Exceeding the Budget**: If the number of off-theme guests exceeds your `k` wildcard tickets (`window_len - max_freq > k`), the room is no longer valid.
# * **Shrinking the Room (Left Pointer)**: You must immediately ask the guest who has been in the room the longest (at the `left` pointer) to leave. You update your color counts (`freq[s[left]] -= 1`) and slide the boundary forward (`left += 1`).
# * **Recording Peak Crowd**: At each valid state, you check if the current room capacity is your largest group yet, and update `max_len`.

