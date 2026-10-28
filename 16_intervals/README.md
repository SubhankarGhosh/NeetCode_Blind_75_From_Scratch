# Module 16: Intervals

Mastering interval sorting, boundary overlap detection, greedy interval scheduling (Earliest Deadline First), chronological sweep-line algorithms, and capacity tracking across 5 foundational LeetCode problems.

---

## 📋 Problem Map

| Problem | Difficulty | Key Paradigm | Time | Space | Status |
| :--- | :---: | :--- | :---: | :---: | :---: |
| [57. Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium | 3-Phase Boundary Partitioning / Merge Sweep | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | 🟢 Complete |
| [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | Start-Time Sorting + Monotonic Interval Expansion | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ | 🟢 Complete |
| [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Medium | Earliest Deadline First (EDF) Greedy Scheduling | $\mathcal{O}(N \log N)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) *(LintCode 920)* | Easy | Chronological Adjacent Overlap Verification | $\mathcal{O}(N \log N)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) *(LintCode 919)* | Medium | Chronological Two-Pointer Event Sweep-Line | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ | 🟢 Complete |

---

## 🏃 Execution Instructions

Run exercises standalone with zero third-party dependencies:

```powershell
# Set UTF-8 encoding in PowerShell
$env:PYTHONIOENCODING = "utf-8"

# 1. Practice with compact exercises (fill TODOs)
python 16_intervals/lc_0057_insert_interval_compact.py
python 16_intervals/lc_0056_merge_intervals_compact.py
python 16_intervals/lc_0435_non_overlapping_intervals_compact.py
python 16_intervals/lc_0252_meeting_rooms_compact.py
python 16_intervals/lc_0253_meeting_rooms_ii_compact.py

# 2. Run verified reference solutions
python 16_intervals/lc_0057_insert_interval_solution.py
python 16_intervals/lc_0056_merge_intervals_solution.py
python 16_intervals/lc_0435_non_overlapping_intervals_solution.py
python 16_intervals/lc_0252_meeting_rooms_solution.py
python 16_intervals/lc_0253_meeting_rooms_ii_solution.py
```

---

## 📚 Deep-Dive Documentation
- **Theoretical Foundations**: [`docs/summary/module_16_intervals.md`](../docs/summary/module_16_intervals.md)
- **Interview Traps & Clarifications**: [`docs/clarifications/module_16_intervals.md`](../docs/clarifications/module_16_intervals.md)
