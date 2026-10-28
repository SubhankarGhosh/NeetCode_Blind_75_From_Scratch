# Module 18: Bit Manipulation

Mastering bitwise operators ($\text{AND } \&, \text{OR } |, \text{XOR } \oplus, \text{NOT } \sim, \text{SHIFTS } \ll, \gg$), Brian Kernighan's lowest-set-bit elimination ($n \& (n - 1)$), XOR cancellation properties, 32-bit register reversal, and bitwise DP transitions across 5 foundational LeetCode problems.

---

## 📋 Problem Map

| Problem | Difficulty | Key Paradigm | Time | Space | Status |
| :--- | :---: | :--- | :---: | :---: | :---: |
| [136. Single Number](https://leetcode.com/problems/single-number/) | Easy | Bitwise XOR Annihilation ($x \oplus x = 0$) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | Easy | Brian Kernighan's Algorithm ($n \& (n - 1)$) | $\mathcal{O}(K)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [338. Counting Bits](https://leetcode.com/problems/counting-bits/) | Easy | Right-Shift Bit DP ($\text{dp}[i] = \text{dp}[i \gg 1] + (i \& 1)$) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [268. Missing Number](https://leetcode.com/problems/missing-number/) | Easy | Double Sequence XOR Cancellation | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/) | Easy | 32-Bit Coordinate Shift & Mask Mirroring | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | 🟢 Complete |

---

## 🏃 Execution Instructions

Run exercises standalone with zero third-party dependencies:

```powershell
# Set UTF-8 encoding in PowerShell
$env:PYTHONIOENCODING = "utf-8"

# 1. Practice with compact exercises (fill TODOs)
python 18_bit_manipulation/lc_0136_single_number_compact.py
python 18_bit_manipulation/lc_0191_number_of_1_bits_compact.py
python 18_bit_manipulation/lc_0338_counting_bits_compact.py
python 18_bit_manipulation/lc_0268_missing_number_compact.py
python 18_bit_manipulation/lc_0190_reverse_bits_compact.py

# 2. Run verified reference solutions
python 18_bit_manipulation/lc_0136_single_number_solution.py
python 18_bit_manipulation/lc_0191_number_of_1_bits_solution.py
python 18_bit_manipulation/lc_0338_counting_bits_solution.py
python 18_bit_manipulation/lc_0268_missing_number_solution.py
python 18_bit_manipulation/lc_0190_reverse_bits_solution.py
```

---

## 📚 Deep-Dive Documentation
- **Theoretical Foundations**: [`docs/summary/module_18_bit_manipulation.md`](../docs/summary/module_18_bit_manipulation.md)
- **Interview Traps & Clarifications**: [`docs/clarifications/module_18_bit_manipulation.md`](../docs/clarifications/module_18_bit_manipulation.md)
