# Module 15 Clarifications & Pitfalls: Greedy

This document details subtle boundary conditions, initialization bugs, and greedy invariants for Module 15.

---

### Q1: The All-Negative Array Trap in Maximum Subarray (LC 53)
* **The Bug**: Initializing `max_sum = 0` or resetting `cur_sum = 0` before checking `max_sum`:
  ```python
  # DANGEROUS:
  max_sum = 0  # What if nums = [-2, -1]? Returns 0 instead of -1!
  ```
* **The Specification**: The problem specifies a **contiguous non-empty subarray**.
  * If all elements in `nums` are negative (e.g., `[-5, -2, -8, -1]`), the maximum subarray must contain at least one element (here, `-1`).
* **The Safe Formulation**:
  ```python
  max_sum = nums[0]
  cur_sum = 0

  for n in nums:
      if cur_sum < 0:
          cur_sum = 0
      cur_sum += n
      max_sum = max(max_sum, cur_sum)
  ```
  Initializing `max_sum = nums[0]` guarantees that any negative maximum element is recorded.

---

### Q2: Order of Operations in Kadane's Accumulator
* Consider two orderings:
  * **Option A (Reset then Accumulate)**:
    ```python
    if cur_sum < 0:
        cur_sum = 0
    cur_sum += n
    max_sum = max(max_sum, cur_sum)
    ```
  * **Option B (Accumulate then Reset)**:
    ```python
    cur_sum += n
    max_sum = max(max_sum, cur_sum)
    if cur_sum < 0:
        cur_sum = 0
    ```
* Both are mathematically equivalent as long as `max_sum` is initialized to `nums[0]`.
* In Option A, `cur_sum` is reset to 0 *before* adding `n`, so `cur_sum` becomes `n`.
* In Option B, `cur_sum` adds `n`, updates `max_sum`, and is then reset to 0 if negative.

---

### Q3: Single-Element Boundary in Jump Game (LC 55)
* **The Scenario**: `nums = [0]`.
* **The Question**: Is index 0 reachable?
  * Yes! The robot starts at index 0, which *is* the last index. Zero jumps are required.
* **Why Backward Loop Handles It**:
  ```python
  goal = len(nums) - 1  # 0
  for i in range(len(nums) - 2, -1, -1):  # range(-1, -1, -1) -> empty loop
      ...
  return goal == 0  # 0 == 0 -> True!
  ```
  The loop correctly does 0 iterations and immediately returns `True`.

---

### Q4: Forward vs. Backward Greedy in Jump Game
* **Backward Approach**:
  * Clean, minimal logic: only checks `i + nums[i] >= goal`.
  * Very easy to defend and explain in an interview using the inductive goal relaxation proof.
* **Forward Approach**:
  * Tracks `max_reach`: `max_reach = max(max_reach, i + nums[i])`.
  * Early exit: if `max_reach >= len(nums) - 1`, can terminate early before traversing the rest of the array.
  * Both approaches achieve optimal $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.
