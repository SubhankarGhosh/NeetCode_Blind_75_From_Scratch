"""LeetCode 297: Serialize and Deserialize Binary Tree (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
Difficulty: Hard
Category: Trees

Pattern Context:
    Serialization is the process of converting a data structure into a sequence of bits/string
    so that it can be stored or transmitted and reconstructed later.
    Pre-order DFS Protocol:
    1. Serialization:
       - Visit Node -> Left -> Right.
       - If `node is None`: write sentinel marker `"N"`.
       - Else: write `str(node.val)` and recurse left, then right.
       - Delimit tokens with commas: `"1,2,N,N,3,4,N,N,5,N,N"`.
    2. Deserialization:
       - Read tokens sequentially via an iterator:
         * If token is `"N"`, return None.
         * Otherwise, instantiate `node = TreeNode(int(token))`.
         * Set `node.left = dfs()` and `node.right = dfs()`.
         * Return `node`.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 07_trees/lc_0297_serialize_and_deserialize_binary_tree_compact.py
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


class Codec:
    """Encodes a tree to a single string and decodes it back using pre-order DFS."""

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string in O(n) time."""
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
        """Decodes pre-order string back to binary tree in O(n) time."""
        vals = data.split(",")
        i = 0

        def dfs() -> Optional[TreeNode]:
            nonlocal i
            val = vals[i]
            i += 1

            if val == "N":
                return None

            # <<< YOUR CODE HERE >>>
            # Hint: Instantiate TreeNode(int(val)), then recursively assign left and right
            node = TODO  # Replace with: TreeNode(int(val))
            if node is None:
                raise NotImplementedError("TODO: Instantiate tree node.")

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

    print("Running verification for lc_0297_serialize_and_deserialize_binary_tree_compact.py...")
    for idx, vals in enumerate(test_cases, 1):
        original = build_tree(vals)
        serialized = codec.serialize(original)
        reconstructed = codec.deserialize(serialized)
        result = tree_to_list(reconstructed)
        expected = tree_to_list(original)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx} (Serialized: {serialized[:30]}...)")
    print("All tests passed with 100% success rate!")
