"""
LeetCode 11: Container With Most Water
https://leetcode.com/problems/container-with-most-water/
"""

# Intuition: Two-pointer from both ends works because area is limited by the
# shorter line. Moving the shorter pointer inward may find a taller line, which
# could increase area despite narrower width. We never move the taller pointer
# because that would only decrease width without potential height gain.

from typing import List


def max_area_naive(height: List[int]) -> int:
    # Time: O(n^2) — check every pair of lines
    # Space: O(1)
    n = len(height)
    max_water = 0
    for i in range(n):
        for j in range(i + 1, n):
            area = min(height[i], height[j]) * (j - i)
            max_water = max(max_water, area)
    return max_water


def max_area_optimized(height: List[int]) -> int:
    # Time: O(n) — single pass from both ends
    # Space: O(1)
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        h = min(height[left], height[right])
        w = right - left
        max_water = max(max_water, h * w)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water


# #### Analogy: The "Shrinking Swimming Pool" Analogy
# Imagine you are building a temporary swimming pool between two vertical support beams of varying heights. The water level can only go as high as the shorter of the two beams (otherwise, it spills over). The total volume of water your pool can hold depends on two factors: the distance between the beams (width) and the height of the shorter beam (limiting height).
# 
# You want to find the combination of two beams that holds the absolute maximum volume of water:
# 
# * **The Starting Point**: You start with the maximum possible width. You place one pointer on the leftmost beam (`left = 0`) and one on the rightmost beam (`right = len(height) - 1`). You calculate the water capacity.
# * **The Shrinking Dilemma**: To try other combinations, you have to move your pointers closer together, which *always* decreases the width of your pool. To compensate for the loss of width, you desperately need to find taller support beams.
# * **Choosing Which Beam to Move**:
#   * **Keep the Taller Beam**: If you move the pointer of the taller beam, you gain nothing. Even if you find a super tall beam inside, the water level is still bottlenecked by the shorter beam you kept, and since width shrank, the total volume will definitely be smaller.
#   * **Discard the Shorter Beam**: Your only hope of holding more water is to find a beam taller than your current bottleneck. Therefore, you must move the pointer pointing to the **shorter** beam inward (`left += 1` if the left is shorter, or `right -= 1` if the right is shorter), hoping to land on a taller support.
# * **Conclusion**: By always sacrificing the shorter support, you navigate the trade-off between shrinking width and potential height gains, finding the maximum volume in a single pass.

