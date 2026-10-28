# Module 08: Tries

Mastering Prefix Trees (Trie ADT), wildcard regex backtracking, and Trie-guided 2D grid search pruning across 3 foundational LeetCode problems.

---

## 📋 Problem Map

| Problem | Difficulty | Key Paradigm | Time | Space | Status |
| :--- | :---: | :--- | :---: | :---: | :---: |
| [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | Prefix Tree ADT (Insert, Search, StartsWith) | $\mathcal{O}(L)$ | $\mathcal{O}(N \cdot L)$ | 🟢 Complete |
| [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Medium | Trie-Backed Wildcard (`.`) DFS Search | $\mathcal{O}(26^d \cdot L)$ | $\mathcal{O}(N \cdot L)$ | 🟢 Complete |
| [212. Word Search II](https://leetcode.com/problems/word-search-ii/) | Hard | Trie-Guided 2D Grid Backtracking with Node Pruning | $\mathcal{O}(M \cdot N \cdot 4 \cdot 3^{L-1})$ | $\mathcal{O}(\sum \|W\|)$ | 🟢 Complete |

---

## 🏃 Execution Instructions

Run exercises standalone with zero third-party dependencies:

```powershell
# Set UTF-8 encoding in PowerShell
$env:PYTHONIOENCODING = "utf-8"

# 1. Practice with compact exercises (fill TODOs)
python 08_tries/lc_0208_implement_trie_prefix_tree_compact.py
python 08_tries/lc_0211_design_add_and_search_words_data_structure_compact.py
python 08_tries/lc_0212_word_search_ii_compact.py

# 2. Run verified reference solutions
python 08_tries/lc_0208_implement_trie_prefix_tree_solution.py
python 08_tries/lc_0211_design_add_and_search_words_data_structure_solution.py
python 08_tries/lc_0212_word_search_ii_solution.py
```

---

## 📚 Deep-Dive Documentation
- **Theoretical Foundations**: [`docs/summary/module_08_tries.md`](../docs/summary/module_08_tries.md)
- **Interview Traps & Clarifications**: [`docs/clarifications/module_08_tries.md`](../docs/clarifications/module_08_tries.md)
