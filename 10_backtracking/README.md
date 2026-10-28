# Module 10: Backtracking

Mastering state space tree generation, recursive decision trees, candidate inclusion/exclusion, grid-based path discovery, and heuristic branch pruning across 2 foundational LeetCode problems.

---

## 📋 Problem Map

| Problem | Difficulty | Key Paradigm | Time | Space | Status |
| :--- | :---: | :--- | :---: | :---: | :---: |
| [39. Combination Sum](https://leetcode.com/problems/combination-sum/) | Medium | Binary Inclusion/Exclusion Tree + State Buffer | $\mathcal{O}(2^{T/M})$ | $\mathcal{O}(T/M)$ | 🟢 Complete |
| [79. Word Search](https://leetcode.com/problems/word-search/) | Medium | In-Place 2D Grid DFS with Frequency Pruning | $\mathcal{O}(M \cdot N \cdot 3^L)$ | $\mathcal{O}(L)$ | 🟢 Complete |

---

## 🏃 Execution Instructions

Run exercises standalone with zero third-party dependencies:

```powershell
# Set UTF-8 encoding in PowerShell
$env:PYTHONIOENCODING = "utf-8"

# 1. Practice with compact exercises (fill TODOs)
python 10_backtracking/lc_0039_combination_sum_compact.py
python 10_backtracking/lc_0079_word_search_compact.py

# 2. Run verified reference solutions
python 10_backtracking/lc_0039_combination_sum_solution.py
python 10_backtracking/lc_0079_word_search_solution.py
```

---

## 📚 Deep-Dive Documentation
- **Theoretical Foundations**: [`docs/summary/module_10_backtracking.md`](../docs/summary/module_10_backtracking.md)
- **Interview Traps & Clarifications**: [`docs/clarifications/module_10_backtracking.md`](../docs/clarifications/module_10_backtracking.md)
