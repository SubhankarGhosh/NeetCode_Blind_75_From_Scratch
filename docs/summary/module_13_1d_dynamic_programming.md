# Module 13 Summary: 1-D Dynamic Programming

This document formalizes the recurrence formulations, space-optimization principles, circular subproblem reductions, and state-transition guarantees underlying Module 13.

---

## 1. Dynamic Programming Foundations

Dynamic Programming solves complex problems by breaking them down into simpler subproblems according to two fundamental pillars:
1. **Optimal Substructure**: An optimal solution to the problem contains optimal solutions to subproblems (Bellman's Principle of Optimality).
2. **Overlapping Subproblems**: The recursive space contains repeated evaluations of identical subproblem states, allowing memoization or bottom-up tabulation.

---

## 2. Invariants & Mathematical Formulations

### Pattern 1: Fibonacci-Type Second-Order Transitions (LC 70 & LC 746)
* **Climbing Stairs (LC 70)**:
  $$\text{dp}[i] = \text{dp}[i-1] + \text{dp}[i-2]$$
  State at step $i$ depends strictly on the immediately preceding two steps.
* **Min Cost Climbing Stairs (LC 746)**:
  $$\text{dp}[i] = \min(\text{dp}[i-1] + \text{cost}[i-1], \, \text{dp}[i-2] + \text{cost}[i-2])$$
* **Space Optimization Guarantee**:
  Because $\text{dp}[i]$ has Markovian dependence of order $k=2$, allocating an array of size $\mathcal{O}(N)$ is unnecessary. Maintaining two scalar variables reduces space from $\mathcal{O}(N)$ to strictly $\mathcal{O}(1)$.

### Pattern 2: Non-Adjacent Selection & Circular Reductions (LC 198 & LC 213)
* **House Robber (LC 198)**:
  $$\text{rob}[i] = \max(\text{rob}[i-1], \, \text{rob}[i-2] + \text{nums}[i])$$
  At house $i$, decision is binary:
  * Exclude house $i \implies \text{loot} = \text{rob}[i-1]$
  * Include house $i \implies \text{loot} = \text{rob}[i-2] + \text{nums}[i]$
* **Circular Subproblem Decomposition (LC 213: House Robber II)**:
  In a circular array of size $N$, house $0$ and house $N-1$ are neighbors and cannot both be selected. This boundary constraint decomposes into two independent linear subproblems:
  $$\text{rob}_{\text{circle}}(\text{nums}) = \max\Big(\text{nums}[0], \, \text{rob}_{\text{linear}}(\text{nums}[1:]), \, \text{rob}_{\text{linear}}(\text{nums}[:-1])\Big)$$
  Both subproblems execute in $\mathcal{O}(N)$ time with $\mathcal{O}(1)$ space.

### Pattern 3: Palindromic Center Expansion (LC 5 & LC 647)
* A string of length $N$ contains exactly $2N - 1$ potential palindrome symmetry centers:
  * $N$ odd-length single-character centers: $(i, i)$
  * $N - 1$ even-length two-character centers: $(i, i+1)$
* Expanding outwards from each center until characters mismatch runs in worst-case $\mathcal{O}(N)$ per center, yielding $\mathcal{O}(N^2)$ total time and $\mathcal{O}(1)$ auxiliary space without requiring a full 2D DP matrix.

### Pattern 4: State Branching with Parsing Constraints (LC 91: Decode Ways)
* A digit string $S$ is decoded under constraints: single digit $s[i-1] \in [1, 9]$ and double digit $s[i-2:i] \in [10, 26]$.
* Recurrence:
  $$\text{dp}[i] = \mathbf{1}_{\{s[i-1] \neq '0'\}} \cdot \text{dp}[i-1] \;+\; \mathbf{1}_{\{10 \le \text{int}(s[i-2:i]) \le 26\}} \cdot \text{dp}[i-2]$$
* Leading zero ($s[0] == '0'$) or illegal consecutive zeros (e.g. `"30"`, `"00"`) invalidate branches immediately.

### Pattern 5: Dual Extremes Tracking under Sign Inversion (LC 152: Max Product Subarray)
* Multiplication over integers violates monotonicity: multiplying by a negative number inverts ordering:
  $$x < y \iff -x > -y$$
* Therefore, the maximum product ending at index $i$ may arise from multiplying the **minimum** (most negative) product ending at index $i-1$ by a negative number.
* Maintain both extremes simultaneously:
  $$\begin{aligned}
  \text{candidates} &= \{n, \; n \cdot \text{cur\_max}, \; n \cdot \text{cur\_min}\} \\
  \text{cur\_max} &= \max(\text{candidates}) \\
  \text{cur\_min} &= \min(\text{candidates})
  \end{aligned}$$
* Time: $\mathcal{O}(N)$, Space: $\mathcal{O}(1)$.

### Pattern 6: Unbounded Knapsack (LC 322: Coin Change)
* Given unlimited supply of coin denominations $\mathcal{C}$:
  $$\text{dp}[a] = \min_{c \in \mathcal{C}, \, a \ge c} \big(\text{dp}[a - c] + 1\big), \quad \text{dp}[0] = 0$$
* Bottom-up 1D array traversal guarantees optimal substructure because every amount $a$ builds on previously minimized smaller amounts $a - c$.

### Pattern 7: Boolean Suffix Partitioning (LC 139: Word Break)
* Suffix state definition:
  $$\text{dp}[i] = \bigvee_{w \in \text{Dict}, \, i + |w| \le N, \, s[i : i + |w|] = w} \text{dp}[i + |w|]$$
  Base case: $\text{dp}[N] = \text{True}$.
* Evaluating suffixes from $N-1$ down to 0 enables early `break` on the inner loop once any dictionary word matches and leads to a valid suffix.
