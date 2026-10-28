# Module 03 Clarifications & Pitfalls: Sliding Window

This document outlines common interview traps, boundary edge cases, and algorithmic nuances for Module 03.

---

### Q1: In LC 3, why does `last_seen[c] >= left` matter?
* **The Pitfall**: Failing to verify that the duplicate character lies *inside* the current window.
* **Example**: `s = "abba"`
  1. $R = 0, 'a' \to \text{last\_seen}['a'] = 0$, window = "a"
  2. $R = 1, 'b' \to \text{last\_seen}['b'] = 1$, window = "ab"
  3. $R = 2, 'b' \to$ duplicate! Jump $L = 1 + 1 = 2$. Window = "b"
  4. $R = 3, 'a' \to$ 'a' exists in `last_seen` at index 0.
     * If you blindly set $L = \text{last\_seen}['a'] + 1 = 1$, you will move $L$ **backwards** from 2 to 1!
     * Checking `last_seen[c] >= left` ensures $L$ only moves forward monotonically.

---

### Q2: In LC 424, does an outdated `max_f` produce invalid windows?
* **Question**: If we remove characters from the left, doesn't `max_f` become temporarily too large?
* **Resolution**: An outdated (overestimated) `max_f` might cause an invalidly small window to not shrink immediately, but it can **never** cause the algorithm to record a false maximum window length!
  * Since we only record window lengths when $(R - L + 1) > \text{max\_len}$, and $\text{max\_len} = \text{max\_f} + k$, we can only beat the record if a genuine character cluster with count $> \text{max\_f}$ appears in the future.
  * This avoids recomputing the maximum over 26 characters on every shrink step.

---

### Q3: In LC 76, why use `have` and `need` instead of checking dictionary equality?
* **The Trap**: Checking `all(window[c] >= count_t[c] for c in count_t)` inside the sliding loop takes $\mathcal{O}(|\Sigma|)$ time at every step. Over $n$ characters, total runtime degrades to $\mathcal{O}(n \cdot |\Sigma|)$.
* **The Solution**: With `have` and `need`:
  * `have` increments *only* when `window[c] == count_t[c]`.
  * `have` decrements *only* when `window[c] < count_t[c]`.
  * The check `have == need` takes $\mathcal{O}(1)$ time, guaranteeing an optimal $\mathcal{O}(n + m)$ runtime regardless of alphabet size.

---

### Q4: Fixed vs. Dynamic Sliding Windows
* **Fixed-Size Window**: The window length $K$ is invariant (e.g. Moving Average, Maximum Sum Subarray of size $K$). $L$ and $R$ advance together with a constant gap.
* **Dynamic-Size Window**: $L$ and $R$ expand and contract independently based on state constraints (e.g., LC 3, LC 424, LC 76).
