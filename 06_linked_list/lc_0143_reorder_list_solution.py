"""LeetCode 143: Reorder List (Reference Solution)

Problem URL: https://leetcode.com/problems/reorder-list/
Difficulty: Medium
Category: Linked List

Complexity Analysis:
- Time Complexity: O(n) where n is the number of nodes.
  Phase 1 (find midpoint): n/2 steps.
  Phase 2 (reverse half): n/2 steps.
  Phase 3 (merge lists): n/2 steps.
  Total steps: 3/2 n = O(n).
- Space Complexity: O(1) auxiliary space as all modifications are made in-place.
"""

from __future__ import annotations
from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def reorder_list(head: Optional[ListNode]) -> None:
    """Reorders the linked list in-place by splitting, reversing second half, and interleaving."""
    if not head or not head.next:
        return

    # Phase 1: Locate midpoint via fast/slow pointers
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None  # Cut the list into two halves

    # Phase 2: Reverse the second half
    prev: Optional[ListNode] = None
    curr = second
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    second = prev

    # Phase 3: Interleave / zip-merge the two halves
    first = head
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2


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
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 2, 3], [1, 3, 2]),
        ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
    ]

    print("Running verification for lc_0143_reorder_list_solution.py...")
    for idx, (vals, expected) in enumerate(test_cases, 1):
        ll = build_list(vals)
        reorder_list(ll)
        result = to_list(ll)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
