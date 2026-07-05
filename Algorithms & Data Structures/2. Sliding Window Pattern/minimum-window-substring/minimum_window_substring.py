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


# #### Analogy: The "Recipe Shopping List" Analogy
# Imagine you are making a complex recipe that requires a specific list of ingredients and quantities, e.g., 2 eggs and 1 carton of milk (our target string `t`). You are walking down a super long grocery store aisle where products are stocked on a single long shelf (the string `s`). You want to find the shortest segment of the shelf containing all the ingredients you need.
# 
# To do this:
# 
# * **The Target List (target & required)**: You write down exactly how many of each unique item you need. The number of unique ingredients on your list is `required`.
# * **Pushing the Shopping Cart (Right Pointer)**: You start walking down the aisle, placing every item you see into your cart. If a specific ingredient in your cart now meets the required quantity (`window_counts[ch] == target[ch]`), you tick it off your list (`formed += 1`).
# * **A Complete Cart (formed == required)**: You keep walking until you have checked off all the items on your list. 
# * **Trimming the Excess (Left Pointer & while loop)**: Now that your cart is full and the recipe can be made, you want to see if you can make your trip shorter. You try to put back/discard items from the start of your path (`left_ch = s[left]`) one by one:
#   * If the discarded item is not on your recipe list, or if you still have plenty of duplicates of it in your cart, your cart is still "complete". You measure this new shorter path (`window_len < min_len`) and record it.
#   * If you discard an essential item and you no longer have enough of it in your cart (`window_counts[left_ch] < target[left_ch]`), you must untick it from your checklist (`formed -= 1`).
# * **Moving Forward**: Once your cart becomes incomplete, you stop putting items back and start pushing the cart forward again (expanding the right pointer) to search for the next copy of the missing ingredient.

