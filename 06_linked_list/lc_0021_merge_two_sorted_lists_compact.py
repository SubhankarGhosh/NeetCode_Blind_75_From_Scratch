"""LeetCode 21: Merge Two Sorted Lists (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/merge-two-sorted-lists/
Difficulty: Easy
Category: Linked List

Pattern Context:
    Merging two sorted singly-linked lists into a single continuous sorted list:
    - Sentinel / Dummy Node Pattern:
      Allocating a temporary dummy head node `dummy = ListNode()` completely eliminates
      special-case logic for initializing the head of the merged list.
    - Two-Pointer Splicing:
      Compare `list1.val` against `list2.val`, attach the smaller node to `tail.next`,
      and advance the corresponding pointer.
    - Constant-Time Tail Splicing:
      When one list is exhausted, splice the remaining non-empty list directly onto `tail.next`
      in O(1) time without looping through remaining elements.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 06_linked_list/lc_0021_merge_two_sorted_lists_compact.py
"""

from __future__ import annotations
from typing import Optional, List

# Sentinel placeholder for exercise tasks
TODO = None


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """Merges two sorted linked lists into one sorted list in O(n + m) time and O(1) space.

    Algorithmic Requirements:
    - Time Complexity: O(n + m) where n and m are lengths of list1 and list2.
    - Space Complexity: O(1) auxiliary space (reusing existing list nodes).

    Steps to implement:
    1. Initialize `dummy = ListNode(0)`, `tail = dummy`.
    2. While `list1` and `list2`:
       - If `list1.val < list2.val`:
         * `tail.next = list1`
         * `list1 = list1.next`
       - Else:
         * `tail.next = list2`
         * `list2 = list2.next`
       - `tail = tail.next`
    3. Splice non-empty remainder: `tail.next = list1 or list2`.
    4. Return `dummy.next`.

    -------------------------------------------------------------------------
    TODO: Implement the comparison and splicing logic below.
    -------------------------------------------------------------------------
    """
    dummy = ListNode(0)
    tail = dummy

    while list1 and list2:
        # <<< YOUR CODE HERE >>>
        # Hint: Connect tail.next to whichever node has the smaller value
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    # Splicing the non-exhausted list
    remaining = TODO  # Replace with: list1 if list1 else list2
    if remaining is None and (list1 or list2):
        raise NotImplementedError("TODO: Splice remaining non-empty list.")
    tail.next = list1 if list1 else list2

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
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([5], [1, 2, 4], [1, 2, 4, 5]),
        ([-3, -1, 4], [-2, 0, 5], [-3, -2, -1, 0, 4, 5]),
    ]

    print("Running verification for lc_0021_merge_two_sorted_lists_compact.py...")
    for idx, (v1, v2, expected) in enumerate(test_cases, 1):
        l1 = build_list(v1)
        l2 = build_list(v2)
        res_node = merge_two_lists(l1, l2)
        result = to_list(res_node)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
