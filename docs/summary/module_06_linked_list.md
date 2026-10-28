# Module 06 Summary: Linked List

This document outlines the core memory mechanics, pointer invariants, and structural reduction algorithms underlying Module 06.

---

## 1. Singly-Linked Memory Architecture

Unlike contiguous dynamic arrays where element $i$ resides at address $\text{base} + i \times \text{size}$, a **Singly-Linked List** is a non-contiguous chain of heap-allocated node structures:
$$\text{Node}_i = \langle \text{val}_i, \text{next}_i \to \text{Node}_{i+1} \rangle$$

* **Strengths**: True $\mathcal{O}(1)$ insertion and deletion given a reference to the preceding node (no shifting of subsequent elements required).
* **Trade-offs**: Lack of random access ($\mathcal{O}(n)$ indexing), poor spatial memory locality (pointer indirection causes CPU cache misses), and overhead of pointer storage.

---

## 2. Invariants & Key Algorithmic Paradigms

### Pattern 1: In-Place Pointer Redirection (LeetCode 206)
* **Invariant**: At step $i$, all nodes in the prefix $[1 \dots i-1]$ are already reversed pointing backward: $\text{Node}_1 \leftarrow \text{Node}_2 \dots \leftarrow \text{Node}_{i-1} = \text{prev}$.
* **Atomic Transfer**:
  $$\text{nxt} \leftarrow \text{curr.next}$$
  $$\text{curr.next} \leftarrow \text{prev}$$
  $$\text{prev} \leftarrow \text{curr}, \quad \text{curr} \leftarrow \text{nxt}$$
* Preserves strictly $\mathcal{O}(n)$ time and $\mathcal{O}(1)$ auxiliary space without node re-allocation.

### Pattern 2: The Sentinel / Dummy Head Pattern (LeetCode 21 & LC 19)
* **The Boundary Problem**: When the node to be modified or prepended is the `head` itself, algorithms typically require cumbersome `if head is None` or special-case checks.
* **The Dummy Invariant**: Introducing an immutable dummy node $D$ such that $D.\text{next} = \text{head}$ transforms every node (including the original head) into an *interior* node with a valid predecessor.
* The result is always extracted cleanly via $D.\text{next}$.

### Pattern 3: Fixed-Offset Two Pointers (LeetCode 19)
* To remove the $n$-th node from the end in a single pass without computing total length $L$:
  * Place pointer $L$ at dummy $D$, and pointer $R$ at head.
  * Advance $R$ by $n$ steps: the distance between $L$ and $R$ is fixed at $n + 1$ nodes.
  * Advance $L$ and $R$ synchronously until $R = \text{None}$:
    $$\text{pos}(R) = L + 1 \implies \text{pos}(L) = (L + 1) - (n + 1) = L - n$$
  * Node $L$ points exactly to the predecessor of the node to be removed.
  * Bypass target: $L.\text{next} \leftarrow L.\text{next.next}$.

### Pattern 4: Floyd's Cycle-Finding Algorithm (LeetCode 141)
* **The Two-Speed Invariant**:
  * $\text{slow}$ advances by 1 node per tick: $S_t = t$.
  * $\text{fast}$ advances by 2 nodes per tick: $F_t = 2t$.
* **Convergence Proof**:
  * Suppose the list has a linear prefix of length $K$ and a cycle of length $C$.
  * After $K$ steps, $\text{slow}$ enters the cycle. $\text{fast}$ is already in the cycle at position $(2K \bmod C)$.
  * Inside the cycle, the relative closing speed is $2 - 1 = 1$ node per iteration.
  * The distance between them decreases by 1 on every step. Therefore, $\text{fast}$ must collide with $\text{slow}$ in at most $C$ steps, bounding total runtime strictly by $\mathcal{O}(K + C) = \mathcal{O}(n)$ with $\mathcal{O}(1)$ space.

### Pattern 5: Multiway Divide-and-Conquer Merging (LeetCode 23)
* Merging $k$ sorted lists pairwise:
  * Level 0: $k$ lists.
  * Level 1: $k/2$ lists merged.
  * Level $d$: $k/2^d$ lists merged.
  * Total tree depth: $\lceil \log_2 k \rceil$.
  * At each depth level, every node in the entire dataset participates in exactly one two-way merge $\implies \mathcal{O}(N)$ work per level.
  * Total Time: $\mathcal{O}(N \log k)$, vastly superior to sequential accumulation $\mathcal{O}(N k)$.
