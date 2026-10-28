"""LeetCode 572: Subtree of Another Tree (Reference Solution)

Problem URL: https://leetcode.com/problems/subtree-of-another-tree/
Difficulty: Easy
Category: Trees

Complexity Analysis:
- Time Complexity: O(n * m) in the worst case (e.g. skewed trees with identical values),
  where n is the number of nodes in root and m is the number of nodes in subRoot.
  On average for balanced trees, runtime approaches O(n).
- Space Complexity: O(h) recursion stack frames where h is the height of root.
"""

from __future__ import annotations
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """Helper: Verifies if two trees are structurally and value identical."""
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def is_subtree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
    """Checks if sub_root is an identical subtree within root."""
    if not sub_root:
        return True
    if not root:
        return False

    if is_same_tree(root, sub_root):
        return True

    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)


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
        ([3, 4, 5, 1, 2], [4, 1, 2], True),
        ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False),
        ([1, 1], [1], True),
        ([1, 2, 3], [2], True),
        ([1, 2, 3], [4], False),
    ]

    print("Running verification for lc_0572_subtree_of_another_tree_solution.py...")
    for idx, (r_vals, s_vals, expected) in enumerate(test_cases, 1):
        r = build_tree(r_vals)
        s = build_tree(s_vals)
        result = is_subtree(r, s)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
