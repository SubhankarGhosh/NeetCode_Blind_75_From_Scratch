# Module 11 Clarifications & Pitfalls: Graphs

This document details subtle traps, graph orientation gotchas, recursion depth considerations, and disjoint-set performance nuances for Module 11.

---

### Q1: The Python Recursion Limit Trap on Large Grids (LC 200)
* **The Trap**: Writing recursive DFS on an $M \times N = 300 \times 300 = 90,000$ cell grid.
* **Why it fails**: The default Python recursion limit is $1,000$. A snake-shaped island can cause a single DFS branch to recurse $90,000$ deep, triggering:
  `RecursionError: maximum recursion depth exceeded in comparison`
* **Production Recommendation**:
  * Use iterative BFS with `collections.deque` (`popleft()` is $\mathcal{O}(1)$).
  * Or use an explicit iterative DFS stack (`stack = [(r, c)]`).
  * Never rely on `sys.setrecursionlimit()` in production services where thread stack sizes are fixed by OS page allocations.

---

### Q2: Edge Direction in Course Schedule (LC 207)
* **The Trap**: Reversing the directed edge semantics.
* **The Specification**: `prerequisites[i] = [a, b]` means "to take course $a$, you must first take course $b$".
  * The directed dependency is: $b \to a$ ($b$ unlocks $a$).
  * Therefore:
    ```python
    adj[b].append(a)      # b points to a
    in_degrees[a] += 1    # a has an incoming prerequisite dependency
    ```
* If reversed ($a \to b$), the in-degree count measures dependents rather than prerequisites, resulting in inverted topological ordering and incorrect cycle verdicts.

---

### Q3: Undirected Graph DFS: The Immediate Parent Backtrack Trap (LC 261)
* **The Trap**: In an undirected graph, edge $(u, v)$ implies neighbor $v$ lists $u$ in its neighbor list.
* If performing DFS for cycle detection:
  * Visiting $u \to v$, when exploring neighbors of $v$, node $u$ will appear.
  * If the algorithm naively checks `if neighbor in visited: return has_cycle`, it will flag the immediate parent $u$ as a cycle!
* **The Fix**:
  * Pass the caller `parent` in the recursive frame:
    ```python
    def dfs(node, parent):
        visited.add(node)
        for neighbor in adj[node]:
            if neighbor == parent:
                continue  # Ignore trivial bidirectional edge reflection
            if neighbor in visited:
                return False  # True cycle detected!
            if not dfs(neighbor, node):
                return False
        return True
    ```
  * Alternatively, using **Union-Find** completely avoids this parent-tracking bookkeeping because undirected edges are merged symmetrically without directional parent confusion.

---

### Q4: In-Place Mutation ("Sinking Islands") vs. Visited Set (LC 200)
* **The Technique**: Overwriting `grid[r][c] = '0'` upon visiting land.
* **Pros**: Reduces auxiliary memory from $\mathcal{O}(M \cdot N)$ to $\mathcal{O}(1)$ additional heap space.
* **Interview Clarification Rule**:
  * Always ask the interviewer: *"Am I permitted to mutate the input grid, or should the input be treated as immutable / read-only?"*
  * Mutating input in multi-threaded concurrent environments or event-driven systems can cause race conditions or data corruption for other consumers sharing the grid.
  * If read-only is preferred, use a set or bitmask: `visited = set()`.

---

### Q5: Why is $|E| == n - 1$ Not Sufficient on its Own for a Valid Tree? (LC 261)
* **Counterexample**:
  * $n = 4$ nodes: $\{0, 1, 2, 3\}$.
  * Edges: `[[0, 1], [1, 2], [2, 0]]`.
  * $|E| = 3 == n - 1$.
  * However, nodes $0, 1, 2$ form a 3-cycle, and node $3$ is an isolated disconnected component!
* **The Mathematical Rule**:
  * A graph is a tree if and only if:
    1. $|E| == n - 1$, **AND**
    2. The graph has exactly $1$ connected component (or is acyclic).
  * An edge count check alone is a necessary condition, but never a sufficient condition.

---

### Q6: Multi-Source Reverse BFS: Avoiding Duplicate Queue Entries (LC 417)
* When enqueuing boundary nodes for Pacific and Atlantic, mark them as `visited` **immediately upon appending to the queue**, not upon popping.
* **The Pitfall**:
  ```python
  # BAD: Marking visited upon dequeue
  curr = queue.popleft()
  visited.add(curr)
  for neighbor in adj[curr]:
      queue.append(neighbor)  # Same neighbor can be enqueued dozens of times!
  ```
* In grid BFS, multiple adjacent cells can reach the same unvisited cell in the same step. Deferring `visited.add()` until pop causes the queue to explode with exponential redundant nodes, inflating time complexity to $\mathcal{O}(4^{M \cdot N})$.
* **Rule**: Always mark cells `visited.add((nr, nc))` at the moment they are pushed to the queue.
