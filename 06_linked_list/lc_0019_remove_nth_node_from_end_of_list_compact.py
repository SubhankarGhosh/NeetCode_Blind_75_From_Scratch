"""LeetCode 19: Remove Nth Node From End of List (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Difficulty: Medium
Category: Linked List

Pattern Context:
    To delete the nth node from the end in a single pass:
    - Sentinel Dummy Node: `dummy = ListNode(0, head)`.
      Handles edge cases cleanly, including deleting the head node when n equals the list length.
    - Two Pointers with Fixed Offset n:
      1. Start `left = dummy` and `right = head`.
      2. Advance `right` forward by n nodes.
      3. Advance both `left` and `right` one node at a time until `right is None`.
      4. `left` now rests on the node immediately BEFORE the node to be removed!
      5. Bypass target: `left.next = left.next.next`.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 06_linked_list/lc_0019_remove_nth_node_from_end_of_list_compact.py
"""

from __future__ import annotations
from typing import Optional, List

# Sentinel placeholder for exercise tasks
TODO = None


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """Removes the nth node from the end of the list in a single pass.

    Algorithmic Requirements:
    - Time Complexity: O(L) single pass where L is the number of nodes in the list.
    - Space Complexity: O(1) auxiliary space.

    Steps to implement:
    1. Create `dummy = ListNode(0, head)`, set `left = dummy`, `right = head`.
    2. Advance `right` forward by `n` steps.
    3. While `right is not None`:
       - `left = left.next`
       - `right = right.next`
    4. Delete target: `left.next = left.next.next`.
    5. Return `dummy.next`.

    -------------------------------------------------------------------------
    TODO: Implement two-pointer offset advancement and deletion below.
    -------------------------------------------------------------------------
    """
    dummy = ListNode(0, head)
    left = dummy
    right = head

    # Advance right by n steps
    for _ in range(n):
        if right is None:
            return head
        right = right.next

    # Move both pointers until right reaches end of list
    while right:
        left = left.next
        right = right.next

    # <<< YOUR CODE HERE >>>
    # Hint: Bypass the nth node from end by updating left.next
    deletion = TODO  # Replace with: left.next.next
    if deletion is None and left.next is not None and left.next.next is not None:
        raise NotImplementedError("TODO: Bypass the deleted node.")
    left.next = left.next.next

    return dummy.next


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
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3], 3, [2, 3]),
    ]

    print("Running verification for lc_0019_remove_nth_node_from_end_of_list_compact.py...")
    for idx, (vals, n, expected) in enumerate(test_cases, 1):
        ll = build_list(vals)
        res_node = remove_nth_from_end(ll, n)
        result = to_list(res_node)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
