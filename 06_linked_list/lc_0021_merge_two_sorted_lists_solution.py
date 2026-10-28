"""LeetCode 21: Merge Two Sorted Lists (Reference Solution)

Problem URL: https://leetcode.com/problems/merge-two-sorted-lists/
Difficulty: Easy
Category: Linked List

Complexity Analysis:
- Time Complexity: O(n + m) where n and m are the lengths of list1 and list2.
  Each iteration advances one pointer forward by 1 node until one list is exhausted.
  The remainder is attached in O(1) time.
- Space Complexity: O(1) auxiliary space as original node objects are linked directly in-place.
"""

from __future__ import annotations
from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """Merges two sorted lists in-place using a sentinel dummy head and tail pointer."""
    dummy = ListNode(0)
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Splice the remainder of whichever list is not yet exhausted
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

    print("Running verification for lc_0021_merge_two_sorted_lists_solution.py...")
    for idx, (v1, v2, expected) in enumerate(test_cases, 1):
        l1 = build_list(v1)
        l2 = build_list(v2)
        res_node = merge_two_lists(l1, l2)
        result = to_list(res_node)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
