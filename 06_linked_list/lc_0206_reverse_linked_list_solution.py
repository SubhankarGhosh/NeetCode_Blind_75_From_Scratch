"""LeetCode 206: Reverse Linked List (Reference Solution)

Problem URL: https://leetcode.com/problems/reverse-linked-list/
Difficulty: Easy
Category: Linked List

Complexity Analysis:
- Time Complexity: O(n) where n is the number of nodes in the linked list.
  Each node is visited exactly once.
- Space Complexity: O(1) auxiliary space as pointers are redirected in-place.
"""

from __future__ import annotations
from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverses a singly-linked list in-place using iterative three-pointer redirection."""
    prev: Optional[ListNode] = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


# =====================================================================
# Offline Test Harness & Helper Functions
# =====================================================================
def build_list(vals: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(node: Optional[ListNode]) -> List[int]:
    vals = []
    while node:
        vals.append(node.val)
        node = node.next
    return vals


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
        ([42], [42]),
        ([1, 1, 1], [1, 1, 1]),
    ]

    print("Running verification for lc_0206_reverse_linked_list_solution.py...")
    for idx, (vals, expected) in enumerate(test_cases, 1):
        ll = build_list(vals)
        res_node = reverse_list(ll)
        result = to_list(res_node)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
