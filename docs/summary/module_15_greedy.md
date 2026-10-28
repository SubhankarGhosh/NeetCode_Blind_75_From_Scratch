# Module 15 Summary: Greedy

This document formalizes the greedy-choice property, prefix truncation invariants, and frontier relaxation proofs underlying Module 15.

---

## 1. The Greedy Algorithmic Paradigm

A greedy algorithm constructs a solution piece by piece, always choosing the next piece that offers the most immediate benefit. For a greedy approach to yield a globally optimal solution, two conditions must hold:
1. **Greedy-Choice Property**: A global optimum can be arrived at by selecting a locally optimal choice without ever retracting previous decisions.
2. **Optimal Substructure**: An optimal solution to the problem contains optimal solutions to its subproblems.

```
       Dynamic Programming                    Greedy
       -------------------                    ------
Solves all subproblems and         Makes the single locally optimal
memorizes to find the global       choice at each step; never backtracks
optimum (Top-down / Bottom-up).    or reconsiders past choices.
```

---

## 2. Invariants & Mathematical Formulations

### Pattern 1: Negative Prefix Discard / Kadane's Algorithm (LC 53: Maximum Subarray)
Let $A = [a_0, a_1, \dots, a_{n-1}]$. We seek $\max_{0 \le i \le j < n} \sum_{k=i}^j a_k$.

* **The Local Recurrence**:
  Define $S(i)$ as the maximum sum of a contiguous subarray ending strictly at index $i$:
  $$S(i) = \max\big(a_i, \; S(i-1) + a_i\big)$$
* **The Greedy Discard Invariant**:
  If $S(i-1) < 0$, then for any $a_i$:
  $$S(i-1) + a_i < a_i$$
  Any subarray ending at $i$ that includes the preceding subarray ending at $i-1$ has a strictly smaller sum than the single-element subarray $[a_i]$ alone!
  Therefore, we greedily discard the running accumulator whenever it falls below zero:
  $$\text{cur\_sum} \leftarrow \max(0, \text{cur\_sum}) + a_i$$
* **Global Optimum**:
  $$\text{max\_sum} = \max_{0 \le i < n} S(i)$$
  Runs in strict $\mathcal{O}(N)$ time with $\mathcal{O}(1)$ auxiliary space.

---

### Pattern 2: Reachable Frontiers & Goal Contraction (LC 55: Jump Game)
Let $A[i]$ denote the maximum jump length from position $i$.

#### Formulation A: Backward Goal Contraction
* Define $\text{goal} = n - 1$.
* Iterate backwards from $i = n - 2$ down to $0$:
  $$\text{If } i + A[i] \ge \text{goal} \implies \text{goal} \leftarrow i$$
* **Proof by Induction (Exchange Argument)**:
  * Base: Position $n - 1$ is the target destination.
  * Inductive Step: If position $i$ can reach $\text{goal}$, then reaching position $i$ is *sufficient* to reach the end. Hence, we can greedily replace the requirement of reaching $\text{goal}$ with the closer requirement of reaching $i$.
  * If $\text{goal}$ contracts all the way to $0$, the array is reachable from the start.

#### Formulation B: Forward Reachable Frontier
* Maintain $R = \max_{0 \le j \le i} (j + A[j])$, the furthest reachable index.
* For each index $i$:
  * If $i > R$, position $i$ is unreachable from the start $\implies$ return `False`.
  * Update $R \leftarrow \max(R, i + A[i])$.
  * If $R \ge n - 1$, target is reachable $\implies$ return `True`.

Both backward goal contraction and forward reachable frontier algorithms run in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.
