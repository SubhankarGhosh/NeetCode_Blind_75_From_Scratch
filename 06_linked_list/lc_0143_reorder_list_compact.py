"""LeetCode 143: Reorder List (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/reorder-list/
Difficulty: Medium
Category: Linked List

Pattern Context:
    Reorder list L0 -> L1 -> ... -> Ln-1 -> Ln into:
        L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
    Must modify nodes in-place without altering node values.

    The 3-Phase In-Place Pipeline:
    1. Find Midpoint: Fast and slow pointers isolate the two halves (slow = head, fast = head.next).
       Split list: `second = slow.next`, `slow.next = None`.
    2. Reverse Second Half: Standard in-place reversal of `second`.
    3. Interleave Two Halves: Zip-merge `first` and `second` using temporary pointer buffers.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 06_linked_list/lc_0143_reorder_list_compact.py
"""

from __future__ import annotations
from typing import Optional, List

# Sentinel placeholder for exercise tasks
TODO = None


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def reorder_list(head: Optional[ListNode]) -> None:
    """Reorders the linked list in-place in O(n) time and O(1) space.

    Algorithmic Requirements:
    - Time Complexity: O(n) three sequential linear sub-passes.
    - Space Complexity: O(1) auxiliary space (no arrays or new nodes).
    """
    if not head or not head.next:
        return

    # Phase 1: Find middle using fast & slow pointers
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None  # Sever link between first and second half

    # Phase 2: Reverse second half
    prev: Optional[ListNode] = None
    curr = second
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    second = prev

    # Phase 3: Interleave two halves
    first = head
    while second:
        # <<< YOUR CODE HERE >>>
        # Hint: Buffer first.next and second.next, then stitch first -> second -> tmp1
        tmp1, tmp2 = first.next, second.next
        stitch = TODO  # Replace with: (first, second, tmp1, tmp2)
        if stitch is None:
            raise NotImplementedError("TODO: Implement interleaving node pointers.")

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

    print("Running verification for lc_0143_reorder_list_compact.py...")
    for idx, (vals, expected) in enumerate(test_cases, 1):
        ll = build_list(vals)
        reorder_list(ll)
        result = to_list(ll)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
