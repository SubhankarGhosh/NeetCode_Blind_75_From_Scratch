"""LeetCode 102: Binary Tree Level Order Traversal (Reference Solution)

Problem URL: https://leetcode.com/problems/binary-tree-level-order-traversal/
Difficulty: Medium
Category: Trees

Complexity Analysis:
- Time Complexity: O(n) where n is the number of nodes in the binary tree.
  Each node is enqueued and dequeued exactly once.
- Space Complexity: O(w) auxiliary space where w is the maximum width of the tree.
  In a full balanced binary tree, the leaf level contains ceil(n / 2) nodes,
  making queue memory O(n).
"""

from __future__ import annotations
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """Performs level-order BFS traversal, partitioning nodes into per-level arrays."""
    if not root:
        return []

    res: List[List[int]] = []
    q: deque[TreeNode] = deque([root])

    while q:
        level: List[int] = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)

    return res


# =====================================================================
# Offline Test Harness & Helpers
# =====================================================================
def build_tree(vals: List[Optional[int]]) -> Optional[TreeNode]:
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    queue = deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),
        ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]),
    ]

    print("Running verification for lc_0102_binary_tree_level_order_traversal_solution.py...")
    for idx, (vals, expected) in enumerate(test_cases, 1):
        tree = build_tree(vals)
        result = level_order(tree)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
