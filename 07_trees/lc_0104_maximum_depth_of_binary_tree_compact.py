"""LeetCode 104: Maximum Depth of Binary Tree (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Difficulty: Easy
Category: Trees

Pattern Context:
    The maximum depth is the number of nodes along the longest path from the root
    node down to the farthest leaf node.
    Recursive DFS Invariant:
    - Base Case: An empty tree (`root is None`) has depth 0.
    - Inductive Step: The depth of any non-empty node is 1 + max(depth(left), depth(right)).

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 07_trees/lc_0104_maximum_depth_of_binary_tree_compact.py
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


def max_depth(root: Optional[TreeNode]) -> int:
    """Computes maximum depth using post-order DFS traversal.

    Algorithmic Requirements:
    - Time Complexity: O(n) visiting each node once.
    - Space Complexity: O(h) recursion stack height.

    Steps to implement:
    1. Base case: If `root is None`, return 0.
    2. Recursively find `max_depth(root.left)` and `max_depth(root.right)`.
    3. Return 1 + max(left_depth, right_depth).

    -------------------------------------------------------------------------
    TODO: Implement depth calculation below.
    -------------------------------------------------------------------------
    """
    if not root:
        return 0

    left_d = max_depth(root.left)
    right_d = max_depth(root.right)

    # <<< YOUR CODE HERE >>>
    # Hint: Return 1 plus the maximum of left_d and right_d
    depth = TODO  # Replace with: 1 + max(left_d, right_d)
    if depth is None:
        raise NotImplementedError("TODO: Return 1 + max(left_d, right_d).")

    return 1 + max(left_d, right_d)


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
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([], 0),
        ([0], 1),
        ([1, 2, 3, 4, 5], 3),
    ]

    print("Running verification for lc_0104_maximum_depth_of_binary_tree_compact.py...")
    for idx, (vals, expected) in enumerate(test_cases, 1):
        tree = build_tree(vals)
        result = max_depth(tree)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
