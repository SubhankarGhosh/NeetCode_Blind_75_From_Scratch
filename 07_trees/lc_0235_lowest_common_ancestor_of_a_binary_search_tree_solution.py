"""LeetCode 235: Lowest Common Ancestor of a Binary Search Tree (Reference Solution)

Problem URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Difficulty: Medium
Category: Trees

Complexity Analysis:
- Time Complexity: O(h) where h is the height of the BST.
  Each iteration eliminates half of the tree in balanced BSTs (O(log n)),
  taking at most O(n) in a degenerate tree.
- Space Complexity: O(1) auxiliary space as the search is performed iteratively
  without recursion or stack frames.
"""

from __future__ import annotations
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """Finds LCA in a BST using iterative directional navigation."""
    curr = root

    while curr:
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left
        else:
            # Split point: one node is left, one is right, or curr is p or q
            return curr

    return None


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


def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


if __name__ == "__main__":
    test_cases = [
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
        ([2, 1], 2, 1, 2),
    ]

    print("Running verification for lc_0235_lowest_common_ancestor_of_a_binary_search_tree_solution.py...")
    for idx, (vals, p_val, q_val, expected_val) in enumerate(test_cases, 1):
        tree = build_tree(vals)
        p_node = find_node(tree, p_val)
        q_node = find_node(tree, q_val)
        lca = lowest_common_ancestor(tree, p_node, q_node)
        assert lca is not None and lca.val == expected_val, f"Case {idx} failed: got {lca.val if lca else None}, expected {expected_val}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
