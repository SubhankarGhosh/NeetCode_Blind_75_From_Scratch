"""LeetCode 23: Merge k Sorted Lists (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/merge-k-sorted-lists/
Difficulty: Hard
Category: Linked List

Pattern Context:
    Given an array of k linked lists, each sorted in ascending order, merge all lists
    into one single sorted linked list:
    - Naive Linear Merging (merging 1 by 1 into a running list):
      Takes O(k * N) time, which times out for large k.
    - Divide and Conquer Pairwise Merging:
      Pair up adjacent lists and merge each pair using LC 21 `merge_two_lists`.
      After 1 round: k lists become k / 2 lists.
      After 2 rounds: k / 4 lists ... terminating in log2(k) rounds.
      In every round, all N nodes are visited exactly once.
      Total Time: O(N log k) with O(1) auxiliary space!

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 06_linked_list/lc_0023_merge_k_sorted_lists_compact.py
"""

from __future__ import annotations
from typing import Optional, List

# Sentinel placeholder for exercise tasks
TODO = None


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """Helper: Merges two sorted linked lists."""
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
    """Merges k sorted lists in O(N log k) time using Divide and Conquer.

    Algorithmic Requirements:
    - Time Complexity: O(N log k) where N is total nodes and k is number of lists.
    - Space Complexity: O(1) auxiliary space beyond array of list heads.

    Steps to implement:
    1. If `not lists` or `len(lists) == 0`, return None.
    2. While `len(lists) > 1`:
       - Initialize `merged_lists = []`.
       - For `i` in `range(0, len(lists), 2)`:
         * `l1 = lists[i]`
         * `l2 = lists[i + 1]` if `(i + 1) < len(lists)` else None.
         * Append `merge_two_lists(l1, l2)` to `merged_lists`.
       - Update `lists = merged_lists`.
    3. Return `lists[0]`.

    -------------------------------------------------------------------------
    TODO: Implement pairwise divide-and-conquer merging below.
    -------------------------------------------------------------------------
    """
    if not lists:
        return None

    while len(lists) > 1:
        merged_lists: List[Optional[ListNode]] = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None

            # <<< YOUR CODE HERE >>>
            # Hint: Merge pair (l1, l2) using merge_two_lists helper
            merged_pair = TODO  # Replace with: merge_two_lists(l1, l2)
            if merged_pair is None and (l1 is not None or l2 is not None):
                raise NotImplementedError("TODO: Merge pair of linked lists.")
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

    print("Running verification for lc_0023_merge_k_sorted_lists_compact.py...")
    for idx, (lists_vals, expected) in enumerate(test_cases, 1):
        list_nodes = [build_list(v) for v in lists_vals]
        res_node = merge_k_lists(list_nodes)
        result = to_list(res_node)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
