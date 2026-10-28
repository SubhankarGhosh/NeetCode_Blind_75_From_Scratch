"""LeetCode 100: Same Tree (Reference Solution)

Problem URL: https://leetcode.com/problems/same-tree/
Difficulty: Easy
Category: Trees

Complexity Analysis:
- Time Complexity: O(min(n, m)) where n and m are the sizes of tree p and tree q.
  Early-exits at the first structural or value discrepancy.
- Space Complexity: O(min(hp, hq)) call stack memory where hp and hq are the heights of the trees.
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
    """Recursively checks structural and value equivalence between two binary trees."""
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


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
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
        ([], [], True),
        ([1], [1], True),
        ([1], [2], False),
    ]

    print("Running verification for lc_0100_same_tree_solution.py...")
    for idx, (p_vals, q_vals, expected) in enumerate(test_cases, 1):
        t1 = build_tree(p_vals)
        t2 = build_tree(q_vals)
        result = is_same_tree(t1, t2)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
