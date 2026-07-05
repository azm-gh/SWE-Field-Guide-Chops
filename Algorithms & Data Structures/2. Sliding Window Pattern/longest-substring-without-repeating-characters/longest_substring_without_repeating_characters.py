"""
LeetCode 3: Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


# Intuition: Variable-size sliding window. Expand right pointer to add new
# characters. When a repeat is found, shrink left pointer past the previous
# occurrence. The window always contains unique characters, tracked by a dict
# mapping character to its last seen index. This gives O(n) instead of O(n^2).


def length_of_longest_substring_naive(s: str) -> int:
    # Time: O(n^2) — check every substring from each start
    # Space: O(min(n, m)) — set stores window chars (m = alphabet size)
    n = len(s)
    max_len = 0
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)
    return max_len


def length_of_longest_substring_optimized(s: str) -> int:
    # Time: O(n) — each char visited once by left/right pointers
    # Space: O(min(n, m)) — dict stores last index of each char (m = alphabet size)
    char_index = {}
    left = 0
    max_len = 0
    for right, ch in enumerate(s):
        if ch in char_index and char_index[ch] >= left:
            left = char_index[ch] + 1
        char_index[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len


# #### Analogy: The "VIP Guest List" Analogy
# Imagine you are hosting a high-end party where only unique individuals can attend (no duplicate names allowed). You have a line of guests waiting outside (the string `s`).
# 
# To find the longest continuous sequence of guests that can be in the venue at once:
# 
# * **The Entrance (Right Pointer)**: You stand at the door, letting guests in one by one. As each guest enters (`ch` at index `right`), you write down their name and the exact time/index they entered (`char_index[ch] = right`).
# * **The Double-Entry Alert**: Suddenly, a guest named Bob arrives at the door. You check your guest log (`char_index`) and see Bob is already inside!
# * **Shrinking the Venue (Left Pointer)**: You cannot have two Bobs at the same time. You look at where the original Bob is standing in the queue (`char_index['Bob']`). To resolve the conflict, you must immediately eject everyone from the back of the venue up to and including the original Bob. You do this by moving your boundary (`left`) to the spot right after the original Bob's index: `left = char_index[ch] + 1`. (If the original Bob was already ejected during a previous conflict, you do nothing).
# * **Recording the Size**: At each step, once the venue has only unique guests, you measure the length of the crowd (`right - left + 1`) and record the peak attendance (`max_len`).

