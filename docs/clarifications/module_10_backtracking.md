# Module 10 Clarifications & Pitfalls: Backtracking

This document highlights critical interview traps, shallow-copy mistakes, and in-place state management techniques for Module 10.

---

### Q1: The Shallow vs. Deep Copy Trap in Backtracking (LC 39)
* **The Classical Bug**: Writing `res.append(cur)` instead of `res.append(cur.copy())` or `res.append(list(cur))`.
* **Why it breaks**: In Python, `cur` is a mutable reference to a list. If you append `cur` directly, `res` will hold references to the *exact same* list object. As the backtrack progresses and executes `cur.pop()`, all elements in `res` will also be mutated, resulting in an array of empty lists `[[], [], []]`.
* **Rule**: Always create a snapshot (`cur.copy()`) when storing successful solutions in global collections.

---

### Q2: Why is In-Place Marking (`board[r][c] = '#'`) superior to a Visited Set? (LC 79)
* **The Visited Set Approach**: Adding `(r, c)` tuples to a `visited = set()`.
  * *Overhead*: Hashing tuples `(r, c)`, dynamically resizing hash buckets, and garbage collecting entries creates substantial overhead inside inner recursive loops.
* **In-Place Mutation**: Temporarily replacing the cell character with a non-alphabetic sentinel:
  ```python
  board[r][c] = "#"
  # Recurse...
  board[r][c] = word[k]
  ```
  * *Zero Memory*: Uses strictly $\mathcal{O}(1)$ auxiliary space and eliminates hash lookups entirely.
  * *Cache Locality*: Directly updates adjacent matrix memory words in L1 CPU cache.

---

### Q3: When should you sort candidates before backtracking?
* In **Combination Sum** (LC 39), sorting `candidates` is optional if using the inclusion/exclusion tree, but sorting allows **early termination**:
  ```python
  candidates.sort()
  # Inside loop:
  if total + candidates[i] > target:
      break  # All subsequent candidates are also > target!
  ```
* In problems with duplicate candidates (e.g. **Combination Sum II / LC 40**), sorting is strictly required to skip duplicates cleanly via `if i > start and candidates[i] == candidates[i - 1]: continue`.
