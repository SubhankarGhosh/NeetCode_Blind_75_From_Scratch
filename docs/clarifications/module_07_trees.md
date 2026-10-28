# Module 07 Clarifications & Pitfalls: Trees

This document details common interview traps, boundary edge cases, and recursive stack limitations for Module 07.

---

### Q1: In LC 98, why does checking `node.left.val < node.val < node.right.val` fail?
* **The Classical Interview Trap**: Checking only immediate parent-child relationships validates local ordering but misses global BST violations.
* **Counterexample**:
  ```text
        5
       / \
      4   6
         / \
        3   7
  ```
  * At node 6: $3 < 6 < 7$ is locally true!
  * At node 5: $4 < 5 < 6$ is locally true!
  * But node 3 is in the right subtree of 5, which violates $3 > 5$.
* **Resolution**: You must propagate shrinking valid intervals $(low, high)$ down the tree.

---

### Q2: In LC 124 (Max Path Sum), why clamp child contributions to 0 (`max(0, gain)`)?
* **Question**: What happens if a child subtree returns a negative sum (e.g. $-10$)?
* **Answer**: If including a child branch decreases the overall path sum, we greedily prune it from our path. Clamping with `max(0, dfs(...))` ensures negative subtrees are treated as 0 (i.e., we choose not to extend the path into that child).
* **Edge Case (All Negative Nodes)**: If every node in the entire tree is negative (e.g. `[-3]`), initializing `max_val = float("-inf")` guarantees the algorithm still picks the single least negative node instead of 0.

---

### Q3: In LC 105, why can't there be duplicate values?
* **The Constraint**: The problem explicitly states that all elements in `preorder` and `inorder` are unique.
* **Why this is essential**: If duplicate values existed, looking up the root value in `inorder` would yield multiple ambiguous indices, making it impossible to determine the correct boundary between the left and right subtrees without additional information.

---

### Q4: Recursion Depth Limits in Python
* In Python, the default recursion limit is typically 1000 frames (`sys.getrecursionlimit()`).
* For a degenerate tree of $N = 10^5$ nodes (essentially a linked list), recursive DFS will raise `RecursionError: maximum recursion depth exceeded`.
* In production systems or extreme inputs, convert recursive DFS to an explicit stack-based iteration, or use BFS with a queue.
