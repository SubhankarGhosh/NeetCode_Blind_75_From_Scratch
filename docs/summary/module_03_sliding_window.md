# Module 03 Summary: Sliding Window

This document outlines the core algorithmic foundations, window invariant models, and amortized complexity bounds for the 4 problems in Module 03.

---

## 1. Sliding Window Theoretical Framework

A sliding window evaluates contiguous subsegments $[L, R]$ of a linear sequence of length $n$:
* **Naive Substring Generation**: Generating all $\binom{n+1}{2} = \Theta(n^2)$ contiguous substrings and validating an objective function takes $\mathcal{O}(n^2 \cdot \text{Cost})$.
* **Sliding Window Optimization**: By monotonically advancing $R$ to expand the window and monotonically advancing $L$ to contract it when an invariant is violated, each pointer moves at most $n$ times. The total number of state transitions is bounded by $2n = \mathcal{O}(n)$.

---

## 2. Invariants & Mathematical Formulations

### Pattern 1: Inflection-Point Sliding Window (LeetCode 121: Best Time to Buy and Sell Stock)
* Let $P[0 \dots n-1]$ be the price series. Profit for buying at $L$ and selling at $R$ is $\Delta(L, R) = P[R] - P[L]$.
* **Invariant**: If $P[R] < P[L]$, then for any future day $R' > R$:
  $$P[R'] - P[R] > P[R'] - P[L]$$
* Buying at $R$ strictly dominates buying at $L$ for all future trades. We can safely reset $L \leftarrow R$ in $\mathcal{O}(1)$.

### Pattern 2: Hash-Indexed Pointer Leaping (LeetCode 3: Longest Substring Without Repeating Characters)
* Let $\mathcal{M}: \Sigma \to \mathbb{Z}$ record the last seen index of each character: $\mathcal{M}[c] = \text{index}$.
* **Window Invariant**: For window $[L, R]$, all characters in $S[L \dots R]$ are mutually distinct.
* When inspecting character $c = S[R]$:
  * If $c \in \mathcal{M}$ and $\mathcal{M}[c] \ge L$, a collision occurs inside the active window.
  * To eliminate the duplicate, $L$ must jump past the previous occurrence:
    $$L \leftarrow \mathcal{M}[c] + 1$$
* Pointer leaping eliminates incremental while loops, reducing operations to a strict single pass with $\mathcal{O}(\min(n, |\Sigma|))$ space.

### Pattern 3: Monotonic Frequency Bound (LeetCode 424: Longest Repeating Character Replacement)
* For any window $[L, R]$ of length $W = R - L + 1$, let $f_{\max} = \max_{c \in \Sigma} \text{count}(c)$.
* The minimum number of replacements needed to make all characters identical is:
  $$\text{cost}(L, R) = W - f_{\max} = (R - L + 1) - f_{\max}$$
* **Validity Condition**: $(R - L + 1) - f_{\max} \le k$.
* **The Monotonic Optimization**:
  * When contracting the window ($L \leftarrow L + 1$), why don't we recompute $f_{\max}$ across the 26 characters?
  * *Proof*: A window of length $W$ can only become our new global maximum if $W > W_{\max}$. Because $W = f_{\max} + k$, achieving a strictly larger valid window requires discovering a *strictly higher* $f_{\max}$. A window with an equal or lower $f_{\max}$ can never break our record. Thus, maintaining a non-decreasing $f_{\max}$ register preserves correctness while ensuring $\mathcal{O}(1)$ time per character.

### Pattern 4: Dual Constraint Counters (LeetCode 76: Minimum Window Substring)
* Given multiset requirements $\mathcal{T} = \text{Counter}(T)$, let $N_{\text{need}} = |\text{keys}(\mathcal{T})|$.
* Let $N_{\text{have}}$ count how many distinct keys $c$ currently satisfy $\text{window}[c] \ge \mathcal{T}[c]$.
* **Two-Phase Operation**:
  1. *Expansion Phase*: Advance $R$ until $N_{\text{have}} = N_{\text{need}}$ (window becomes valid).
  2. *Contraction Phase*: Advance $L$ while maintaining $N_{\text{have}} = N_{\text{need}}$, recording minimum length $(R - L + 1)$, until the window becomes deficient ($N_{\text{have}} < N_{\text{need}}$).
* Ensures strictly $\mathcal{O}(|S| + |T|)$ runtime without repeated hash map scans.
