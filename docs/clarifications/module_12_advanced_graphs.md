# Module 12 Clarifications & Pitfalls: Advanced Graphs

This document details critical edge-case pitfalls, graph construction gotchas, and prefix ordering traps for Module 12 (Alien Dictionary).

---

### Q1: The Classic Prefix Trap (`["abc", "ab"]`)
* **The Scenario**: Word $W_1 = \text{"abc"}$ appears immediately before word $W_2 = \text{"ab"}$.
* **The Logic Error**: If your loop only checks `w1[j] != w2[j]`, the loop terminates after 2 characters without detecting any character discrepancy because `"ab" == "ab"`.
* **The Rule**: In standard lexicography, `"ab"` must precede `"abc"`. Having `"abc"` appear before `"ab"` is an invalid input dictionary!
  ```python
  if len(w1) > len(w2) and w1.startswith(w2):
      return ""  # Invalid ordering!
  ```
* Missing this check is the #1 reason candidates fail hidden test cases on LeetCode/interviews.

---

### Q2: Why MUST you `break` after the first character discrepancy?
* **The Scenario**: Comparing `"wrt"` and `"wrf"`.
  * Index 0: `'w' == 'w'`
  * Index 1: `'r' == 'r'`
  * Index 2: `'t' != 'f'` $\implies$ Edge: `'t' \longrightarrow 'f'`.
* **The Trap**: What if you do **not** break and keep comparing subsequent characters in longer words like `"za"` and `"zb"` vs `"aa"` and `"bb"`?
* In a dictionary, once the first difference is found (e.g., `'a'` before `'b'`), the ordering of the remaining letters in those two words is completely arbitrary and does **not** reflect their alphabet precedence!
* If you add edges for subsequent letters, you inject false dependencies into the graph that can create false cycles or corrupted topological orders.

---

### Q3: Why use `Set[str]` instead of `List[str]` for Adjacency Lists?
* **The Duplicate Edge Bug**:
  Suppose words contain:
  ```python
  words = ["aba", "abb", "abc"]
  ```
  * `"aba"` vs `"abb"` gives: `'a' \longrightarrow 'b'`.
  * If another pair later also suggests `'a' \longrightarrow 'b'`, appending to a list would register duplicate outgoing edges: `adj['a'] = ['b', 'b']`.
  * If you increment `in_degrees['b']` each time, `'b'` will receive an in-degree of 2 even though it only has 1 unique dependency!
  * As a result, when `'a'` is popped from the queue, `in_degrees['b']` drops to 1 and never reaches 0, falsely flagging a cycle and returning `""`.
* **The Rule**: Always use a `set` for neighbor tracking:
  ```python
  if c2 not in adj[c1]:
      adj[c1].add(c2)
      in_degrees[c2] += 1
  ```

---

### Q4: Isolated Letters with Zero Edges
* **The Scenario**: `words = ["z", "x", "z"]` vs `words = ["zy", "zx"]`.
  * In `["zy", "zx"]`, comparing adjacent words gives `'y' \longrightarrow 'x'`.
  * Letter `'z'` appears in the vocabulary, but participates in no edges (`in_degree['z'] == 0`, `adj['z'] == set()`).
* **The Rule**: Every unique character in `words` must be included in the alphabet output.
  * Initializing `in_degrees = {c: 0 for w in words for c in w}` ensures that isolated characters are immediately placed into the BFS queue with in-degree 0 and successfully output in the final string.

---

### Q5: Multiple Valid Topological Orderings
* **Observation**: If several letters have in-degree 0 simultaneously, any order among them is valid according to the dictionary.
* For example, given `["z", "x"]`, valid outputs include `"zx"`. Given `["z", "x", "a"]` where `'z' < 'x'` and `'x' < 'a'`, only `"zxa"` is valid. But if there are disconnected components, e.g. `['z' -> 'x']` and `['a' -> 'b']`, `"zxab"`, `"azxb"`, `"abzx"` are all valid topological orderings.
* The test harness handles this by validating that all pairwise dictionary constraints and character set preservation are strictly satisfied.
