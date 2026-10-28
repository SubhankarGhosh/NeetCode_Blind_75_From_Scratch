# NeetCode Blind 75 From Scratch: Algorithms & Data Structures Mastery

An active-learning, test-driven curriculum designed to master the **Blind 75** algorithm patterns from first principles—grounded in rigorous complexity bounds and zero external dependencies.

---

## 🗺️ Curriculum Structure & Pattern Map

| Module | Category | Problem Count | Key Algorithmic Concepts | Status |
| :---: | :--- | :---: | :--- | :---: |
| **01** | [Arrays & Hashing](01_arrays_and_hashing/) | 8 | Hash tables, frequency counting, prefix products, bucket indexing | 🟢 Complete (8/8) |
| **02** | [Two Pointers](02_two_pointers/) | 3 | Inward converging boundaries, palindromic symmetry, target-sum reduction | 🟢 Complete (3/3) |
| **03** | [Sliding Window](03_sliding_window/) | 4 | Dynamic/fixed windows, frequency state tracking, substring invariants | 🟢 Complete (4/4) |
| **04** | [Stack](04_stack/) | 1 | LIFO parentheses matching, state tracking | ⏳ Queued |
| **05** | [Binary Search](05_binary_search/) | 2 | Rotated sorted arrays, inflection point search, logarithmic boundary reduction | ⏳ Queued |
| **06** | [Linked List](06_linked_list/) | 6 | In-place pointer reversal, fast/slow pointers, dummy node pattern, k-way merging | ⏳ Queued |
| **07** | [Trees](07_trees/) | 11 | Recursive DFS, BFS level-order, BST properties, ancestor search, serialization | ⏳ Queued |
| **08** | [Tries](08_tries/) | 3 | Prefix trees, character map branches, wildcard matching, matrix DFS pruning | ⏳ Queued |
| **09** | [Heap / Priority Queue](09_heap_priority_queue/) | 1 | Min-heap / max-heap dual balancing, dynamic median calculation | ⏳ Queued |
| **10** | [Backtracking](10_backtracking/) | 2 | State tree exploration, candidate pruning, grid search backtracking | ⏳ Queued |
| **11** | [Graphs](11_graphs/) | 6 | Adjacency lists, cycle detection, topological sorting, union-find (disjoint sets) | ⏳ Queued |
| **12** | [Advanced Graphs](12_advanced_graphs/) | 1 | Topological sort with lexicographical dependency constraints (Alien Dictionary) | ⏳ Queued |
| **13** | [1-D Dynamic Programming](13_1d_dynamic_programming/) | 10 | Recurrence formulations, optimal substructure, space-optimized state variables | ⏳ Queued |
| **14** | [2-D Dynamic Programming](14_2d_dynamic_programming/) | 2 | 2D grid pathing, longest common subsequence table transitions | ⏳ Queued |
| **15** | [Greedy](15_greedy/) | 2 | Local optimal choice, Kadane's maximum subarray, reachable index frontiers | ⏳ Queued |
| **16** | [Intervals](16_intervals/) | 5 | Interval merging, non-overlapping scheduling, sweep-line room allocation | ⏳ Queued |
| **17** | [Math & Geometry](17_math_and_geometry/) | 3 | In-place matrix rotations, coordinate boundary stepping, in-place state flags | ⏳ Queued |
| **18** | [Bit Manipulation](18_bit_manipulation/) | 5 | Bitwise XOR cancellation, bit shifts, Hamming weight, 32-bit integer arithmetic | ⏳ Queued |

---

## 🛠️ The Compact Practice Framework

Following the active-learning pedagogy across the `_From_Scratch` curriculum:
* **Guided Practice (`lc_XXXX_<slug>_compact.py`)**:
  Contains problem descriptions, LeetCode URLs, complexity requirements, `TODO = None` active-learning placeholders, algorithmic hints, and self-contained test suites.
* **Reference Solutions (`lc_XXXX_<slug>_solution.py`)**:
  Production-grade reference solutions verified against 100% of test cases with detailed complexity derivations.
* **Theory & Concept Summaries (`docs/summary/`)**:
  Algorithmic blueprints, pattern invariants, and mathematical justifications.
* **Clarifications & Traps (`docs/clarifications/`)**:
  Interview gotchas, off-by-one errors, recursion limits, and trade-off considerations.

### Running Exercises Standalone
Every script runs independently with standard Python (zero pip dependencies):
```powershell
# Set UTF-8 encoding in PowerShell
$env:PYTHONIOENCODING = "utf-8"

# Run a compact practice script
python 01_arrays_and_hashing/lc_0217_contains_duplicate_compact.py

# Run a reference solution
python 01_arrays_and_hashing/lc_0217_contains_duplicate_solution.py

# Run the test suite across all implemented solutions
python run_all_modules.py
```
