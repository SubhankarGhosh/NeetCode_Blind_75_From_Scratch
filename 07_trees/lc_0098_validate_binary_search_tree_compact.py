"""LeetCode 98: Validate Binary Search Tree (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/validate-binary-search-tree/
Difficulty: Medium
Category: Trees

Pattern Context:
    A valid Binary Search Tree (BST) must satisfy the global property:
    - Every node in the left subtree has a value strictly less than node.val.
    - Every node in the right subtree has a value strictly greater than node.val.
    Crucial Insight:
    Checking only immediate children (e.g. `node.left.val < node.val`) is INSUFFICIENT!
    Subtree boundaries must propagate down:
    - Left child must fall in: `(low, node.val)`.
    - Right child must fall in: `(node.val, high)`.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 07_trees/lc_0098_validate_binary_search_tree_compact.py
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


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """Validates whether a binary tree satisfies the strict BST property.

    Algorithmic Requirements:
    - Time Complexity: O(n) checking each node once.
    - Space Complexity: O(h) recursion stack height.

    Steps to implement:
    1. Define helper `valid(node, low, high)`.
    2. Base case: If `node is None`, return True.
    3. If `not (low < node.val < high)`, return False.
    4. Recursively validate:
       `valid(node.left, low, node.val) and valid(node.right, node.val, high)`.
    5. Call helper with `(-inf, inf)`.

    -------------------------------------------------------------------------
    TODO: Implement recursive range-boundary propagation below.
    -------------------------------------------------------------------------
    """
    def valid(node: Optional[TreeNode], low: float, high: float) -> bool:
        if not node:
            return True

        if not (low < node.val < high):
            return False

        # <<< YOUR CODE HERE >>>
        # Hint: Validate left child in (low, node.val) and right child in (node.val, high)
        children_valid = TODO  # Replace with: valid(node.left, low, node.val) and valid(node.right, node.val, high)
        if children_valid is None:
            raise NotImplementedError("TODO: Propagate range boundaries to children.")

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

    print("Running verification for lc_0098_validate_binary_search_tree_compact.py...")
    for idx, (vals, expected) in enumerate(test_cases, 1):
        tree = build_tree(vals)
        result = is_valid_bst(tree)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
