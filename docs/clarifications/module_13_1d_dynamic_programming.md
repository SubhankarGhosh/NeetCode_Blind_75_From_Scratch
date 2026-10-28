# Module 13 Clarifications & Pitfalls: 1-D Dynamic Programming

This document details subtle edge cases, initialization traps, greedy fallacies, and space-optimization gotchas for Module 13.

---

### Q1: The Zero Digit Traps in Decode Ways (LC 91)
* **The Rules**:
  * Letter encodings range from `'1'` (`'A'`) to `'26'` (`'Z'`).
  * `'0'` by itself is **invalid** (there is no letter corresponding to `'0'`).
  * Leading zero (e.g., `"0"`, `"06"`) immediately yields 0 ways.
* **The Pitfall**: Failing to differentiate between valid zeros (`"10"`, `"20"`) and invalid zeros (`"30"`, `"70"`, `"00"`).
* **The Structure**:
  ```python
  curr = 0
  if s[i - 1] != "0":
      curr += prev1  # Single digit decode
  if 10 <= int(s[i - 2:i]) <= 26:
      curr += prev2  # Two digit decode
  ```
  If both conditions fail (e.g. at the second `'0'` in `"100"`), `curr` becomes 0 and propagates, correctly collapsing remaining branch counts to 0.

---

### Q2: The Single-Element Boundary Trap in House Robber II (LC 213)
* **The Bug**: Directly running `max(rob(nums[1:]), rob(nums[:-1]))` on a single-element list `nums = [5]`.
* **Why it breaks**:
  * `nums[1:]` is `[]`, yielding `rob([]) = 0`.
  * `nums[:-1]` is `[]`, yielding `rob([]) = 0`.
  * The algorithm would return `max(0, 0) = 0` instead of the correct answer `5`.
* **The Rule**: Always handle the base case `if len(nums) == 1: return nums[0]` before applying the two-slice decomposition.

---

### Q3: Why Greedy Fails in Coin Change (LC 322)
* **The Intuition**: Always pick the largest coin denomination that fits within the remaining amount.
* **Counterexample**:
  * `coins = [1, 3, 4]`, `amount = 6`
  * Greedy selection:
    1. Pick `4` (remaining: 2)
    2. Pick `1` (remaining: 1)
    3. Pick `1` (remaining: 0)
    * Total coins: $3$ (`4 + 1 + 1`)
  * Dynamic Programming optimal selection:
    * Pick `3 + 3 = 6`
    * Total coins: $2$ (`3 + 3`)
* **Conclusion**: Coin Change does not satisfy the greedy-choice property for arbitrary coin systems; DP is strictly required.

---

### Q4: Maximum Product Subarray: All-Negative Arrays and Zeros (LC 152)
* **Trap 1: Initializing `res = 0`**:
  * If the input is `nums = [-2]`, initializing `res = 0` incorrectly returns 0 instead of `-2`.
  * Rule: Always initialize `res = max(nums)` so that single negative elements or all-negative arrays are respected.
* **Trap 2: Multiplying In-Place without Temporary Buffer**:
  ```python
  # BUG:
  cur_max = max(n, n * cur_max, n * cur_min)
  cur_min = min(n, n * cur_max, n * cur_min)  # Uses ALREADY MUTATED cur_max!
  ```
  * Mutating `cur_max` first taints the calculation of `cur_min`.
  * Fix: Save `tmp = cur_max * n` before updating `cur_max`.

---

### Q5: Choosing the Sentinel in Unbounded Knapsack (LC 322)
* Rather than `float('inf')` (which incurs floating-point conversions and comparisons), use `amount + 1`:
  ```python
  dp = [amount + 1] * (amount + 1)
  dp[0] = 0
  ```
* Because the smallest coin denomination is at least 1, the maximum possible number of coins needed for any amount $A$ is $A$ (using all 1-unit coins).
* Therefore, `amount + 1` is an unreachable upper bound that stays within standard integer arithmetic without risk of overflow.
