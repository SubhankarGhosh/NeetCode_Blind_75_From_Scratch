# Agent Operating Manual & Background Context

> **Repository**: `NeetCode_Blind_75_From_Scratch`  
> **Root Directory**: `D:\GIT\NeetCode_Blind_75_From_Scratch`  
> **Target Scope**: NeetCode Blind 75 Algorithms & Data Structures Mastery from First Principles  
> **Python Version**: Python 3.11+ / 3.12+ / 3.13  

---

## 1. Project Mission & Pedagogical Framework

The mission of this repository is to systematically master the **NeetCode Blind 75** algorithm patterns from first principles. By deconstructing every core problem into its structural invariant, mathematical justification, and optimal implementation, we build mental agility for technical interviews.

### The Compact Practice Framework
Following the proven architecture from the `_From_Scratch` curriculum:
1. **Dual-Script Per-Problem Structure**:
   - `lc_XXXX_<slug>_compact.py`: Guided active-learning script with granular `TODO = None` placeholders, algorithmic step-by-step hints, time/space complexity contract, and a self-contained offline test harness.
   - `lc_XXXX_<slug>_solution.py`: Production-grade, verified reference solution with 100% test pass rate for self-checking and review.
2. **Comprehensive Theory & Pattern Summaries**:
   - `docs/summary/module_XX_<topic>.md`: Deep dive into core algorithmic paradigms (e.g., hash maps, two pointers, sliding window invariants, monotonic stacks, tree DFS/BFS, topological sort, memoization vs. tabulation).
3. **Clarifications & Pitfalls Documentation**:
   - `docs/clarifications/module_XX_clarifications.md`: Common interview pitfalls, off-by-one errors, boundary conditions, recursion stack limits, and alternative optimal trade-offs.
4. **Offline Test Verification**:
   - Zero external dependencies beyond the Python Standard Library (`collections`, `heapq`, `math`, `typing`).
   - Every script is directly executable via `python <path_to_script>.py`.

---

## 2. Curriculum & Module Map (18 Pattern Categories / 75 Problems)

| Module | Category | Problem Count | Key Focus |
| :---: | :--- | :---: | :--- |
| **01** | `01_arrays_and_hashing` | 8 | Hash maps, frequency buckets, prefix products, prefix sets |
| **02** | `02_two_pointers` | 3 | Inward converging pointers, symmetry checking, triplet reduction |
| **03** | `03_sliding_window` | 4 | Dynamic/fixed window sizing, frequency maps, window invariants |
| **04** | `04_stack` | 1 | LIFO matching, monotonic property, matching delimiters |
| **05** | `05_binary_search` | 2 | Rotated array inflection points, sorted half detection |
| **06** | `06_linked_list` | 6 | Pointer mutation, dummy heads, fast & slow pointers, k-way merging |
| **07** | `07_trees` | 11 | DFS traversals, BFS level order, BST properties, tree serialization |
| **08** | `08_tries` | 3 | Prefix trees, wildcard backtracking search, matrix trie pruning |
| **09** | `09_heap_priority_queue` | 1 | Two-heap median stream tracking |
| **10** | `10_backtracking` | 2 | Decision trees, state pruning, grid-based path backtracking |
| **11** | `11_graphs` | 6 | BFS/DFS grid traversal, cycle detection, topological sort, union-find |
| **12** | `12_advanced_graphs` | 1 | Directed acyclic graph ordering (Alien Dictionary) |
| **13** | `13_1d_dynamic_programming` | 10 | State transitions, recurrence relations, unbounded knapsack, prefix DP |
| **14** | `14_2d_dynamic_programming` | 2 | Grid DP pathing, 2D string alignment / LCS matrix |
| **15** | `15_greedy` | 2 | Kadane's algorithm, reachable index frontiers |
| **16** | `16_intervals` | 5 | Boundary sorting, merge overlaps, sweep-line room allocation |
| **17** | `17_math_and_geometry` | 3 | In-place matrix rotations, spiral traversal, in-place marker flags |
| **18** | `18_bit_manipulation` | 5 | Bitmask arithmetic, bitwise XOR, bit shifts, two's complement |

---

## 3. Directory Layout

```text
NeetCode_Blind_75_From_Scratch/
├── .gitignore
├── README.md                                          # Curriculum overview and execution instructions
├── gemini.md                                          # Agent operating manual (Gemini mirror)
├── agents.md                                          # Mirror operating manual for agent pairs
├── run_all_modules.py                                 # Automated master test runner
├── docs/
│   ├── summary/                                       # Theory, pattern blueprints, algorithmic templates
│   │   ├── module_01_arrays_and_hashing.md
│   │   └── ...
│   └── clarifications/                                # Pitfalls, edge cases, interview trade-offs
│       ├── module_01_clarifications.md
│       └── ...
├── 01_arrays_and_hashing/                             # Module 01
│   ├── README.md
│   ├── lc_0217_contains_duplicate_compact.py
│   ├── lc_0217_contains_duplicate_solution.py
│   └── ...
└── ...
```

---

## 4. Coding Conventions & Standards

- **Complexity Documentation**: Every function docstring must explicitly declare **Time Complexity** and **Space Complexity** using formal Big-O notation.
- **Type Annotations**: Use strict standard library type hints (`List[int]`, `Optional[ListNode]`, `Dict[str, List[str]]`).
- **Data Structure Definitions**: For custom structures (e.g., `ListNode`, `TreeNode`), define standard LeetCode class implementations with helper converters (e.g., list-to-linked-list, list-to-tree) in the offline test harness.
- **Encoding**: Ensure UTF-8 output encoding in PowerShell: `$env:PYTHONIOENCODING = "utf-8"`.
