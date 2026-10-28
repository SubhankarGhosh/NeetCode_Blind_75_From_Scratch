"""LeetCode 235: Lowest Common Ancestor of a Binary Search Tree (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Difficulty: Medium
Category: Trees

Pattern Context:
    The Lowest Common Ancestor (LCA) of two nodes p and q in a BST is the lowest node
    that has both p and q as descendants (where a node can be a descendant of itself).
    BST Ordering Invariant:
    - If both p.val and q.val are strictly greater than curr.val:
      Both nodes reside in the right subtree -> descend right (`curr = curr.right`).
    - If both p.val and q.val are strictly less than curr.val:
      Both nodes reside in the left subtree -> descend left (`curr = curr.left`).
    - Otherwise (split point):
      One node lies to the left, one to the right, or curr matches p or q.
      `curr` is uniquely the Lowest Common Ancestor!

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 07_trees/lc_0235_lowest_common_ancestor_of_a_binary_search_tree_compact.py
"""

from __future__ import annotations
from typing import Optional, List
from collections import deque

# Sentinel placeholder for exercise tasks
TODO = None


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """Finds the LCA of nodes p and q in a BST in O(h) time and O(1) space.

    Algorithmic Requirements:
    - Time Complexity: O(h) where h is tree height.
    - Space Complexity: O(1) auxiliary space (iterative traversal).

    Steps to implement:
    1. Initialize `curr = root`.
    2. While `curr`:
       - If `p.val > curr.val and q.val > curr.val`:
         * `curr = curr.right`
       - Else if `p.val < curr.val and q.val < curr.val`:
         * `curr = curr.left`
       - Else:
         * Return `curr` (the split point).
    3. Return None.

    -------------------------------------------------------------------------
    TODO: Implement iterative BST LCA search below.
    -------------------------------------------------------------------------
    """
    curr = root

    while curr:
        # <<< YOUR CODE HERE >>>
        # Hint: If both values > curr.val, go right; if both < curr.val, go left; else return curr
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left
        else:
            split_node = TODO  # Replace with: curr
            if split_node is None:
                raise NotImplementedError("TODO: Return split LCA node.")
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

    print("Running verification for lc_0235_lowest_common_ancestor_of_a_binary_search_tree_compact.py...")
    for idx, (vals, p_val, q_val, expected_val) in enumerate(test_cases, 1):
        tree = build_tree(vals)
        p_node = find_node(tree, p_val)
        q_node = find_node(tree, q_val)
        lca = lowest_common_ancestor(tree, p_node, q_node)
        assert lca is not None and lca.val == expected_val, f"Case {idx} failed: got {lca.val if lca else None}, expected {expected_val}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
