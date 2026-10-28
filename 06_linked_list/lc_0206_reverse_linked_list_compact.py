"""LeetCode 206: Reverse Linked List (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/reverse-linked-list/
Difficulty: Easy
Category: Linked List

Pattern Context:
    Reversing a singly-linked list in-place requires redirecting each node's `next`
    pointer to point to its predecessor (`prev`), rather than its successor.
    To avoid losing access to the rest of the list when modifying `curr.next`,
    we temporarily buffer `nxt = curr.next` before mutating pointers.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 06_linked_list/lc_0206_reverse_linked_list_compact.py
"""

from __future__ import annotations
from typing import Optional, List

# Sentinel placeholder for exercise tasks
TODO = None


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverses a singly-linked list in-place in O(n) time and O(1) space.

    Algorithmic Requirements:
    - Time Complexity: O(n) single pass visiting each node once.
    - Space Complexity: O(1) auxiliary space (in-place pointer mutation).

    Steps to implement:
    1. Initialize `prev = None`, `curr = head`.
    2. While `curr is not None`:
       - Buffer next node: `nxt = curr.next`.
       - Reverse pointer: `curr.next = prev`.
       - Step forward: `prev = curr`, `curr = nxt`.
    3. Return `prev` (new head of the reversed list).

    -------------------------------------------------------------------------
    TODO: Implement the 3-pointer in-place reversal step below.
    -------------------------------------------------------------------------
    """
    prev: Optional[ListNode] = None
    curr = head

    while curr:
        nxt = curr.next
        # <<< YOUR CODE HERE >>>
        # Hint: Direct curr.next to prev, then advance prev to curr and curr to nxt
        reversed_next = TODO  # Replace with: prev
        if reversed_next is None and curr is not None and prev is not None:
            raise NotImplementedError("TODO: Direct curr.next to prev.")

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

    print("Running verification for lc_0206_reverse_linked_list_compact.py...")
    for idx, (vals, expected) in enumerate(test_cases, 1):
        ll = build_list(vals)
        res_node = reverse_list(ll)
        result = to_list(res_node)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
