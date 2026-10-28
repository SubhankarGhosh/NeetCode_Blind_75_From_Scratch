# Module 03: Sliding Window

Mastering dynamic and fixed window boundaries, running state invariants, frequency map tracking, and substring contraction across 4 foundational LeetCode problems.

---

## 📋 Problem Map

| Problem | Difficulty | Key Paradigm | Time | Space | Status |
| :--- | :---: | :--- | :---: | :---: | :---: |
| [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | Dynamic Buy-Day Reset Sliding Window | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | Last-Seen Index Leaping Window | $\mathcal{O}(n)$ | $\mathcal{O}(\min(n, m))$ | 🟢 Complete |
| [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | Monotonic `max_f` Window Contraction | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard | Dual `have`/`need` Frequency Constraint Window | $\mathcal{O}(n + m)$ | $\mathcal{O}(k)$ | 🟢 Complete |

---

## 🏃 Execution Instructions

Run exercises standalone with zero third-party dependencies:

```powershell
# Set UTF-8 encoding in PowerShell
$env:PYTHONIOENCODING = "utf-8"

# 1. Practice with compact exercises (fill TODOs)
python 03_sliding_window/lc_0121_best_time_to_buy_and_sell_stock_compact.py
python 03_sliding_window/lc_0003_longest_substring_without_repeating_characters_compact.py
python 03_sliding_window/lc_0424_longest_repeating_character_replacement_compact.py
python 03_sliding_window/lc_0076_minimum_window_substring_compact.py

# 2. Run verified reference solutions
python 03_sliding_window/lc_0121_best_time_to_buy_and_sell_stock_solution.py
python 03_sliding_window/lc_0003_longest_substring_without_repeating_characters_solution.py
python 03_sliding_window/lc_0424_longest_repeating_character_replacement_solution.py
python 03_sliding_window/lc_0076_minimum_window_substring_solution.py
```

---

## 📚 Deep-Dive Documentation
- **Theoretical Foundations**: [`docs/summary/module_03_sliding_window.md`](../docs/summary/module_03_sliding_window.md)
- **Interview Traps & Clarifications**: [`docs/clarifications/module_03_clarifications.md`](../docs/clarifications/module_03_clarifications.md)
