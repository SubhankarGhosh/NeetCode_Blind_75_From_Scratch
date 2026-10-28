# Module 01 Clarifications & Pitfalls: Arrays & Hashing

This document details common interview traps, boundary conditions, and algorithmic edge cases encountered in Module 01.

---

### Q1: Can we sort instead of using extra space in LC 217?
* **Trade-off**:
  * *Hash Set*: $\mathcal{O}(n)$ Time, $\mathcal{O}(n)$ Space. (Best for time-critical applications).
  * *In-place Sorting*: $\mathcal{O}(n \log n)$ Time, $\mathcal{O}(1)$ or $\mathcal{O}(\log n)$ auxiliary space (depending on quicksort/heapsort vs. Python's Timsort).
* **Interview Gotcha**: In Python, `nums.sort()` mutates the caller's input in-place, which may violate immutability contracts in multi-threaded or production APIs. Clarify with your interviewer whether modifying the input array is permitted.

---

### Q2: Handling Unicode / Large Alphabets in LC 242 (Valid Anagram)
* **ASCII / Lowercase English**: A fixed 26-element array `counts = [0] * 26` provides cache locality and zero hash collision overhead with $\mathcal{O}(1)$ space.
* **Unicode Follow-up**: If inputs include arbitrary UTF-8 characters (e.g. Chinese, emojis), fixed arrays are impractical. Switch to `collections.Counter` or `collections.defaultdict(int)`, yielding $\mathcal{O}(k)$ space where $k$ is the count of distinct Unicode code points.

---

### Q3: Why doesn't Two Sum use Two Pointers here? (LC 1 vs LC 167)
* For an **unsorted** array, Two Pointers requires sorting first ($\mathcal{O}(n \log n)$ time) and loses original indices, requiring storing $(val, original\_index)$ tuples ($\mathcal{O}(n)$ space).
* A one-pass Hash Map achieves optimal $\mathcal{O}(n)$ time directly while preserving original indices without extra overhead. (If the array is already sorted, Two Pointers is superior because it uses $\mathcal{O}(1)$ space).

---

### Q4: LC 238 — What if the array contains zeros?
* *Case 1: No zeros*: Total product divided by $x_i$ works mathematically, but division is explicitly disallowed by the problem statement.
* *Case 2: One zero*: Every element except the zero element evaluates to 0; the zero element evaluates to the product of all non-zero elements.
* *Case 3: Two or more zeros*: Every position evaluates to 0.
* **Prefix/Postfix Advantage**: The two-pass multiplication approach handles all zero configurations natively without special-casing or zero-division exception handling.

---

### Q5: LC 128 — Why isn't the nested while loop $\mathcal{O}(n^2)$?
* **Common Trap**: Candidates see a `while` loop inside a `for` loop and assume quadratic $\mathcal{O}(n^2)$ complexity.
* **Amortized Proof**: The condition `if (n - 1) not in num_set:` ensures the while loop *only runs for numbers that start a sequence*.
  * Example: `nums = [1, 2, 3, 4, 100]`
  * When $n = 2, 3, 4$, $(n-1)$ is in the set, so the while loop is skipped in $\mathcal{O}(1)$.
  * When $n = 1$, the while loop visits $2, 3, 4$ and stops.
  * Every number in `nums` is checked in the `for` loop once ($\mathcal{O}(n)$), and visited inside the `while` loop at most once ($\mathcal{O}(n)$).
  * Total time is strictly bounded by $2n = \mathcal{O}(n)$.
