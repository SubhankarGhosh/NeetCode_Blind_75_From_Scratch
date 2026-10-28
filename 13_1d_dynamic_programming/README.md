# Module 13: 1-D Dynamic Programming

Mastering linear state transitions, recurrence relations, space optimization ($\mathcal{O}(N) \to \mathcal{O}(1)$), circular array decomposition, palindrome center expansion, sign-inverting extreme tracking, and unbounded knapsack dynamic programming across 10 foundational LeetCode problems.

---

## 📋 Problem Map

| Problem | Difficulty | Key Paradigm | Time | Space | Status |
| :--- | :---: | :--- | :---: | :---: | :---: |
| [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | Fibonacci Recurrence / Rolling Variables | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | Easy | Cost Prefix Minimization / 2-State Rolling | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [198. House Robber](https://leetcode.com/problems/house-robber/) | Medium | Non-Adjacent Element Selection DP | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [213. House Robber II](https://leetcode.com/problems/house-robber-ii/) | Medium | Circular Array Subproblem Decomposition | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Medium | Dual-Center Expansion ($(i, i)$ and $(i, i+1)$) | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | Medium | Symmetrical Center Counting ($2N - 1$ Centers) | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [91. Decode Ways](https://leetcode.com/problems/decode-ways/) | Medium | 1-Digit & 2-Digit Valid Segment Transitions | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [322. Coin Change](https://leetcode.com/problems/coin-change/) | Medium | Unbounded Knapsack / Shortest Path on DAG | $\mathcal{O}(A \cdot C)$ | $\mathcal{O}(A)$ | 🟢 Complete |
| [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | Medium | Dual Extreme Tracking (`cur_max` & `cur_min`) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [139. Word Break](https://leetcode.com/problems/word-break/) | Medium | Suffix-to-Prefix Boolean Partitioning DP | $\mathcal{O}(N \cdot M \cdot K)$ | $\mathcal{O}(N)$ | 🟢 Complete |

---

## 🏃 Execution Instructions

Run exercises standalone with zero third-party dependencies:

```powershell
# Set UTF-8 encoding in PowerShell
$env:PYTHONIOENCODING = "utf-8"

# 1. Practice with compact exercises (fill TODOs)
python 13_1d_dynamic_programming/lc_0070_climbing_stairs_compact.py
python 13_1d_dynamic_programming/lc_0746_min_cost_climbing_stairs_compact.py
python 13_1d_dynamic_programming/lc_0198_house_robber_compact.py
python 13_1d_dynamic_programming/lc_0213_house_robber_ii_compact.py
python 13_1d_dynamic_programming/lc_0005_longest_palindromic_substring_compact.py
python 13_1d_dynamic_programming/lc_0647_palindromic_substrings_compact.py
python 13_1d_dynamic_programming/lc_0091_decode_ways_compact.py
python 13_1d_dynamic_programming/lc_0322_coin_change_compact.py
python 13_1d_dynamic_programming/lc_0152_maximum_product_subarray_compact.py
python 13_1d_dynamic_programming/lc_0139_word_break_compact.py

# 2. Run verified reference solutions
python 13_1d_dynamic_programming/lc_0070_climbing_stairs_solution.py
python 13_1d_dynamic_programming/lc_0746_min_cost_climbing_stairs_solution.py
python 13_1d_dynamic_programming/lc_0198_house_robber_solution.py
python 13_1d_dynamic_programming/lc_0213_house_robber_ii_solution.py
python 13_1d_dynamic_programming/lc_0005_longest_palindromic_substring_solution.py
python 13_1d_dynamic_programming/lc_0647_palindromic_substrings_solution.py
python 13_1d_dynamic_programming/lc_0091_decode_ways_solution.py
python 13_1d_dynamic_programming/lc_0322_coin_change_solution.py
python 13_1d_dynamic_programming/lc_0152_maximum_product_subarray_solution.py
python 13_1d_dynamic_programming/lc_0139_word_break_solution.py
```

---

## 📚 Deep-Dive Documentation
- **Theoretical Foundations**: [`docs/summary/module_13_1d_dynamic_programming.md`](../docs/summary/module_13_1d_dynamic_programming.md)
- **Interview Traps & Clarifications**: [`docs/clarifications/module_13_1d_dynamic_programming.md`](../docs/clarifications/module_13_1d_dynamic_programming.md)
