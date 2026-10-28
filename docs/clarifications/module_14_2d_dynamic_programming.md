# Module 14 Clarifications & Pitfalls: 2-D Dynamic Programming

This document details subtle dimension pitfalls, memory aliasing bugs, and subsequence vs. substring distinctions for Module 14.

---

### Q1: The Python 2D List Shallow Copy Trap (`[[0] * n] * m`)
* **The Classical Bug**: Initializing a 2D matrix as:
  ```python
  # DANGEROUS BUG:
  dp = [[0] * n] * m
  ```
* **Why it fails**: In Python, `[obj] * m` creates $m$ references to the **exact same inner list object** in memory.
  * Mutating `dp[0][1] = 5` will simultaneously mutate `dp[1][1] = 5`, `dp[2][1] = 5`, ..., corrupting the entire dynamic programming state table!
* **The Safe Formulation**:
  ```python
  # CORRECT:
  dp = [[0] * n for _ in range(m)]
  ```
  Every row is allocated as an independent list object in memory.

---

### Q2: Subsequence vs. Substring in LCS (LC 1143)
* **Subsequence (LC 1143)**: Characters do **not** need to be contiguous (e.g. `"ace"` is a subsequence of `"abcde"`).
  * State transition on mismatch:
    $$\text{dp}[i][j] = \max(\text{dp}[i+1][j], \; \text{dp}[i][j+1])$$
    We can safely discard either character without losing previously matched characters.
* **Substring (Contiguous)**:
  * State transition on mismatch:
    $$\text{dp}[i][j] = 0$$
    The contiguous chain is broken; length must reset immediately to zero.
* Conflating these two concepts leads to implementing the wrong state transition logic.

---

### Q3: Why Use $(M + 1) \times (N + 1)$ Padding Instead of $M \times N$?
* **Without Padding ($M \times N$)**:
  * Checking `dp[i + 1][j + 1]`, `dp[i + 1][j]`, and `dp[i][j + 1]` requires constant boundary guards:
    `if i + 1 < m and j + 1 < n ...`
* **With Padding ($(M + 1) \times (N + 1)$)**:
  * Row $M$ and Column $N$ are permanently initialized to `0` representing the empty string base cases.
  * Inner loops can safely reference index `i + 1` and `j + 1` without branching or conditional checks, improving code clarity and execution throughput.

---

### Q4: Unique Paths: DP vs. Combinatorics (LC 62)
* **The Combinatorial Shortcut**:
  `math.comb(m + n - 2, m - 1)` computes the answer in $\mathcal{O}(\min(M, N))$ time.
* **Why Interviewers Insist on DP**:
  1. Tests state transition modeling and space reduction principles.
  2. Directly generalizable:
     * In **Unique Paths II** (LC 63), obstacles are added to the grid. The combinatorial formula cannot easily account for obstacles, whereas DP handles it simply:
       ```python
       if obstacleGrid[r][c] == 1:
           dp[c] = 0  # No paths can pass through an obstacle
       ```
     * In **Minimum Path Sum** (LC 64), cells have costs and path sums are minimized: $\text{dp}[r][c] = \text{cost}[r][c] + \min(\text{dp}[r-1][c], \text{dp}[r][c-1])$, which has no combinatorial closed form.
