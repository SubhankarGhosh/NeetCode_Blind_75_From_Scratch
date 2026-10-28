# Module 09 Summary: Heap / Priority Queue

This document outlines the core mathematical foundations, heap structural properties, and dual-heap balance invariants underlying Module 09.

---

## 1. Complete Binary Tree & Heap Property

A **Binary Heap** is a complete binary tree satisfying the heap-order property:
* **Min-Heap Property**: For any node $u$ other than the root, $\text{val}(\text{parent}(u)) \le \text{val}(u)$. The root holds the minimum element.
* **Max-Heap Property**: For any node $u$ other than the root, $\text{val}(\text{parent}(u)) \ge \text{val}(u)$. The root holds the maximum element.
* **Array-Backed Representation**:
  * Root is at index 0.
  * For node at index $i$: $\text{left}(i) = 2i + 1$, $\text{right}(i) = 2i + 2$, $\text{parent}(i) = \lfloor (i - 1)/2 \rfloor$.
* **Complexity**: Insertion (`sift-up`) and deletion (`sift-down`) take strictly $\mathcal{O}(\log n)$ time, while inspection (`peek`) takes $\mathcal{O}(1)$ time.

---

## 2. Invariants & Mathematical Formulations

### Dual-Heap Streaming Partition Invariant (LeetCode 295)
Given an unbounded sequence of real numbers $X = (x_1, x_2, \dots, x_n)$, let $X_{(1)} \le X_{(2)} \le \dots \le X_{(n)}$ represent the sorted permutation at step $n$.

We partition $X$ into two disjoint heaps:
1. $\mathcal{H}_{\text{small}}$: A **Max-Heap** holding the lower half:
   $$\mathcal{H}_{\text{small}} = \{X_{(1)}, X_{(2)}, \dots, X_{(\lceil n/2 \rceil)}\}$$
2. $\mathcal{H}_{\text{large}}$: A **Min-Heap** holding the upper half:
   $$\mathcal{H}_{\text{large}} = \{X_{(\lceil n/2 \rceil + 1)}, \dots, X_{(n)}\}$$

### The Two System Invariants
1. **The Order Invariant**:
   $$\max(\mathcal{H}_{\text{small}}) \le \min(\mathcal{H}_{\text{large}})$$
   If a new number violates this condition, the maximum of $\mathcal{H}_{\text{small}}$ is transferred to $\mathcal{H}_{\text{large}}$ in $\mathcal{O}(\log n)$.
2. **The Size Invariant**:
   $$\Big| |\mathcal{H}_{\text{small}}| - |\mathcal{H}_{\text{large}}| \Big| \le 1$$
   If one heap exceeds the other by more than 1 element, its root is popped and pushed into the opposing heap.

### Instantaneous Median Derivation:
$$\text{median} = \begin{cases} 
\max(\mathcal{H}_{\text{small}}) & \text{if } |\mathcal{H}_{\text{small}}| > |\mathcal{H}_{\text{large}}| \\
\min(\mathcal{H}_{\text{large}}) & \text{if } |\mathcal{H}_{\text{large}}| > |\mathcal{H}_{\text{small}}| \\
\frac{\max(\mathcal{H}_{\text{small}}) + \min(\mathcal{H}_{\text{large}})}{2} & \text{if } |\mathcal{H}_{\text{small}}| = |\mathcal{H}_{\text{large}}|
\end{cases}$$
Because the roots of both heaps are accessible in $\mathcal{O}(1)$ time, querying the median never requires sorting or linear scanning.
