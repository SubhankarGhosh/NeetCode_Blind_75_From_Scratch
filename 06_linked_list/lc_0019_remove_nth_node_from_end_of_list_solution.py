"""LeetCode 19: Remove Nth Node From End of List (Reference Solution)

Problem URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Difficulty: Medium
Category: Linked List

Complexity Analysis:
- Time Complexity: O(L) where L is the total number of nodes in the linked list.
  The algorithm performs a single pass: pointer `right` traverses L nodes, and pointer `left`
  traverses (L - n) nodes.
- Space Complexity: O(1) auxiliary space beyond the sentinel dummy node.

Algorithm Walkthrough (Strict Chronological Sequence):
    Example: head = [1, 2, 3, 4, 5], n = 2 (Remove node 4)
    Step 0: Create dummy node (val=0) pointing to head:
            dummy(0) -> [1] -> [2] -> [3] -> [4] -> [5] -> None
            left = dummy, right = [1]
    Step 1: Advance right by n = 2 steps:
            - Step 1a: right = [2]
            - Step 1b: right = [3]
            Now gap between left and right is 2 nodes.
    Step 2: Advance left and right in lockstep until right reaches None:
            - Loop 1: left = [1], right = [4]
            - Loop 2: left = [2], right = [5]
            - Loop 3: left = [3], right = None  <-- STOP
    Step 3: left is at node [3]. The node to remove is [4] (left.next).
            Update pointer: left.next = left.next.next (points [3] directly to [5]).
    Step 4: Return dummy.next ([1] -> [2] -> [3] -> [5]).

Brute-Force Alternative:
    Pass 1: Traverse the entire list to count total length L.
    Pass 2: Traverse (L - n) nodes from the start to reach the predecessor, then bypass.
    Drawback: Requires two full traversals instead of a single streaming pass.

Potential Interview Follow-Up Questions:
    1. Q: What if n is greater than the length of the list?
       A: If `right` becomes None before completing the initial n steps, either return head
          unmodified or raise a ValueError depending on API specification.
    2. Q: What if the list is doubly-linked?
       A: In a doubly-linked list with a tail pointer, simply walk backward from tail by (n - 1)
          steps in O(n) without needing two pointers or full traversal.
    3. Q: How would you handle this in a concurrent/multi-threaded environment?
       A: Use optimistic concurrency with version stamps / compare-and-swap (CAS) on `node.next`
          pointers (e.g. Harris's lock-free linked list deletion with logical deletion markers).
"""

from __future__ import annotations
from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """Removes the nth node from the end of the list in a single pass using two pointers."""
    dummy = ListNode(0, head)
    left = dummy
    right = head

    # Advance right pointer by n steps to establish the offset window
    for _ in range(n):
        if right is None:
            return head
        right = right.next

    # Slide window until right falls off the end of the list
    while right:
        left = left.next
        right = right.next

    # Bypass the target node
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

    print("Running verification for lc_0019_remove_nth_node_from_end_of_list_solution.py...")
    for idx, (vals, n, expected) in enumerate(test_cases, 1):
        ll = build_list(vals)
        res_node = remove_nth_from_end(ll, n)
        result = to_list(res_node)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
