# Module 15: Greedy

Mastering the greedy-choice property, locally optimal decision making, Kadane's algorithm for maximum subarray prefixes, and forward/backward reachable frontier maintenance across 2 foundational LeetCode problems.

---

## 📋 Problem Map

| Problem | Difficulty | Key Paradigm | Time | Space | Status |
| :--- | :---: | :--- | :---: | :---: | :---: |
| [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Medium | Kadane's Algorithm / Negative Prefix Reset | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [55. Jump Game](https://leetcode.com/problems/jump-game/) | Medium | Backward Goal Shift / Forward Reachable Frontier | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | 🟢 Complete |

---

## 🏃 Execution Instructions

Run exercises standalone with zero third-party dependencies:

```powershell
# Set UTF-8 encoding in PowerShell
$env:PYTHONIOENCODING = "utf-8"

# 1. Practice with compact exercises (fill TODOs)
python 15_greedy/lc_0053_maximum_subarray_compact.py
python 15_greedy/lc_0055_jump_game_compact.py

# 2. Run verified reference solutions
python 15_greedy/lc_0053_maximum_subarray_solution.py
python 15_greedy/lc_0055_jump_game_solution.py
```

---

## 📚 Deep-Dive Documentation
- **Theoretical Foundations**: [`docs/summary/module_15_greedy.md`](../docs/summary/module_15_greedy.md)
- **Interview Traps & Clarifications**: [`docs/clarifications/module_15_greedy.md`](../docs/clarifications/module_15_greedy.md)
