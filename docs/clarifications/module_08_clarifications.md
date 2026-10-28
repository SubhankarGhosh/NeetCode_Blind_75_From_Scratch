# Module 08 Clarifications & Pitfalls: Tries

This document details common interview traps, memory allocation choices, and performance optimizations for Module 08.

---

### Q1: Python Dictionary vs. 26-Element Fixed Array for Trie Children
* **Array Implementation (`children = [None] * 26`)**:
  * *Pros*: Direct integer indexing `ord(c) - ord('a')`, zero hashing overhead.
  * *Cons*: Every single node allocates a 26-element array, leading to substantial memory waste when branching factors are sparse (e.g. deep word branches).
* **Hash Map Implementation (`children = {}`)**:
  * *Pros*: Allocates edges dynamically only for characters that actually appear. Far more memory efficient for sparse prefixes and general non-English / Unicode alphabets.
  * *Interview Standard*: Python dictionaries are highly optimized and idiomatic in modern FAANG interviews.

---

### Q2: Why is Trie Pruning (`parent.children.pop(c)`) critical in LC 212?
* **Problem Without Pruning**:
  * Consider a board filled with `'a'`s (`board = [['a'] * 4 for _ in range(4)]`) and words like `["a", "aa", "aaa", "aaaa"]`.
  * After discovering `"aaaa"`, standard DFS will continue to match and revisit all branches from all 16 cells repeatedly, leading to Time Limit Exceeded (TLE) on LeetCode test cases.
* **With Pruning**:
  * When `"aaaa"` is found, its leaf node has no children and is deleted from its parent.
  * This recursively prunes the branch back to the root, preventing future cell searches from traversing exhausted word paths.

---

### Q3: How to avoid building strings dynamically during DFS in LC 212?
* **Common Trap**: Accumulating characters along the DFS path via `path += board[r][c]` or `"".join(path)` causes $\mathcal{O}(L)$ string copies at every step.
* **The Solution**: Store the full completed string directly on the terminal TrieNode (`node.word = word`) during construction. When `curr_node.word` is encountered during DFS, append it directly to `res` in $\mathcal{O}(1)$ time.
