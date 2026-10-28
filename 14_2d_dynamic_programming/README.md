# Module 14: 2-D Dynamic Programming

Mastering two-dimensional grid path counting, coordinate DP state transitions, sequence alignment, longest common subsequence (LCS) matrix formulations, and $\mathcal{O}(M \cdot N) \to \mathcal{O}(\min(M, N))$ space-optimization techniques across 2 foundational LeetCode problems.

---

## 📋 Problem Map

| Problem | Difficulty | Key Paradigm | Time | Space | Status |
| :--- | :---: | :--- | :---: | :---: | :---: |
| [62. Unique Paths](https://leetcode.com/problems/unique-paths/) | Medium | 2D Grid Path Summation / 1D Row Space Optimization | $\mathcal{O}(M \cdot N)$ | $\mathcal{O}(\min(M, N))$ | 🟢 Complete |
| [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Medium | 2D String Alignment Table / Suffix Matching DP | $\mathcal{O}(M \cdot N)$ | $\mathcal{O}(\min(M, N))$ | 🟢 Complete |

---

## 🏃 Execution Instructions

Run exercises standalone with zero third-party dependencies:

```powershell
# Set UTF-8 encoding in PowerShell
$env:PYTHONIOENCODING = "utf-8"

# 1. Practice with compact exercises (fill TODOs)
python 14_2d_dynamic_programming/lc_0062_unique_paths_compact.py
python 14_2d_dynamic_programming/lc_1143_longest_common_subsequence_compact.py

# 2. Run verified reference solutions
python 14_2d_dynamic_programming/lc_0062_unique_paths_solution.py
python 14_2d_dynamic_programming/lc_1143_longest_common_subsequence_solution.py
```

---

## 📚 Deep-Dive Documentation
- **Theoretical Foundations**: [`docs/summary/module_14_2d_dynamic_programming.md`](../docs/summary/module_14_2d_dynamic_programming.md)
- **Interview Traps & Clarifications**: [`docs/clarifications/module_14_2d_dynamic_programming.md`](../docs/clarifications/module_14_2d_dynamic_programming.md)
