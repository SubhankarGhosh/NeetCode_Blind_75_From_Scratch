"""LeetCode 104: Maximum Depth of Binary Tree (Reference Solution)

Problem URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Difficulty: Easy
Category: Trees

Complexity Analysis:
- Time Complexity: O(n) where n is the number of nodes in the binary tree.
  Every node is traversed once.
- Space Complexity: O(h) call stack memory where h is the tree height.
  O(log n) for a balanced tree, O(n) for a completely degenerate linked-list tree.
"""

from __future__ import annotations
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    """Finds maximum depth of binary tree using recursive post-order DFS."""
    if not root:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))


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
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([], 0),
        ([0], 1),
        ([1, 2, 3, 4, 5], 3),
    ]

    print("Running verification for lc_0104_maximum_depth_of_binary_tree_solution.py...")
    for idx, (vals, expected) in enumerate(test_cases, 1):
        tree = build_tree(vals)
        result = max_depth(tree)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
