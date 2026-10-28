# Module 02 Clarifications & Pitfalls: Two Pointers

This document highlights critical interview traps, boundary conditions, and subtle pointer bugs for Module 02.

---

### Q1: In LC 125, why not just use `s = [c.lower() for c in s if c.isalnum()]` and `s == s[::-1]`?
* **Pros**: In Python, this is concise and runs fast in practice due to C-level iteration.
* **Interview Trap**: Creating `[c.lower() for c in s if c.isalnum()]` allocates an auxiliary list of size $\mathcal{O}(n)$, and slicing `s[::-1]` creates a second copy of size $\mathcal{O}(n)$.
* **Strict Interview Requirement**: FAANG interviewers specifically test whether you can manipulate indices in-place without auxiliary memory. The two-pointer solution guarantees $\mathcal{O}(1)$ auxiliary space regardless of input scale (e.g. multi-gigabyte text streams).

---

### Q2: In LC 15 (3Sum), why do we only skip duplicates on `left` and not also on `right` explicitly?
* **Observation**: In our implementation, upon finding a valid triplet, we do:
  ```python
  left += 1
  right -= 1
  while left < right and nums[left] == nums[left - 1]:
      left += 1
  ```
* **Why this is sufficient**:
  * Because $nums$ is sorted and the target $T = -(nums[i])$ is fixed, each unique $nums[left]$ can only pair with one unique $nums[right]$ value.
  * Skipping duplicate values on `left` automatically prevents duplicate triplets from ever being recorded.
  * On subsequent iterations, if `three_sum_val > 0`, `right` will naturally decrement past any redundant values. (Explicitly skipping duplicate `right` values is also correct, but technically redundant).

---

### Q3: What if $h_L == h_R$ in LC 11 (Container With Most Water)?
* **Question**: If both boundaries have equal height ($h_L = h_R$), which pointer should we advance?
* **Answer**: You can advance **either** pointer (or even both simultaneously)!
  * Proof: Since $h_L = h_R$, any container formed by keeping $L$ and choosing an inner $R' < R$ has height $\le h_L$ and width $< (R - L)$, so its area is strictly smaller.
  * The exact same logic applies to keeping $R$ and choosing an inner $L' > L$.
  * Neither $L$ nor $R$ can ever form a larger container with any inner boundary. Thus, advancing `left += 1`, `right -= 1`, or choosing arbitrarily is mathematically sound and preserves the optimal global maximum.

---

### Q4: When should you NOT use Two Pointers?
* Two pointers (converging from opposite ends) strictly requires **monotonicity**:
  * Either the input array is sorted (e.g., Two Sum II, 3Sum).
  * Or the objective function exhibits monotonic pruning (e.g., Container With Most Water).
* For arbitrary unsorted arrays with negative numbers seeking target sums (without sorting permitted), a **Hash Map** remains necessary.
