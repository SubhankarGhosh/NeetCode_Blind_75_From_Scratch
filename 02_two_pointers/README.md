# Module 02: Two Pointers

Mastering boundary convergence, symmetry validation, triplet search reduction, and greedy volume maximization across 3 foundational LeetCode problems.

---

## 📋 Problem Map

| Problem | Difficulty | Key Paradigm | Time | Space | Status |
| :--- | :---: | :--- | :---: | :---: | :---: |
| [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | In-Place Inward Pointers & Alphanumeric Filter | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [15. 3Sum](https://leetcode.com/problems/3sum/) | Medium | Sorting + Dual Converging Pointers + Deduplication | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)^*$ | 🟢 Complete |
| [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | Greedy Shortest-Wall Elimination | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | 🟢 Complete |

*\* Note: Space complexity excludes output array and internal sort implementation memory.*

---

## 🏃 Execution Instructions

Run exercises standalone with zero third-party dependencies:

```powershell
# Set UTF-8 encoding in PowerShell
$env:PYTHONIOENCODING = "utf-8"

# 1. Practice with compact exercises (fill TODOs)
python 02_two_pointers/lc_0125_valid_palindrome_compact.py
python 02_two_pointers/lc_0015_3sum_compact.py
python 02_two_pointers/lc_0011_container_with_most_water_compact.py

# 2. Run verified reference solutions
python 02_two_pointers/lc_0125_valid_palindrome_solution.py
python 02_two_pointers/lc_0015_3sum_solution.py
python 02_two_pointers/lc_0011_container_with_most_water_solution.py
```

---

## 📚 Deep-Dive Documentation
- **Theoretical Foundations**: [`docs/summary/module_02_two_pointers.md`](../docs/summary/module_02_two_pointers.md)
- **Interview Traps & Clarifications**: [`docs/clarifications/module_02_clarifications.md`](../docs/clarifications/module_02_clarifications.md)
