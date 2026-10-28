"""LeetCode 297: Serialize and Deserialize Binary Tree (Reference Solution)

Problem URL: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
Difficulty: Hard
Category: Trees

Complexity Analysis:
- Time Complexity: O(n) for both serialization and deserialization.
  Every node (and null child) is visited exactly once in a single pre-order DFS pass.
- Space Complexity: O(n) auxiliary space to store the serialized string tokens and
  accommodate the recursion stack frames.
"""

from __future__ import annotations
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    """Serializes and deserializes a binary tree using pre-order DFS with null sentinels."""

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single comma-separated string."""
        res: List[str] = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes pre-order string back to a binary tree."""
        vals = data.split(",")
        i = 0

        def dfs() -> Optional[TreeNode]:
            nonlocal i
            val = vals[i]
            i += 1

            if val == "N":
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


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
    codec = Codec()
    test_cases = [
        [1, 2, 3, None, None, 4, 5],
        [],
        [1],
        [1, 2],
        [-1, 0, 1],
        [5, 4, 7, 3, None, 2, None, -1, None, 9],
    ]

    print("Running verification for lc_0297_serialize_and_deserialize_binary_tree_solution.py...")
    for idx, vals in enumerate(test_cases, 1):
        original = build_tree(vals)
        serialized = codec.serialize(original)
        reconstructed = codec.deserialize(serialized)
        result = tree_to_list(reconstructed)
        expected = tree_to_list(original)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx} (Serialized: {serialized[:30]}...)")
    print("All tests passed with 100% success rate!")
