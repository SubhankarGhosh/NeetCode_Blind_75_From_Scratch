# Module 06: Linked List

Mastering pointer manipulation, sentinel dummy heads, fast & slow pointers (tortoise and hare), in-place list reversals, and divide-and-conquer k-way merging across 6 foundational LeetCode problems.

---

## 📋 Problem Map

| Problem | Difficulty | Key Paradigm | Time | Space | Status |
| :--- | :---: | :--- | :---: | :---: | :---: |
| [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | Iterative 3-Pointer Reversal | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | Sentinel Dummy Head + In-Place Splice | $\mathcal{O}(n + m)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [143. Reorder List](https://leetcode.com/problems/reorder-list/) | Medium | Midpoint Split + Reverse + Interleave | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | Two Pointers with Fixed Offset $n$ | $\mathcal{O}(L)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | Floyd's Tortoise and Hare | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | Divide & Conquer Pairwise Merge | $\mathcal{O}(N \log k)$ | $\mathcal{O}(1)^*$ | 🟢 Complete |

*\* Note: Space complexity excludes list heads array at reduction levels.*

---

## 🏃 Execution Instructions

Run exercises standalone with zero third-party dependencies:

```powershell
# Set UTF-8 encoding in PowerShell
$env:PYTHONIOENCODING = "utf-8"

# 1. Practice with compact exercises (fill TODOs)
python 06_linked_list/lc_0206_reverse_linked_list_compact.py
python 06_linked_list/lc_0021_merge_two_sorted_lists_compact.py
python 06_linked_list/lc_0143_reorder_list_compact.py
python 06_linked_list/lc_0019_remove_nth_node_from_end_of_list_compact.py
python 06_linked_list/lc_0141_linked_list_cycle_compact.py
python 06_linked_list/lc_0023_merge_k_sorted_lists_compact.py

# 2. Run verified reference solutions
python 06_linked_list/lc_0206_reverse_linked_list_solution.py
python 06_linked_list/lc_0021_merge_two_sorted_lists_solution.py
python 06_linked_list/lc_0143_reorder_list_solution.py
python 06_linked_list/lc_0019_remove_nth_node_from_end_of_list_solution.py
python 06_linked_list/lc_0141_linked_list_cycle_solution.py
python 06_linked_list/lc_0023_merge_k_sorted_lists_solution.py
```

---

## 📚 Deep-Dive Documentation
- **Theoretical Foundations**: [`docs/summary/module_06_linked_list.md`](../docs/summary/module_06_linked_list.md)
- **Interview Traps & Clarifications**: [`docs/clarifications/module_06_linked_list.md`](../docs/clarifications/module_06_linked_list.md)
