# Module 11 Summary: Graphs

This document outlines the theoretical frameworks, graph representations, traversal invariants, and advanced disjoint-set data structures underlying Module 11.

---

## 1. Graph Fundamentals & Representations

A graph $G = (V, E)$ consists of a set of vertices $V$ and a set of edges $E \subseteq V \times V$.
* **Implicit Grids as Graphs**: An $M \times N$ matrix is an implicit undirected graph where each cell $(r, c)$ represents a vertex with up to 4 orthogonal neighbors:
  $$\text{Adj}(r, c) = \{(r \pm 1, c), (r, c \pm 1)\} \cap [0, M-1] \times [0, N-1]$$
* **Adjacency Lists**: For sparse graphs ($|E| \ll |V|^2$), an adjacency list consumes $\mathcal{O}(V + E)$ space, enabling linear-time traversals.
* **Adjacency Matrices**: Consumes $\mathcal{O}(V^2)$ space; suitable only for dense graphs or constant-time edge existence queries.

---

## 2. Invariants & Algorithmic Paradigms

### Pattern 1: Grid Connected Components (LeetCode 200: Number of Islands)
* **The Component Model**: An island is an equivalence class of cells under the reflexive, symmetric, transitive closure of the orthogonal adjacency relation on cells with value `'1'`.
* **Traversal Strategy**:
  1. Scan all cells $(r, c) \in M \times N$.
  2. When an unvisited land cell `'1'` is detected, increment `island_count` and launch a complete BFS or DFS exploration.
  3. Mark every reachable land cell as visited (either via an auxiliary `visited` set or by mutating `'1'` $\to$ `'0'` in-place).
* **Complexity**: Each cell is evaluated at most 4 times during neighbor checks and entered into the queue at most once:
  $$\mathcal{T}(M, N) = \mathcal{O}(M \cdot N), \quad \mathcal{S}(M, N) = \mathcal{O}(\min(M, N)) \text{ for BFS queue}$$

### Pattern 2: Hash-Mapped Graph Cloning (LeetCode 133: Clone Graph)
* **The Problem**: Create a deep copy of an arbitrary connected undirected graph containing potential cycles.
* **The Invariant**: A 1-to-1 bijection must exist between nodes in the original graph $u \in V$ and newly allocated nodes $u' \in V'$:
  $$\text{old\_to\_new}: V \to V'$$
* **Memoized DFS Construction**:
  $$\text{clone}(u) = \begin{cases} \text{old\_to\_new}[u] & \text{if } u \in \text{old\_to\_new} \\ u' = \text{Node}(u.\text{val}), \quad \text{old\_to\_new}[u] \leftarrow u' \\ u'.\text{neighbors} \leftarrow [\text{clone}(v) \text{ for } v \in u.\text{neighbors}] & \text{otherwise} \end{cases}$$
* Registering $u'$ in `old_to_new` **before** recursing on its neighbors terminates cycles immediately, preventing infinite call stacks.

### Pattern 3: Multi-Source Reverse Boundary Traversal (LeetCode 417: Pacific Atlantic Water Flow)
* **The Naive Fallacy**: Simulating downhill flow from every individual cell $(r, c)$ leads to redundant repeated searches with complexity $\mathcal{O}((M \cdot N)^2)$.
* **The Inversion Principle (Reverse Reachability)**:
  Instead of flowing *downhill* towards the oceans, start multi-source BFS/DFS from the ocean boundaries and flow *uphill*:
  $$(r_1, c_1) \to (r_2, c_2) \iff \text{height}(r_2, c_2) \ge \text{height}(r_1, c_1)$$
* Compute:
  * $\mathcal{P} = \{\text{cells reachable from Pacific border}\}$
  * $\mathcal{A} = \{\text{cells reachable from Atlantic border}\}$
* The answer is the set intersection $\mathcal{P} \cap \mathcal{A}$. Total complexity shrinks to optimal $\mathcal{O}(M \cdot N)$.

### Pattern 4: Directed Acyclic Graph (DAG) Validation & Topological Sort (LeetCode 207: Course Schedule)
* **Kahn's Algorithm (BFS In-Degree Removal)**:
  1. Compute $\text{in\_degree}[v]$ for all vertices $v \in V$.
  2. Enqueue all vertices with $\text{in\_degree}[v] = 0$ (no unsatisfied dependencies).
  3. While queue is non-empty:
     * Pop vertex $u$, increment `courses_taken`.
     * For each directed outgoing edge $(u, v)$:
       $$\text{in\_degree}[v] \leftarrow \text{in\_degree}[v] - 1$$
       If $\text{in\_degree}[v] == 0$, enqueue $v$.
  4. **Cycle Condition**: The graph is a DAG if and only if `courses_taken == numCourses`. If `courses_taken < numCourses`, any unprocessed vertices belong to or depend upon a directed cycle.
* **Alternative (3-State DFS)**:
  * `0 = UNVISITED`, `1 = VISITING` (currently on call stack), `2 = VISITED` (cleared).
  * If DFS encounters a node with state `1`, a back-edge (cycle) is discovered.

---

## 3. Disjoint Set Union (DSU / Union-Find)

Union-Find manages a partition of a set into disjoint connected components.

```
Initial State:
  (0)   (1)   (2)   (3)   (4)     -> 5 components

After union(0, 1), union(1, 2):
  [0] <- 1 <- 2     (3)   (4)     -> 3 components
```

### Path Compression & Union by Rank
1. **Find with Path Halving / Full Compression**:
   Flattens the tree during root traversal:
   $$\text{parent}[x] \leftarrow \text{parent}[\text{parent}[x]]$$
2. **Union by Rank / Size**:
   Attaches the shallower tree underneath the root of the deeper tree, keeping tree height bounded by $\mathcal{O}(\log V)$.
3. **Inverse Ackermann Function $\alpha(V)$**:
   Combining path compression with union by rank yields an amortized time complexity of:
   $$\mathcal{O}(\alpha(V)) \le 4 \quad \text{for any practical } V \le 10^{80}$$

### Tree Validation Invariants (LeetCode 261: Graph Valid Tree)
A graph $G = (V, E)$ with $|V| = n$ is a tree if and only if **any two** of the following three conditions hold (which together imply the third):
1. $|E| = n - 1$
2. $G$ is connected ($1$ connected component)
3. $G$ is acyclic

By verifying condition 1 first ($|E| == n - 1$) in $\mathcal{O}(1)$ time, we only need to verify either acyclicity or connectivity using Union-Find to prove that $G$ is a valid tree.
