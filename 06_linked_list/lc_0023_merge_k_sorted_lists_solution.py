"""LeetCode 23: Merge k Sorted Lists (Reference Solution)

Problem URL: https://leetcode.com/problems/merge-k-sorted-lists/
Difficulty: Hard
Category: Linked List

Complexity Analysis:
- Time Complexity: O(N log k) where N is the total number of nodes across all k lists.
  There are ceil(log2(k)) reduction levels. At each level, every node is merged exactly
  once in O(N) time. Total time: O(N log k).
- Space Complexity: O(1) auxiliary space beyond the temporary lists array used to hold
  pointers at each reduction level (no recursive call stack or heap node duplication).
"""

from __future__ import annotations
from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """Merges two sorted lists in O(len(l1) + len(l2)) time."""
    dummy = ListNode(0)
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return dummy.next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """Merges k sorted lists in O(N log k) time using pairwise divide-and-conquer."""
    if not lists:
        return None

    while len(lists) > 1:
        merged_lists: List[Optional[ListNode]] = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            merged_lists.append(merge_two_lists(l1, l2))
        lists = merged_lists

    return lists[0]


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
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1]], [1]),
        ([[1, 2], [-1, 3], [0, 4]], [-1, 0, 1, 2, 3, 4]),
    ]

    print("Running verification for lc_0023_merge_k_sorted_lists_solution.py...")
    for idx, (lists_vals, expected) in enumerate(test_cases, 1):
        list_nodes = [build_list(v) for v in lists_vals]
        res_node = merge_k_lists(list_nodes)
        result = to_list(res_node)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
