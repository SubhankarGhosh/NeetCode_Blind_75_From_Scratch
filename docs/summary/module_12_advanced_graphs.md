# Module 12 Summary: Advanced Graphs

This document formalizes the lexicographical dependency theory, directed acyclic graph (DAG) synthesis from partial orders, and topological sorting invariants underlying Module 12.

---

## 1. Formal Foundations of Lexicographical Ordering

Let $\Sigma$ be a finite alphabet with a total strict order $\prec$. A word $S = s_0 s_1 \dots s_{m-1}$ is lexicographically strictly smaller than word $T = t_0 t_1 \dots t_{n-1}$ ($S <_{\text{lex}} T$) if and only if either:
1. **Divergent Character Precedence**: There exists an index $k < \min(m, n)$ such that $s_i = t_i$ for all $0 \le i < k$, and:
   $$s_k \prec t_k$$
2. **Proper Prefix Precedence**: $m < n$ and $s_i = t_i$ for all $0 \le i < m$ ($S$ is a proper prefix of $T$).

### The First Divergence Principle
Given a sorted sequence of words $\langle W_0, W_1, \dots, W_{N-1} \rangle$:
* For any adjacent pair $(W_i, W_{i+1})$, examine characters from index $j = 0$:
  * At the first index $j$ where $W_i[j] \neq W_{i+1}[j]$, we establish the single directed constraint:
    $$W_i[j] \longrightarrow W_{i+1}[j]$$
  * **Critical Observation**: Characters at indices $j' > j$ provide **zero ordering information**! (e.g., in `"apple"` vs `"apply"`, `'e'` precedes `'y'`, but this tells us nothing about `'p'`, `'l'`, or `'a'`).
* Checking only **adjacent** word pairs is sufficient because lexicographical ordering is transitive: if $W_i <_{\text{lex}} W_{i+1}$ for all $i$, then $W_a <_{\text{lex}} W_b$ holds for all $a < b$.

---

## 2. Invalid Dictionary Invariants

A candidate dictionary is invalid (requiring an empty output `""`) under exactly two failure conditions:

### 1. Prefix Contradiction (Subsumption Violation)
If $W_{i+1}$ is a strict prefix of $W_i$ (i.e., $|W_i| > |W_{i+1}|$ and $W_i[0 : |W_{i+1}|] == W_{i+1}$), then $W_i$ cannot precede $W_{i+1}$ in any lexicographical system:
$$\text{Example: } W_0 = \text{"banana"}, \quad W_1 = \text{"ban"} \implies \text{Mathematically impossible}$$

### 2. Dependency Cycles (Lack of Strict Partial Order)
If the set of induced precedence constraints contains a directed cycle:
$$c_0 \longrightarrow c_1 \longrightarrow \dots \longrightarrow c_k \longrightarrow c_0$$
then $c_0 \prec c_0$, violating the irreflexive property of strict orders.

---

## 3. Algorithmic Formulation: Kahn's Algorithm

1. **Vocabulary Initialization**:
   Every character $c \in \Sigma_{\text{obs}}$ (where $\Sigma_{\text{obs}} = \bigcup_{W \in \text{words}} \text{set}(W)$) must appear in the final alphabet. Initialize:
   $$\text{adj}[c] \leftarrow \emptyset, \quad \text{in\_degree}[c] \leftarrow 0 \quad \forall c \in \Sigma_{\text{obs}}$$
2. **Edge Construction**:
   Iterate over adjacent pairs $(W_i, W_{i+1})$. Detect first differing characters $u = W_i[j]$ and $v = W_{i+1}[j]$. If $v \notin \text{adj}[u]$:
   $$\text{adj}[u] \leftarrow \text{adj}[u] \cup \{v\}, \quad \text{in\_degree}[v] \leftarrow \text{in\_degree}[v] + 1$$
3. **Queue-Based BFS (Topological Linearization)**:
   * Enqueue all $c \in \Sigma_{\text{obs}}$ with $\text{in\_degree}[c] == 0$.
   * Dequeue $u$, append $u$ to result list.
   * For each neighbor $v \in \text{adj}[u]$, decrement $\text{in\_degree}[v]$. If $0$, enqueue $v$.
4. **Completeness & Cycle Verification**:
   $$\text{len}(\text{result}) == |\Sigma_{\text{obs}}| \iff \text{Valid DAG exists}$$
   If $\text{len}(\text{result}) < |\Sigma_{\text{obs}}|$, at least one directed cycle prevented the remaining nodes from reaching an in-degree of 0. Return `""`.

---

## 4. Complexity Analysis

Let:
* $N$ = number of words in `words`.
* $L$ = maximum length of a word.
* $C = \sum_{i} |W_i| \le N \cdot L$ = total character count across all words.
* $U = |\Sigma_{\text{obs}}| \le 26$ = count of unique letters.

| Phase | Time Complexity | Space Complexity |
| :--- | :---: | :---: |
| Vocabulary Extraction | $\mathcal{O}(C)$ | $\mathcal{O}(U) = \mathcal{O}(1)$ |
| Pairwise Comparison & Edge Construction | $\mathcal{O}(\min(C, N \cdot L))$ | $\mathcal{O}(\min(U^2, N)) = \mathcal{O}(1)$ |
| Kahn's Topological Sort | $\mathcal{O}(U + |E|) = \mathcal{O}(1)$ | $\mathcal{O}(U) = \mathcal{O}(1)$ |
| **Total** | $\mathcal{O}(C)$ | $\mathcal{O}(1)$ |
