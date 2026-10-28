# Module 01: Arrays & Hashing

Mastering hash-based lookups, frequency counting, prefix-accumulations, and linear-time bucket sorting across 8 foundational LeetCode problems.

---

## 📋 Problem Map

| Problem | Difficulty | Key Paradigm | Time | Space | Status |
| :--- | :---: | :--- | :---: | :---: | :---: |
| [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | Hash Set Early-Exit | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | 🟢 Complete |
| [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | 26-Element Frequency Table | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [1. Two Sum](https://leetcode.com/problems/two-sum/) | Easy | One-Pass Complement Hash Map | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | 🟢 Complete |
| [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | 26-Tuple Hashable Key | $\mathcal{O}(n \cdot k)$ | $\mathcal{O}(n \cdot k)$ | 🟢 Complete |
| [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | Linear-Time Bucket Sort | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | 🟢 Complete |
| [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | Two-Pass Prefix/Postfix Products | $\mathcal{O}(n)$ | $\mathcal{O}(1)^*$ | 🟢 Complete |
| [271. Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) | Medium | Length-Prefixed Chunking (`len#str`) | $\mathcal{O}(N)$ | $\mathcal{O}(1)^*$ | 🟢 Complete |
| [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | Sequence Head Invariant (`n - 1 \notin S`) | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | 🟢 Complete |

*\* Note: Output array/string does not count toward auxiliary space.*

---

## 🏃 Execution Instructions

Run exercises standalone with zero third-party dependencies:

```powershell
# Set UTF-8 encoding in PowerShell
$env:PYTHONIOENCODING = "utf-8"

# 1. Practice with compact exercises (fill TODOs)
python 01_arrays_and_hashing/lc_0217_contains_duplicate_compact.py
python 01_arrays_and_hashing/lc_0001_two_sum_compact.py

# 2. Run verified reference solutions
python 01_arrays_and_hashing/lc_0217_contains_duplicate_solution.py
python 01_arrays_and_hashing/lc_0001_two_sum_solution.py
python 01_arrays_and_hashing/lc_0347_top_k_frequent_elements_solution.py
python 01_arrays_and_hashing/lc_0238_product_of_array_except_self_solution.py
python 01_arrays_and_hashing/lc_0271_encode_and_decode_strings_solution.py
python 01_arrays_and_hashing/lc_0128_longest_consecutive_sequence_solution.py
```

---

## 📚 Deep-Dive Documentation
- **Theoretical Foundations**: [`docs/summary/module_01_arrays_and_hashing.md`](../docs/summary/module_01_arrays_and_hashing.md)
- **Interview Traps & Clarifications**: [`docs/clarifications/module_01_clarifications.md`](../docs/clarifications/module_01_clarifications.md)
