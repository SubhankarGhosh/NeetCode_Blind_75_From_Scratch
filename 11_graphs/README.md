# Module 11: Graphs

Mastering graph modeling, grid traversals (BFS/DFS), connected component identification, deep graph cloning, reverse multi-source exploration, directed acyclic graph (DAG) cycle detection via topological sorting, and Disjoint Set Union (Union-Find) with path compression and rank optimization across 6 foundational LeetCode problems.

---

## 📋 Problem Map

| Problem | Difficulty | Key Paradigm | Time | Space | Status |
| :--- | :---: | :--- | :---: | :---: | :---: |
| [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | 2D Grid Component Discovery (BFS/DFS) | $\mathcal{O}(M \cdot N)$ | $\mathcal{O}(M \cdot N)$ | 🟢 Complete |
| [133. Clone Graph](https://leetcode.com/problems/clone-graph/) | Medium | Hash-Mapped Recursive Deep Copy (DFS) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ | 🟢 Complete |
| [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Medium | Reverse Multi-Source Uphill BFS from Ocean Borders | $\mathcal{O}(M \cdot N)$ | $\mathcal{O}(M \cdot N)$ | 🟢 Complete |
| [207. Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | Kahn's Algorithm / In-Degree Topological Sort | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ | 🟢 Complete |
| [261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) *(LintCode 178)* | Medium | Disjoint Set Union (Union-Find) Cycle Check | $\mathcal{O}(V + E \cdot \alpha(V))$ | $\mathcal{O}(V)$ | 🟢 Complete |
| [323. Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) *(LintCode 591)* | Medium | DSU with Path Compression and Union by Rank | $\mathcal{O}(V + E \cdot \alpha(V))$ | $\mathcal{O}(V)$ | 🟢 Complete |

---

## 🏃 Execution Instructions

Run exercises standalone with zero third-party dependencies:

```powershell
# Set UTF-8 encoding in PowerShell
$env:PYTHONIOENCODING = "utf-8"

# 1. Practice with compact exercises (fill TODOs)
python 11_graphs/lc_0200_number_of_islands_compact.py
python 11_graphs/lc_0133_clone_graph_compact.py
python 11_graphs/lc_0417_pacific_atlantic_water_flow_compact.py
python 11_graphs/lc_0207_course_schedule_compact.py
python 11_graphs/lc_0261_graph_valid_tree_compact.py
python 11_graphs/lc_0323_number_of_connected_components_in_an_undirected_graph_compact.py

# 2. Run verified reference solutions
python 11_graphs/lc_0200_number_of_islands_solution.py
python 11_graphs/lc_0133_clone_graph_solution.py
python 11_graphs/lc_0417_pacific_atlantic_water_flow_solution.py
python 11_graphs/lc_0207_course_schedule_solution.py
python 11_graphs/lc_0261_graph_valid_tree_solution.py
python 11_graphs/lc_0323_number_of_connected_components_in_an_undirected_graph_solution.py
```

---

## 📚 Deep-Dive Documentation
- **Theoretical Foundations**: [`docs/summary/module_11_graphs.md`](../docs/summary/module_11_graphs.md)
- **Interview Traps & Clarifications**: [`docs/clarifications/module_11_graphs.md`](../docs/clarifications/module_11_graphs.md)
