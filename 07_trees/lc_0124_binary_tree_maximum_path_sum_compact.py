"""LeetCode 124: Binary Tree Maximum Path Sum (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/
Difficulty: Hard
Category: Trees

Pattern Context:
    A path is any sequence of nodes where each pair of adjacent nodes has an edge connecting them.
    A node can only appear at most once in a path, and the path does NOT need to pass through the root.

    Post-Order DFS Split vs. Continuation Invariant:
    At each node:
    1. Maximum Non-Negative Branch Gain:
       Calculate `left_gain = max(0, dfs(node.left))` and `right_gain = max(0, dfs(node.right))`.
       (Clamping negative contributions to 0 ensures we ignore branches that decrease total sum).
    2. Path with Split (Bridge):
       The path connecting left subtree, current node, and right subtree is:
       `node.val + left_gain + right_gain`.
       Update the global maximum path sum with this value!
    3. Return Value (Continuation to Parent):
       A parent can only continue along ONE child branch (it cannot split twice).
       Return `node.val + max(left_gain, right_gain)` to the caller.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 07_trees/lc_0124_binary_tree_maximum_path_sum_compact.py
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


def max_path_sum(root: Optional[TreeNode]) -> int:
    """Finds maximum path sum in a binary tree in O(n) time and O(h) space.

    Algorithmic Requirements:
    - Time Complexity: O(n) visiting each node once.
    - Space Complexity: O(h) recursion stack frames.

    Steps to implement:
    1. Initialize `max_val = float("-inf")`.
    2. Define `dfs(node)`:
       - Base case: If `node is None`, return 0.
       - `left_gain = max(0, dfs(node.left))`
       - `right_gain = max(0, dfs(node.right))`
       - Update `max_val = max(max_val, node.val + left_gain + right_gain)`
       - Return `node.val + max(left_gain, right_gain)`
    3. Call `dfs(root)`, return `max_val`.

    -------------------------------------------------------------------------
    TODO: Implement bottom-up post-order path accumulation below.
    -------------------------------------------------------------------------
    """
    max_val = float("-inf")

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal max_val
        if not node:
            return 0

        left_gain = max(0, dfs(node.left))
        right_gain = max(0, dfs(node.right))

        # Path with split at current node
        current_split_sum = node.val + left_gain + right_gain
        max_val = max(max_val, current_split_sum)

        # <<< YOUR CODE HERE >>>
        # Hint: Return the node value plus the single best child branch
        continuation_gain = TODO  # Replace with: node.val + max(left_gain, right_gain)
        if continuation_gain is None:
            raise NotImplementedError("TODO: Return non-splitting branch gain.")

        return node.val + max(left_gain, right_gain)

    dfs(root)
    return int(max_val)


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
        ([1, 2, 3], 6),
        ([-10, 9, 20, None, None, 15, 7], 42),
        ([-3], -3),
        ([2, -1], 2),
        ([1, -2, 3], 4),
        ([-2, 1], 1),
    ]

    print("Running verification for lc_0124_binary_tree_maximum_path_sum_compact.py...")
    for idx, (vals, expected) in enumerate(test_cases, 1):
        tree = build_tree(vals)
        result = max_path_sum(tree)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
