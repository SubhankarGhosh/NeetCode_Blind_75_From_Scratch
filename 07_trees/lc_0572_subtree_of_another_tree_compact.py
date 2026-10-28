"""LeetCode 572: Subtree of Another Tree (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/subtree-of-another-tree/
Difficulty: Easy
Category: Trees

Pattern Context:
    Given the roots of two binary trees `root` and `subRoot`, return True if there is
    a subtree of `root` with the exact same structure and node values as `subRoot`.
    Hierarchical DFS Matching:
    - Base Case: An empty `subRoot` is always a valid subtree (return True).
    - Base Case: If `root` is None but `subRoot` is not, it cannot match (return False).
    - If `is_same_tree(root, subRoot)` evaluates to True, match found!
    - Otherwise, recursively search:
      is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot).

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 07_trees/lc_0572_subtree_of_another_tree_compact.py
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


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """Helper: Checks if two trees are identical."""
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def is_subtree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
    """Determines whether sub_root is a subtree of root.

    Algorithmic Requirements:
    - Time Complexity: O(n * m) where n = len(root) and m = len(subRoot).
    - Space Complexity: O(h) recursion stack height.

    Steps to implement:
    1. If `not sub_root`: return True.
    2. If `not root`: return False.
    3. If `is_same_tree(root, sub_root)`: return True.
    4. Return `is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)`.

    -------------------------------------------------------------------------
    TODO: Implement subtree matching logic below.
    -------------------------------------------------------------------------
    """
    if not sub_root:
        return True
    if not root:
        return False

    if is_same_tree(root, sub_root):
        return True

    # <<< YOUR CODE HERE >>>
    # Hint: Check left child or right child
    branch_match = TODO  # Replace with: is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)
    if branch_match is None:
        raise NotImplementedError("TODO: Recursively check left and right subtrees.")

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

    print("Running verification for lc_0572_subtree_of_another_tree_compact.py...")
    for idx, (r_vals, s_vals, expected) in enumerate(test_cases, 1):
        r = build_tree(r_vals)
        s = build_tree(s_vals)
        result = is_subtree(r, s)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
