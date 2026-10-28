# Module 05 Summary: Binary Search

This document outlines the core algorithmic foundations, search space elimination invariants, and inflection point mechanics underlying Module 05.

---

## 1. The Binary Search Invariant Principle

Binary search operates on a search space $[L, R]$ by selecting a test point $M = \lfloor (L + R)/2 \rfloor$ and evaluating a predicate $P(M)$:
* When $P(M)$ induces a monotonic partition (e.g. all False values followed by all True values), testing $M$ eliminates half of the remaining candidates.
* Recurrence: $T(n) = T(n/2) + \mathcal{O}(1) \implies T(n) = \Theta(\log n)$.

---

## 2. Theoretical Invariants in Rotated Sorted Arrays

A rotated sorted array $A$ is formed by cyclically shifting an ascending sorted array of unique elements by $k$ positions:
$$A = [a_k, a_{k+1}, \dots, a_{n-1}, a_0, a_1, \dots, a_{k-1}]$$

It consists of two ascending sorted segments separated by a single **inflection point** (the cliff where $A[k-1] > A[k]$).

### Invariant 1: Inflection Point Localization (LeetCode 153)
* We compare $A[M]$ against the right boundary $A[R]$:
  1. **Case $A[M] > A[R]$**:
     * Because all elements are unique and the right portion has wrapped around to values smaller than $A[0]$, having $A[M] > A[R]$ proves the inflection cliff lies strictly in the interval $[M + 1, R]$.
     * Therefore, the global minimum is in $[M + 1, R] \implies L \leftarrow M + 1$.
  2. **Case $A[M] \le A[R]$**:
     * The subarray $A[M \dots R]$ is properly sorted.
     * The minimum could be $A[M]$ itself, or it must lie to the left in $[L, M]$.
     * Therefore, $R \leftarrow M$.
* Termination: $L = R$ isolates the unique global minimum in $\lfloor \log_2 n \rfloor$ iterations.

### Invariant 2: Sorted-Half Partitioning (LeetCode 33)
* In any rotated sorted array of unique elements, for any midpoint $M$:
  $$\textbf{At least one of the two halves } [L, M] \textbf{ or } [M, R] \textbf{ is strictly sorted!}$$
* **Step 1: Identify the Sorted Half**:
  * If $A[L] \le A[M]$: The left half $[L, M]$ is guaranteed to be strictly sorted.
  * Else: The right half $[M, R]$ is guaranteed to be strictly sorted.
* **Step 2: Exact Interval Containment Test**:
  * If the left half is sorted:
    $$\text{target} \in [A[L], A[M]) \implies R \leftarrow M - 1 \quad (\text{search left})$$
    $$\text{otherwise} \implies L \leftarrow M + 1 \quad (\text{search right})$$
  * If the right half is sorted:
    $$\text{target} \in (A[M], A[R]] \implies L \leftarrow M + 1 \quad (\text{search right})$$
    $$\text{otherwise} \implies R \leftarrow M - 1 \quad (\text{search left})$$
* This preserves the $\mathcal{O}(\log n)$ runtime bound without requiring finding the rotation pivot first.
