# Module 07 Summary: Trees

This document outlines the core mathematical foundations, recursive induction invariants, and search tree mechanics underlying the 11 problems in Module 07.

---

## 1. Tree Topologies & Inductive Definitions

A **Binary Tree** $T$ is an acyclic connected directed graph where each node has at most two outgoing edges (left and right):
$$T = \emptyset \quad \lor \quad T = \langle r, T_{\text{left}}, T_{\text{right}} \rangle$$

* **Depth vs. Height**: The depth of a node is the length of the path from the root down to the node; the height of a node is the length of the longest path from the node down to a leaf.
* **Traversal Paradigms**:
  * **Pre-order (Root, Left, Right)**: Optimal for serialization and tree replication.
  * **In-order (Left, Root, Right)**: Produces strictly sorted ascending sequences in Binary Search Trees.
  * **Post-order (Left, Right, Root)**: Optimal for bottom-up metric aggregation (e.g., maximum depth, path sums).
  * **Level-order (BFS)**: Traverses nodes breadth-first across topological levels.

---

## 2. Invariants & Mathematical Formulations

### Pattern 1: Binary Search Tree (BST) Ordering Invariant (LC 98, LC 235, LC 230)
* **The Global BST Property**: For any node $u$:
  $$\forall x \in T_{\text{left}}(u): \text{val}(x) < \text{val}(u) \quad \text{and} \quad \forall y \in T_{\text{right}}(u): \text{val}(y) > \text{val}(u)$$
* **Range Propagation**: A node $u$ validated under interval bounds $(L, R)$ requires:
  $$u \in (L, R) \implies T_{\text{left}}(u) \subset (L, \text{val}(u)) \quad \text{and} \quad T_{\text{right}}(u) \subset (\text{val}(u), R)$$
* **LCA Split Point Property**: For query nodes $p$ and $q$, the Lowest Common Ancestor is the unique node $u$ where $p$ and $q$ bifurcate into distinct subtrees:
  $$\min(\text{val}(p), \text{val}(q)) \le \text{val}(u) \le \max(\text{val}(p), \text{val}(q))$$

### Pattern 2: Tree Reconstruction from Dual Traversals (LC 105)
* Given Preorder $P$ and Inorder $I$:
  * $P[0]$ uniquely defines the root value $r$.
  * The index $k$ such that $I[k] = r$ partitions $I$ into:
    $$I_{\text{left}} = I[0 \dots k-1], \quad I_{\text{right}} = I[k+1 \dots |I|-1]$$
  * The left subtree has size $S_{\text{left}} = k$. Thus in $P$:
    $$P_{\text{left}} = P[1 \dots k], \quad P_{\text{right}} = P[k+1 \dots |P|-1]$$
  * Pre-indexing $I$ in an auxiliary hash map eliminates $\mathcal{O}(n)$ slicing, enabling strict $\mathcal{O}(n)$ reconstruction.

### Pattern 3: Path Sum Bridge vs. Continuation Invariant (LC 124)
* A path cannot contain branching vertices. At any candidate apex node $u$:
  1. **Bridge Sum (Internal to Subtree)**:
     $$S_{\text{bridge}}(u) = \text{val}(u) + \max(0, G_{\text{left}}) + \max(0, G_{\text{right}})$$
     Evaluates candidates for global maximum path sum.
  2. **Continuation Gain (Returned to Parent)**:
     $$G(u) = \text{val}(u) + \max(0, G_{\text{left}}, G_{\text{right}})$$
     A parent node can only extend one path downwards without inducing an illegal bifurcation.

### Pattern 4: Pre-Order DFS Serialization Bijective Mapping (LC 297)
* Standard pre-order without null indicators cannot uniquely reconstruct a general binary tree (requires both pre-order and in-order).
* **Null-Augmented Pre-order**: By explicitly recording empty child pointers with a sentinel token `"N"`, every binary tree maps bijectively to a unique serialized sequence:
  $$\text{Tree} \iff \text{Tokens}$$
  Reconstruction requires no index search, proceeding in a single deterministic linear pass.
