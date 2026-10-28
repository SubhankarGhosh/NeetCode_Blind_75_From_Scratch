# Module 10 Summary: Backtracking

This document outlines the core mathematical foundations, state-space tree exploration models, and systematic branch pruning techniques underlying Module 10.

---

## 1. Backtracking & State Space Trees

**Backtracking** is a general algorithmic paradigm for solving constraint satisfaction problems by systematically searching through a state space tree:
* **The Trial-and-Error Paradigm**: Candidates are built incrementally. As soon as a candidate partial solution is proven mathematically incapable of yielding a valid complete solution, the algorithm abandons it (**prunes** the branch) and reverts (**backtracks**) the state.
* **State Space Formalism**:
  $$\mathcal{S} = \langle \text{partial\_candidate}, \text{decision\_index}, \text{accumulated\_cost} \rangle$$
* State transitions must satisfy reversibility: every `state.append(x)` must be coupled symmetrically with a trailing `state.pop()` upon recursive unwind.

---

## 2. Invariants & Mathematical Formulations

### Pattern 1: Binary Decision Trees vs. Multiway Loops (LeetCode 39: Combination Sum)
* **The Problem**: A set of distinct integers $\mathcal{C}$ can be chosen arbitrarily many times to sum to target $T$.
* **The Inclusion/Exclusion Invariant**:
  At candidate index $i$ with running sum $S$:
  1. *Branch 1 (Include)*: Choose candidate $c_i$. The new sum becomes $S + c_i$. Because $c_i$ may be reused, stay at index $i$:
     $$\text{dfs}(i, \text{cur} \cup [c_i], S + c_i)$$
  2. *Branch 2 (Exclude)*: Backtrack by popping $c_i$. Never choose $c_i$ again by advancing to index $i + 1$:
     $$\text{dfs}(i + 1, \text{cur}, S)$$
* **Duplicate Freedom Proof**: Every combination is formed by a strictly ordered sequence of candidate counts:
  $$\sum_{j=0}^{k-1} n_j \cdot c_j = T \quad (n_j \ge 0)$$
  Because candidate index $i$ only moves forward monotonically, permutations of identical element multisets (e.g., $[2, 3, 2]$ vs $[2, 2, 3]$) can never be generated twice.
* **Complexity**: Max tree depth $D = \lfloor T / \min(\mathcal{C}) \rfloor$. Total states bounded by $\mathcal{O}(2^D)$.

### Pattern 2: Graph Path Exploration & Spatial Pruning (LeetCode 79: Word Search)
* **The Problem**: Search for an ordered string $W = w_0 w_1 \dots w_{L-1}$ in a 2D grid of size $M \times N$.
* **Grid Transition Invariant**:
  From cell $(r, c)$ matching $w_k$:
  * Mark $(r, c)$ visited to prevent immediate loopback.
  * Orthogonal fan-out: at $k=0$, there are at most 4 neighboring choices; for $k \ge 1$, the predecessor cell is already marked visited, bounding active branches by at most 3.
  * Maximum search tree size per starting cell is $4 \cdot 3^{L-1} = \mathcal{O}(3^L)$.
* **Heuristic Optimizations**:
  1. *Frequency Pre-check*: If $\text{count}_{\text{board}}(c) < \text{count}_{\text{word}}(c)$ for any character $c$, reject in $\mathcal{O}(MN)$ time without exploring a single DFS path.
  2. *Prefix vs. Suffix Inversion*: If $w_0$ is extremely frequent on the board (e.g. 50 `'A'`s) but $w_{L-1}$ is extremely rare (e.g. 1 `'Z'`), starting search from $w_0$ generates massive dead-end tree expansions. Reversing the word ($W \leftarrow W^R$) starts DFS from the bottleneck letter, shrinking branch exploration by orders of magnitude.
