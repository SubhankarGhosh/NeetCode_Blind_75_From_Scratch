# Module 09 Clarifications & Pitfalls: Heap / Priority Queue

This document outlines common interview traps, language implementation details, and interview follow-up questions for Module 09.

---

### Q1: Simulating Max-Heaps in Python (`heapq`)
* **Standard Python Behavior**: Python's built-in `heapq` module strictly implements a **Min-Heap**.
* **The Negative Value Idiom**: To represent a Max-Heap, multiply values by $-1$ upon insertion (`heappush(heap, -val)`) and negate them upon extraction (`-heappop(heap)`).
  * *Beware of Float Zeros*: Note that in Python `-0.0 == 0.0`. For integer values, negation is exact.

---

### Q2: Why not use a Self-Balancing Binary Search Tree (AVL / Red-Black Tree)?
* A self-balancing BST with subtree size counts can insert in $\mathcal{O}(\log n)$ and find the median (order statistic) in $\mathcal{O}(\log n)$.
* **Why Heaps are Superior**:
  * Binary heaps have lower constant factors, zero pointer overhead, and flat array-backed storage ($2i + 1$, $2i + 2$).
  * Querying the median is $\mathcal{O}(1)$ with dual heaps versus $\mathcal{O}(\log n)$ in augmented balanced trees.

---

### Q3: Common Interview Follow-Up Questions for LC 295
1. **Follow-Up 1: What if all stream numbers are in the range $[0, 100]$?**
   * *Optimal Solution*: Count-based frequency array `counts = [0] * 101`!
   * Adding a number is $\mathcal{O}(1)$.
   * Finding the median requires scanning the 101 buckets in $\mathcal{O}(100) = \mathcal{O}(1)$ time with strictly $\mathcal{O}(1)$ space.
2. **Follow-Up 2: What if 99% of stream numbers are in the range $[0, 100]$ and 1% are outliers?**
   * *Optimal Solution*: Use a hybrid approach:
     * A frequency array of size 101 for the $99\%$ dense core.
     * Two small dual heaps (or balanced BSTs) for outliers smaller than 0 and larger than 100.
     * Because $99\%$ of numbers fall within $[0, 100]$, the median is almost always inside the bucket array, allowing sub-microsecond lookups.
