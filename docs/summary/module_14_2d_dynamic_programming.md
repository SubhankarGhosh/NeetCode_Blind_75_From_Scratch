# Module 14 Summary: 2-D Dynamic Programming

This document formalizes 2-dimensional coordinate pathing, string alignment matrix transitions, and dimension-reduction space optimizations underlying Module 14.

---

## 1. 2D Coordinate Grid Dynamic Programming

Coordinate dynamic programming models state spaces defined over 2D geometric planes, grids, or matrices.

### Unique Paths Invariant (LeetCode 62)
A robot at $(0, 0)$ moves strictly right ($\to$) or down ($\downarrow$) towards target $(M-1, N-1)$ in an $M \times N$ matrix.

```
+---+---+---+---+
| S | → | → | → |
+---+---+---+---+
| ↓ |   |   |   |
+---+---+---+---+
| ↓ |   |   | T |
+---+---+---+---+
```

* **Recurrence Relation**:
  Every cell $(r, c)$ can only be accessed from the cell immediately above $(r-1, c)$ or immediately to the left $(r, c-1)$:
  $$\text{dp}[r][c] = \text{dp}[r-1][c] + \text{dp}[r][c-1]$$
* **Boundary Invariant**:
  $$\text{dp}[0][c] = 1 \quad \forall c \in [0, N-1], \qquad \text{dp}[r][0] = 1 \quad \forall r \in [0, M-1]$$
* **The Combinatorial Equivalence (Pascal's Identity)**:
  Any path from $(0, 0)$ to $(M-1, N-1)$ requires exactly $(M-1)$ Down moves and $(N-1)$ Right moves across a total of $(M + N - 2)$ moves. The total number of distinct paths is the binomial coefficient:
  $$\binom{M + N - 2}{M - 1} = \frac{(M + N - 2)!}{(M - 1)! \cdot (N - 1)!}$$
  While computable in $\mathcal{O}(\min(M, N))$ time via arithmetic, the DP formulation effortlessly generalizes to obstacle grids (e.g. Unique Paths II) where combinatorial formulas break.

---

## 2. String Alignment & Subsequence Matrices

Sequence comparison algorithms (e.g., diff tools, git merge, DNA homology alignment) are grounded in the 2D matrix formulation of Longest Common Subsequence (LCS).

### LCS Matrix Formulation (LeetCode 1143)
Let $S = s_0 s_1 \dots s_{M-1}$ and $T = t_0 t_1 \dots t_{N-1}$.
Define $\text{dp}[i][j]$ as the length of the LCS between suffixes $S[i:]$ and $T[j:]$.

```
                 t_j
            +-----------+-----------+
            |  Match    |  Mismatch |
+-----------+-----------+-----------+
|    s_i    | 1 + ↘     | max(↓, →) |
+-----------+-----------+-----------+
```

* **Optimal Substructure Recurrence**:
  $$\text{dp}[i][j] = \begin{cases}
  1 + \text{dp}[i+1][j+1] & \text{if } s_i = t_j \\
  \max\big(\text{dp}[i+1][j], \; \text{dp}[i][j+1]\big) & \text{if } s_i \neq t_j
  \end{cases}$$
* **Boundary Conditions**:
  $$\text{dp}[M][j] = 0 \quad \forall j \in [0, N], \qquad \text{dp}[i][N] = 0 \quad \forall i \in [0, M]$$

---

## 3. Dimension Reduction: $\mathcal{O}(M \cdot N) \longrightarrow \mathcal{O}(\min(M, N))$

In both grid pathing and sequence alignment, the transition for row $i$ depends exclusively on:
1. Cells in row $i + 1$ (or row $i - 1$)
2. Cells to the immediate left or right in current row $i$

Because no dependencies reach further than 1 step back in the row index, storing the entire $M \times N$ matrix in memory is unnecessary:

| Paradigm | 2D Memory | 1D Optimized Memory | Memory Allocation Reduction |
| :--- | :---: | :---: | :---: |
| Unique Paths | $\mathcal{O}(M \cdot N)$ | $\mathcal{O}(\min(M, N))$ | $100 \times 100 \to 100$ integers |
| Longest Common Subsequence | $\mathcal{O}(M \cdot N)$ | $\mathcal{O}(\min(M, N))$ | $1000 \times 1000 \to 1000$ integers |

By ensuring the shorter string/dimension defines the array length ($N \le M$), cache performance is maximized and auxiliary heap memory is bounded by $\mathcal{O}(\min(M, N))$.
