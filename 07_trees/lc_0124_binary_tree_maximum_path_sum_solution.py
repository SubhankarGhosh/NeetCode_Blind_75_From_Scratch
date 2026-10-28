"""LeetCode 124: Binary Tree Maximum Path Sum (Reference Solution)

Problem URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/
Difficulty: Hard
Category: Trees

Complexity Analysis:
- Time Complexity: O(n) where n is the number of nodes in the binary tree.
  A single post-order DFS traversal visits every node once.
- Space Complexity: O(h) recursion stack frames where h is tree height.
"""

from __future__ import annotations
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: Optional[TreeNode]) -> int:
    """Computes global maximum path sum using post-order DFS with branch clamping."""
    max_val = float("-inf")

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal max_val
        if not node:
            return 0

        # Calculate max branch contributions; clamp negatives to 0 (ignore bad branches)
        left_gain = max(0, dfs(node.left))
        right_gain = max(0, dfs(node.right))

        # Evaluate path sum where current node acts as the bridge/apex
        split_path = node.val + left_gain + right_gain
        if split_path > max_val:
            max_val = split_path

        # Return single best continuous branch upward to parent
        return node.val + max(left_gain, right_gain)

    dfs(root)
    return int(max_val)


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
        ([1, 2, 3], 6),
        ([-10, 9, 20, None, None, 15, 7], 42),
        ([-3], -3),
        ([2, -1], 2),
        ([1, -2, 3], 4),
        ([-2, 1], 1),
    ]

    print("Running verification for lc_0124_binary_tree_maximum_path_sum_solution.py...")
    for idx, (vals, expected) in enumerate(test_cases, 1):
        tree = build_tree(vals)
        result = max_path_sum(tree)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
