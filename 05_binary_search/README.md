# Module 05: Binary Search

Mastering logarithmic search space reduction, rotation inflection point localization, and sorted-half partitioning across 2 foundational LeetCode problems.

---

## 📋 Problem Map

| Problem | Difficulty | Key Paradigm | Time | Space | Status |
| :--- | :---: | :--- | :---: | :---: | :---: |
| [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | Rotation Inflection Search (`nums[mid] > nums[right]`) | $\mathcal{O}(\log n)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | Sorted-Half Detection & Interval Containment | $\mathcal{O}(\log n)$ | $\mathcal{O}(1)$ | 🟢 Complete |

---

## 🏃 Execution Instructions

Run exercises standalone with zero third-party dependencies:

```powershell
# Set UTF-8 encoding in PowerShell
$env:PYTHONIOENCODING = "utf-8"

# 1. Practice with compact exercises (fill TODOs)
python 05_binary_search/lc_0153_find_minimum_in_rotated_sorted_array_compact.py
python 05_binary_search/lc_0033_search_in_rotated_sorted_array_compact.py

# 2. Run verified reference solutions
python 05_binary_search/lc_0153_find_minimum_in_rotated_sorted_array_solution.py
python 05_binary_search/lc_0033_search_in_rotated_sorted_array_solution.py
```

---

## 📚 Deep-Dive Documentation
- **Theoretical Foundations**: [`docs/summary/module_05_binary_search.md`](../docs/summary/module_05_binary_search.md)
- **Interview Traps & Clarifications**: [`docs/clarifications/module_05_clarifications.md`](../docs/clarifications/module_05_clarifications.md)
