"""LeetCode 102: Binary Tree Level Order Traversal (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/binary-tree-level-order-traversal/
Difficulty: Medium
Category: Trees

Pattern Context:
    Return the level order traversal of a binary tree's nodes' values (from left to right,
    level by level).
    Breadth-First Search (BFS) Level-Batching Invariant:
    - Use a FIFO queue initialized with `root`.
    - Inside the while loop, capturing `q_len = len(q)` guarantees that the inner loop
      processes EXACTLY all nodes belonging to the current level before any of their
      children (which belong to the next level) are considered.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 07_trees/lc_0102_binary_tree_level_order_traversal_compact.py
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


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """Returns level-by-level traversal using BFS queue batching.

    Algorithmic Requirements:
    - Time Complexity: O(n) visiting each node once.
    - Space Complexity: O(w) queue memory where w is the maximum width of the tree.

    Steps to implement:
    1. If `not root`: return [].
    2. Initialize `res = []`, `q = deque([root])`.
    3. While `q`:
       - `level = []`
       - For `_ in range(len(q))`:
         * `node = q.popleft()`
         * `level.append(node.val)`
         * Enqueue `node.left` and `node.right` if they exist.
       - Append `level` to `res`.
    4. Return `res`.

    -------------------------------------------------------------------------
    TODO: Implement BFS level batching and child enqueue logic below.
    -------------------------------------------------------------------------
    """
    if not root:
        return []

    res: List[List[int]] = []
    q: deque[TreeNode] = deque([root])

    while q:
        level: List[int] = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)

            # <<< YOUR CODE HERE >>>
            # Hint: Append node.left and node.right to q if present
            enqueue_children = TODO  # Replace with: (node.left, node.right)
            if enqueue_children is None and (node.left or node.right):
                raise NotImplementedError("TODO: Enqueue non-empty children.")

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        res.append(level)

    return res


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
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),
        ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]),
    ]

    print("Running verification for lc_0102_binary_tree_level_order_traversal_compact.py...")
    for idx, (vals, expected) in enumerate(test_cases, 1):
        tree = build_tree(vals)
        result = level_order(tree)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
