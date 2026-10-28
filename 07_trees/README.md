# Module 07: Trees

Mastering hierarchical recursive traversals (Pre-order, In-order, Post-order), Level-Order BFS, Binary Search Tree (BST) invariant validation, path split-sums, and tree serialization across 11 foundational LeetCode problems.

---

## 📋 Problem Map

| Problem | Difficulty | Key Paradigm | Time | Space | Status |
| :--- | :---: | :--- | :---: | :---: | :---: |
| [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Easy | Recursive Child Pointer Swap | $\mathcal{O}(n)$ | $\mathcal{O}(h)$ | 🟢 Complete |
| [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | Post-Order Subtree Height Accumulation | $\mathcal{O}(n)$ | $\mathcal{O}(h)$ | 🟢 Complete |
| [100. Same Tree](https://leetcode.com/problems/same-tree/) | Easy | Simultaneous Structural DFS | $\mathcal{O}(\min(n, m))$ | $\mathcal{O}(h)$ | 🟢 Complete |
| [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | Easy | Subtree Root Matching + DFS Branching | $\mathcal{O}(n \cdot m)$ | $\mathcal{O}(h)$ | 🟢 Complete |
| [235. Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Medium | BST Value Split Point Navigation | $\mathcal{O}(h)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | BFS Queue Level-Batching | $\mathcal{O}(n)$ | $\mathcal{O}(w)$ | 🟢 Complete |
| [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Medium | Range Boundary $(low, high)$ Propagation | $\mathcal{O}(n)$ | $\mathcal{O}(h)$ | 🟢 Complete |
| [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Medium | Iterative Stack-Based In-Order Traversal | $\mathcal{O}(h + k)$ | $\mathcal{O}(h)$ | 🟢 Complete |
| [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Medium | Preorder Root + Inorder Partition Indexing | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | 🟢 Complete |
| [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Hard | Post-Order Split Apex vs. Continuous Branch | $\mathcal{O}(n)$ | $\mathcal{O}(h)$ | 🟢 Complete |
| [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Hard | Pre-Order DFS with Null Sentinels (`"N"`) | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | 🟢 Complete |

---

## 🏃 Execution Instructions

Run exercises standalone with zero third-party dependencies:

```powershell
# Set UTF-8 encoding in PowerShell
$env:PYTHONIOENCODING = "utf-8"

# 1. Practice with compact exercises (fill TODOs)
python 07_trees/lc_0226_invert_binary_tree_compact.py
python 07_trees/lc_0104_maximum_depth_of_binary_tree_compact.py
python 07_trees/lc_0100_same_tree_compact.py
python 07_trees/lc_0572_subtree_of_another_tree_compact.py
python 07_trees/lc_0235_lowest_common_ancestor_of_a_binary_search_tree_compact.py
python 07_trees/lc_0102_binary_tree_level_order_traversal_compact.py
python 07_trees/lc_0098_validate_binary_search_tree_compact.py
python 07_trees/lc_0230_kth_smallest_element_in_a_bst_compact.py
python 07_trees/lc_0105_construct_binary_tree_from_preorder_and_inorder_traversal_compact.py
python 07_trees/lc_0124_binary_tree_maximum_path_sum_compact.py
python 07_trees/lc_0297_serialize_and_deserialize_binary_tree_compact.py

# 2. Run verified reference solutions
python 07_trees/lc_0226_invert_binary_tree_solution.py
python 07_trees/lc_0104_maximum_depth_of_binary_tree_solution.py
python 07_trees/lc_0100_same_tree_solution.py
python 07_trees/lc_0572_subtree_of_another_tree_solution.py
python 07_trees/lc_0235_lowest_common_ancestor_of_a_binary_search_tree_solution.py
python 07_trees/lc_0102_binary_tree_level_order_traversal_solution.py
python 07_trees/lc_0098_validate_binary_search_tree_solution.py
python 07_trees/lc_0230_kth_smallest_element_in_a_bst_solution.py
python 07_trees/lc_0105_construct_binary_tree_from_preorder_and_inorder_traversal_solution.py
python 07_trees/lc_0124_binary_tree_maximum_path_sum_solution.py
python 07_trees/lc_0297_serialize_and_deserialize_binary_tree_solution.py
```

---

## 📚 Deep-Dive Documentation
- **Theoretical Foundations**: [`docs/summary/module_07_trees.md`](../docs/summary/module_07_trees.md)
- **Interview Traps & Clarifications**: [`docs/clarifications/module_07_trees.md`](../docs/clarifications/module_07_trees.md)
