# Module 05 Clarifications & Pitfalls: Binary Search

This document highlights critical interview traps, boundary conditions, and subtle pointer bugs for Module 05.

---

### Q1: In LC 153, why do we compare `nums[mid]` against `nums[right]` and NOT `nums[left]`?
* **The Pitfall**: Comparing `nums[mid]` to `nums[left]` fails when the array is **already fully sorted** (rotated by $n$ or 0 times, e.g. `[1, 2, 3, 4, 5]`).
  * If `nums = [1, 2, 3, 4, 5]`, `nums[left] = 1` and `nums[mid] = 3`.
  * If you assume `nums[mid] > nums[left]` means "inflection point is to the right", you will set `left = mid + 1` and eliminate the true minimum `1`!
* **The Invariant**: Comparing `nums[mid]` to `nums[right]` works universally:
  * In a fully sorted array (`[1, 2, 3, 4, 5]`), `nums[mid] < nums[right]` ($3 < 5$), correctly driving `right = mid` toward index 0.
  * In a rotated array (`[3, 4, 5, 1, 2]`), `nums[mid] > nums[right]` ($5 > 2$), correctly driving `left = mid + 1` toward the right half.

---

### Q2: Why is the loop condition `left < right` in LC 153, but `left <= right` in LC 33?
* **LC 153 (Convergent Search for an Element)**:
  * We are guaranteed that the minimum element exists within the array.
  * When `nums[mid] <= nums[right]`, `mid` itself could be the answer, so we shrink to `right = mid` (not `mid - 1`).
  * Using `while left < right:` guarantees termination at `left == right`, pointing precisely at the minimum. (Using `left <= right` with `right = mid` would cause an infinite loop).
* **LC 33 (Exact Value Search with Potential Absence)**:
  * Target might not exist in the array (returning -1).
  * We check `nums[mid] == target` at every step, and shrink both boundaries strictly past `mid` (`mid - 1` or `mid + 1`).
  * `while left <= right:` allows examining single-element windows $[left, left]$ before declaring the target absent.

---

### Q3: What happens if the array contains duplicate elements? (LC 81 / LC 154)
* When duplicates are present (e.g. `nums = [1, 0, 1, 1, 1]` or `[1, 1, 1, 0, 1]`):
  * It is possible that `nums[left] == nums[mid] == nums[right]`.
  * In this scenario, it is mathematically impossible to determine which half contains the pivot in $\mathcal{O}(1)$ time.
  * The algorithm must fall back to linear decrement (`right -= 1` or `left += 1`), degrading worst-case complexity to $\mathcal{O}(n)$.
  * In Blind 75 (LC 153 & LC 33), all elements are explicitly guaranteed to be **unique**, preserving strict $\mathcal{O}(\log n)$ runtime.
