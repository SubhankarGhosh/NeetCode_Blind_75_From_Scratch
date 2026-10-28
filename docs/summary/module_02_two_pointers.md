# Module 02 Summary: Two Pointers

This document outlines the core algorithmic foundations, mathematical invariants, and search space elimination proofs underlying the 3 problems in Module 02.

---

## 1. Search Space Pruning Mechanics

The fundamental power of the **Two Pointers** technique lies in reducing polynomial search spaces without visiting unpromising states:
* In a naive brute-force search over pairs $(i, j)$ where $0 \le i < j < n$, the state space has size $\binom{n}{2} = \frac{n(n-1)}{2} = \Theta(n^2)$.
* When monotonic properties exist (e.g. sorted order, or monotonicity of container area bounds), moving a pointer from $i$ to $i+1$ eliminates an entire row or column of candidate pairs that are mathematically proven to be inferior, reducing runtime from $\mathcal{O}(n^2)$ to $\mathcal{O}(n)$.

---

## 2. Invariants & Mathematical Formulations

### Pattern 1: Symmetric Boundary Invariant (LeetCode 125: Valid Palindrome)
* **Definition**: A string $S$ is symmetric if $S[i] = S[|S| - 1 - i]$ for all $0 \le i < \lfloor |S|/2 \rfloor$.
* **In-Place Traversal**: Let $L = 0$ and $R = |S| - 1$.
  * Increment $L$ past non-alphanumeric characters; decrement $R$ past non-alphanumeric characters.
  * Invariant: At each valid comparison step, the substrings $S[0 \dots L-1]$ and $S[R+1 \dots |S|-1]$ are already proven symmetric.
  * If $\text{lower}(S[L]) \ne \text{lower}(S[R])$, the entire string is immediately disqualified.
* **Complexity**: Strict $\mathcal{O}(n)$ time and $\mathcal{O}(1)$ auxiliary space.

### Pattern 2: Higher-Order Sum Reduction (LeetCode 15: 3Sum)
* **Equation**: $a + b + c = 0 \iff b + c = -a$.
* **Sorting Invariant**: Let $A$ be sorted such that $A[0] \le A[1] \le \dots \le A[n-1]$.
  * Fix $A[i] = a$. The target for the remaining sub-array $A[i+1 \dots n-1]$ becomes $T = -A[i]$.
  * Pointers $L = i + 1$ and $R = n - 1$.
  * If $A[L] + A[R] > T$: because $A$ is sorted, $A[R] + A[k] > T$ for all $k \ge L$. Thus $R$ can never pair with any current candidate $\implies R \leftarrow R - 1$.
  * If $A[L] + A[R] < T$: similarly, $A[L] + A[k] < T$ for all $k \le R \implies L \leftarrow L + 1$.
* **Duplicate Elimination**:
  1. Outer loop: if $A[i] = A[i-1]$, skipping $i$ avoids generating identical triplet families.
  2. Inner loop: once a valid triplet is found, increment $L$ and advance past all subsequent elements identical to $A[L-1]$.
* **Early Pruning**: Since $A$ is sorted, if $A[i] > 0$, then $0 < A[i] \le A[L] \le A[R]$, making $A[i] + A[L] + A[R] > 0$ strictly impossible $\implies$ break early.

### Pattern 3: Greedy Bottleneck Elimination (LeetCode 11: Container With Most Water)
* **Capacity Function**:
  $$V(L, R) = (R - L) \times \min(h_L, h_R)$$
* **Monotonic Bottleneck Proof**:
  * Suppose $h_L < h_R$. The height bottleneck is $h_L$.
  * What happens if we decrement $R$ to any $R' < R$?
    $$V(L, R') = (R' - L) \times \min(h_L, h_{R'}) \le (R' - L) \times h_L < (R - L) \times h_L = V(L, R)$$
  * Because the width $(R' - L)$ strictly shrinks and the effective height is bounded by $h_L$, **no rectangle using $L$ with any interior right boundary $R' < R$ can ever exceed $V(L, R)$**.
  * Consequently, the entire set of pairs $\{(L, R') \mid L < R' < R\}$ can be pruned immediately from consideration without evaluation.
  * The only potential candidate that could exceed $V(L, R)$ requires changing the bottleneck, which necessitates advancing $L \leftarrow L + 1$.
* **Complexity**: Exactly $n - 1$ pointer adjustments $\implies \mathcal{O}(n)$ time and $\mathcal{O}(1)$ space.
