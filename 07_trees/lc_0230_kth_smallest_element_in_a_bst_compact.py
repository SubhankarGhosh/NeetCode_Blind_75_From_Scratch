"""LeetCode 230: Kth Smallest Element in a BST (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Difficulty: Medium
Category: Trees

Pattern Context:
    An in-order traversal (Left -> Node -> Right) of a Binary Search Tree visits
    elements in strictly sorted ascending order.
    Iterative Stack Traversal:
    - Instead of visiting all n nodes into an array and indexing `arr[k - 1]` in O(n) space,
      an iterative in-order traversal with a stack can early-exit immediately upon
      reaching the k-th node!
    - Time Complexity: O(h + k), Space Complexity: O(h).

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 07_trees/lc_0230_kth_smallest_element_in_a_bst_compact.py
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


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    """Finds the k-th smallest element in a BST using iterative in-order traversal.

    Algorithmic Requirements:
    - Time Complexity: O(h + k) stopping immediately at the k-th element.
    - Space Complexity: O(h) stack memory.

    Steps to implement:
    1. Initialize `stack = []`, `curr = root`, `count = 0`.
    2. While `curr is not None or len(stack) > 0`:
       - While `curr`: push `curr` to `stack`, `curr = curr.left`.
       - Pop `curr = stack.pop()`.
       - Increment `count += 1`.
       - If `count == k`: return `curr.val`.
       - Advance `curr = curr.right`.
    3. Return -1 if not found.

    -------------------------------------------------------------------------
    TODO: Implement iterative in-order traversal logic below.
    -------------------------------------------------------------------------
    """
    stack: List[TreeNode] = []
    curr = root
    count = 0

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        count += 1

        # <<< YOUR CODE HERE >>>
        # Hint: If count equals k, we have arrived at the k-th smallest element
        is_kth = TODO  # Replace with: count == k
        if is_kth is None:
            raise NotImplementedError("TODO: Check if k-th element reached.")

        if is_kth:
            return curr.val

        curr = curr.right

    return -1


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
        ([3, 1, 4, None, 2], 1, 1),
        ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
        ([2, 1, 3], 2, 2),
        ([1], 1, 1),
        ([4, 2, 5, 1, 3], 4, 4),
    ]

    print("Running verification for lc_0230_kth_smallest_element_in_a_bst_compact.py...")
    for idx, (vals, k, expected) in enumerate(test_cases, 1):
        tree = build_tree(vals)
        result = kth_smallest(tree, k)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
