# Module 04 Clarifications & Pitfalls: Stack

This document details common interview traps, boundary conditions, and subtle edge cases for Module 04.

---

### Q1: Why can't we just count brackets with integer counters?
* **The Trap**: If the problem only had one bracket type `()`, an integer counter `balance` would suffice: increment on `(`, decrement on `)`, and reject if `balance < 0`.
* **Why it fails with multiple types**: With multiple bracket types (`()`, `[]`, `{}`), an integer counter fails to capture **nesting order**.
  * Example: `"([)]"` has equal counts of opening and closing brackets of each type, but is invalid because the brackets interleave illegally.
  * A stack is strictly required to enforce that the *most recently opened* bracket is the first to be closed.

---

### Q2: Edge Cases to Test During Technical Interviews
1. **Empty String `""`**: Vacuously true (0 unmatched brackets).
2. **Odd Length Strings**: Any string of odd length cannot be fully paired and can be rejected immediately in $\mathcal{O}(1)$ via `if len(s) % 2 != 0: return False`.
3. **Leading Closing Delimiters `"]"`**: Attempting `stack.pop()` without checking `if not stack:` causes an `IndexError` (stack underflow).
4. **All Opening Delimiters `"((((("**: Forgetting to check `len(stack) == 0` at the end results in returning `True` for unclosed brackets.
5. **Mismatched Types `"(]"`**: Proper mapping lookup ensures closing square does not pair with opening parenthesis.

---

### Q3: Python List vs. `collections.deque` for Stacks
* In Python, a standard list `[]` is implemented as a contiguous dynamic array.
* Appending (`stack.append()`) and popping from the end (`stack.pop()`) are amortized $\mathcal{O}(1)$ operations with zero node-allocation overhead and superior L1 cache locality compared to doubly-linked node implementations like `collections.deque`.
* A standard Python `list` is therefore the preferred, idiomatic data structure for stacks.
