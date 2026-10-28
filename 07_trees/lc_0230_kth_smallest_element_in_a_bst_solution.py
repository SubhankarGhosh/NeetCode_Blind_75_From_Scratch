"""LeetCode 230: Kth Smallest Element in a BST (Reference Solution)

Problem URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Difficulty: Medium
Category: Trees

Complexity Analysis:
- Time Complexity: O(h + k) where h is tree height and k is the target order.
  Descends left h times, then pops exactly k elements before early-terminating.
- Space Complexity: O(h) auxiliary space to maintain the explicit recursion stack.
"""

from __future__ import annotations
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    """Finds k-th smallest element in a BST using iterative stack-based in-order traversal."""
    stack: List[TreeNode] = []
    curr = root
    count = 0

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        count += 1
        if count == k:
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

    print("Running verification for lc_0230_kth_smallest_element_in_a_bst_solution.py...")
    for idx, (vals, k, expected) in enumerate(test_cases, 1):
        tree = build_tree(vals)
        result = kth_smallest(tree, k)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
