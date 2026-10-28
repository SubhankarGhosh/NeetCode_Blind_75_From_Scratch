"""LeetCode 141: Linked List Cycle (Reference Solution)

Problem URL: https://leetcode.com/problems/linked-list-cycle/
Difficulty: Easy
Category: Linked List

Complexity Analysis:
- Time Complexity: O(n) where n is the number of nodes in the linked list.
  If there is no cycle, fast reaches the end in n/2 steps.
  If there is a cycle of length C with a non-cyclic prefix of length K:
  slow enters the cycle after K steps; fast is already in the cycle.
  The gap between them shrinks by 1 node per iteration, guaranteeing meeting in at most C steps.
  Total steps <= K + C = n = O(n).
- Space Complexity: O(1) auxiliary space as only two node reference pointers are maintained.
"""

from __future__ import annotations
from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    """Detects cycles using Floyd's Tortoise and Hare algorithm in O(n) time and O(1) space."""
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


# =====================================================================
# Offline Test Harness & Cycle Helper
# =====================================================================
def build_cycle_list(vals: List[int], pos: int) -> Optional[ListNode]:
    if not vals:
        return None
    nodes = [ListNode(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


if __name__ == "__main__":
    test_cases = [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([], -1, False),
        ([1, 2, 3, 4, 5], -1, False),
        ([1, 2, 3, 4, 5], 4, True),
    ]

    print("Running verification for lc_0141_linked_list_cycle_solution.py...")
    for idx, (vals, pos, expected) in enumerate(test_cases, 1):
        ll = build_cycle_list(vals, pos)
        result = has_cycle(ll)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
