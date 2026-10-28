"""LeetCode 98: Validate Binary Search Tree (Reference Solution)

Problem URL: https://leetcode.com/problems/validate-binary-search-tree/
Difficulty: Medium
Category: Trees

Complexity Analysis:
- Time Complexity: O(n) where n is the number of nodes in the binary tree.
  Every node is visited once to check its valid (low, high) range.
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


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """Validates BST properties using recursive interval boundary propagation."""
    def valid(node: Optional[TreeNode], low: float, high: float) -> bool:
        if not node:
            return True
        if not (low < node.val < high):
            return False

        return valid(node.left, low, node.val) and valid(node.right, node.val, high)

    return valid(root, float("-inf"), float("inf"))


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
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([5, 4, 6, None, None, 3, 7], False),  # 3 is in right subtree of 5!
        ([1], True),
        ([2, 2, 2], False),  # BST must be strictly less/greater
        ([10, 5, 15, None, None, 6, 20], False),
    ]

    print("Running verification for lc_0098_validate_binary_search_tree_solution.py...")
    for idx, (vals, expected) in enumerate(test_cases, 1):
        tree = build_tree(vals)
        result = is_valid_bst(tree)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
