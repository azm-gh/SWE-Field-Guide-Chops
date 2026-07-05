"""
LeetCode 104: Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

# Intuition: DFS recursion is natural for tree depth — the max depth of a node
# is 1 + max(depth of left, depth of right). BFS level-order traversal works
# too: each level processed increments depth, and we stop when the queue is
# empty. Both are O(n).

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth_dfs_naive(root: TreeNode) -> int:
    # Time: O(n) — visit every node once
    # Space: O(h) — recursion stack, h = height of tree
    if not root:
        return 0
    return 1 + max(max_depth_dfs_naive(root.left), max_depth_dfs_naive(root.right))


def max_depth_bfs_optimized(root: TreeNode) -> int:
    # Time: O(n) — visit every node once
    # Space: O(w) — queue holds at most the width of the tree
    if not root:
        return 0
    q = deque([root])
    depth = 0
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        depth += 1
    return depth
