"""LeetCode 141: Linked List Cycle (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/linked-list-cycle/
Difficulty: Easy
Category: Linked List

Pattern Context:
    Determining whether a linked list contains a cycle using Floyd's Cycle-Finding Algorithm
    (The "Tortoise and Hare"):
    - Maintain two pointers starting at `head`:
      * `slow` advances 1 step at a time.
      * `fast` advances 2 steps at a time.
    - If no cycle exists, `fast` (or `fast.next`) will reach None in O(n) steps.
    - If a cycle of length C exists, every iteration reduces the relative distance
      between `fast` and `slow` by 1 node modulo C. Thus `fast` is mathematically
      guaranteed to lap and catch `slow` within the cycle in at most C steps.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 06_linked_list/lc_0141_linked_list_cycle_compact.py
"""

from __future__ import annotations
from typing import Optional, List

# Sentinel placeholder for exercise tasks
TODO = None


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    """Detects if a cycle exists in the linked list in O(n) time and O(1) space.

    Algorithmic Requirements:
    - Time Complexity: O(n) where n is the number of nodes.
    - Space Complexity: O(1) auxiliary space (no hash sets).

    Steps to implement:
    1. Initialize `slow = head`, `fast = head`.
    2. While `fast is not None and fast.next is not None`:
       - Advance `slow = slow.next`.
       - Advance `fast = fast.next.next`.
       - If `slow == fast`, return True (pointers met inside a cycle).
    3. Return False if loop exits (fast reached end of list).

    -------------------------------------------------------------------------
    TODO: Implement the tortoise and hare cycle detection below.
    -------------------------------------------------------------------------
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # <<< YOUR CODE HERE >>>
        # Hint: Check if slow pointer has met fast pointer
        pointers_collided = TODO  # Replace with: slow == fast
        if pointers_collided is None:
            raise NotImplementedError("TODO: Check if slow meets fast.")

        if pointers_collided:
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

    print("Running verification for lc_0141_linked_list_cycle_compact.py...")
    for idx, (vals, pos, expected) in enumerate(test_cases, 1):
        ll = build_cycle_list(vals, pos)
        result = has_cycle(ll)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
