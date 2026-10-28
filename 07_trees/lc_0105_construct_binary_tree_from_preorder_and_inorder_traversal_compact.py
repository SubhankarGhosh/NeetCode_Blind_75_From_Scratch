"""LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Difficulty: Medium
Category: Trees

Pattern Context:
    Given two integer arrays `preorder` and `inorder`, reconstruct and return the binary tree:
    Key Traversal Invariants:
    1. Preorder Traversal (Root -> Left -> Right):
       The first element is GUARANTEED to be the root of the current subtree.
    2. Inorder Traversal (Left -> Root -> Right):
       Locating the root value at index `mid` partitions the array:
       - Elements to the left of `mid` constitute the entire left subtree.
       - Elements to the right of `mid` constitute the entire right subtree.
    3. Optimal Hash Map Indexing:
       Pre-hashing `inorder_idx = {val: i for i, val in enumerate(inorder)}` allows O(1)
       root lookups, avoiding O(n) array slicing and yielding an optimal O(n) runtime!

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 07_trees/lc_0105_construct_binary_tree_from_preorder_and_inorder_traversal_compact.py
"""

from __future__ import annotations
from typing import Optional, List, Dict
from collections import deque

# Sentinel placeholder for exercise tasks
TODO = None


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_traversals(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """Reconstructs binary tree from preorder and inorder sequences in O(n) time.

    Algorithmic Requirements:
    - Time Complexity: O(n) using hash map index lookups without array copies.
    - Space Complexity: O(n) for hash map and recursion stack.

    Steps to implement:
    1. Build `in_map = {val: i for i, val in enumerate(inorder)}`.
    2. Maintain `pre_idx = 0` (tracks root element in preorder).
    3. Define `helper(left, right)`:
       - Base case: If `left > right`, return None.
       - Read root value `val = preorder[pre_idx]`, increment `pre_idx += 1`.
       - Create `root = TreeNode(val)`.
       - Look up `mid = in_map[val]`.
       - `root.left = helper(left, mid - 1)`.
       - `root.right = helper(mid + 1, right)`.
       - Return `root`.
    4. Call `helper(0, len(inorder) - 1)`.

    -------------------------------------------------------------------------
    TODO: Implement tree reconstruction using inorder partition boundaries below.
    -------------------------------------------------------------------------
    """
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

        # <<< YOUR CODE HERE >>>
        # Hint: Build left subtree in [in_left, mid - 1] and right subtree in [mid + 1, in_right]
        subtrees = TODO  # Replace with: (helper(in_left, mid - 1), helper(mid + 1, in_right))
        if subtrees is None:
            raise NotImplementedError("TODO: Recursively build left and right subtrees.")

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

    print("Running verification for lc_0105_construct_binary_tree_from_preorder_and_inorder_traversal_compact.py...")
    for idx, (pre, inord, expected) in enumerate(test_cases, 1):
        tree = build_tree_from_traversals(list(pre), list(inord))
        result = tree_to_list(tree)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
