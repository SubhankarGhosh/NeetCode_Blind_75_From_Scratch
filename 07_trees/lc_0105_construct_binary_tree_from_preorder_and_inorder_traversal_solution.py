"""LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal (Reference Solution)

Problem URL: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Difficulty: Medium
Category: Trees

Complexity Analysis:
- Time Complexity: O(n) where n is the number of nodes.
  Building the hash map takes O(n). Each recursive call constructs one tree node in O(1)
  time via constant-time index lookups, avoiding costly O(n) array slice copies.
- Space Complexity: O(n) to store the hash map and handle the recursion call stack.
"""

from __future__ import annotations
from typing import Optional, List, Dict
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_traversals(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """Reconstructs a binary tree from preorder and inorder sequences in linear O(n) time."""
    in_map: Dict[int, int] = {val: i for i, val in enumerate(inorder)}
    pre_idx = 0

    def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
        nonlocal pre_idx
        if in_left > in_right:
            return None

        val = preorder[pre_idx]
        pre_idx += 1
        root = TreeNode(val)
        mid = in_map[val]

        # Inorder elements left of mid belong to left subtree; right belong to right subtree
        root.left = helper(in_left, mid - 1)
        root.right = helper(mid + 1, in_right)

        return root

    return helper(0, len(inorder) - 1)


# =====================================================================
# Offline Test Harness & Helpers
# =====================================================================
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    res = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    return res


if __name__ == "__main__":
    test_cases = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1]),
        ([1, 2, 3], [2, 1, 3], [1, 2, 3]),
        ([1, 2], [2, 1], [1, 2]),
        ([1, 2], [1, 2], [1, None, 2]),
    ]

    print("Running verification for lc_0105_construct_binary_tree_from_preorder_and_inorder_traversal_solution.py...")
    for idx, (pre, inord, expected) in enumerate(test_cases, 1):
        tree = build_tree_from_traversals(list(pre), list(inord))
        result = tree_to_list(tree)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
