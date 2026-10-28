"""LeetCode 226: Invert Binary Tree (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/invert-binary-tree/
Difficulty: Easy
Category: Trees

Pattern Context:
    To invert / mirror a binary tree:
    For every node in the tree, swap its left and right child pointers,
    then recursively invert the left and right subtrees.
    Base Case: If node is None, return None.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 07_trees/lc_0226_invert_binary_tree_compact.py
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


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Inverts a binary tree by recursively swapping left and right subtrees.

    Algorithmic Requirements:
    - Time Complexity: O(n) where n is the number of nodes in the tree.
    - Space Complexity: O(h) recursion stack frames where h is tree height.

    Steps to implement:
    1. Base case: If `root is None`, return None.
    2. Swap `root.left` and `root.right`.
    3. Recursively call `invert_tree(root.left)` and `invert_tree(root.right)`.
    4. Return `root`.

    -------------------------------------------------------------------------
    TODO: Implement child pointer swap and recursive descent below.
    -------------------------------------------------------------------------
    """
    if not root:
        return None

    # <<< YOUR CODE HERE >>>
    # Hint: Swap root.left and root.right
    swap = TODO  # Replace with: (root.right, root.left)
    if swap is None:
        raise NotImplementedError("TODO: Swap left and right child pointers.")
    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root


# =====================================================================
# Offline Test Harness & Tree Serialization Helpers
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
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([], []),
        ([1], [1]),
    ]

    print("Running verification for lc_0226_invert_binary_tree_compact.py...")
    for idx, (vals, expected) in enumerate(test_cases, 1):
        tree = build_tree(vals)
        inv = invert_tree(tree)
        result = tree_to_list(inv)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
