# Module 16 Clarifications & Pitfalls: Intervals

This document details subtle endpoint boundary conventions, sorting key criteria, and sweep-line decoupling invariants for Module 16.

---

### Q1: The Touching Boundary Convention ($\le$ vs. $<$)
* Different problems handle touching endpoints ($[1, 4]$ and $[4, 5]$) differently:
  * **Merge Intervals (LC 56)**: Touching endpoints are considered **overlapping**.
    $$\text{Condition: } \text{curr\_start} \le \text{last\_end} \implies \text{Merged into } [1, 5]$$
  * **Non-overlapping Intervals (LC 435)**: Touching endpoints are considered **compatible**.
    $$\text{Condition: } \text{start} \ge \text{prev\_end} \implies \text{No conflict; accepted without removal}$$
  * **Meeting Rooms (LC 252 & LC 253)**: A meeting ending at 10:00 AM vacates the room in time for a meeting starting at 10:00 AM.
    $$\text{Condition: } \text{starts}[s] < \text{ends}[e] \implies \text{Strictly less than triggers new room}$$
* **Rule**: Always clarify whether endpoint equality constitutes collision before writing comparison operators!

---

### Q2: When to Sort by Start Time vs. End Time
* **Sorting by Start Time (`key=lambda x: x[0]`)**:
  * Mandatory for **Merge Intervals** (LC 56) and **Meeting Rooms I** (LC 252).
  * Why: By ordering intervals chronologically by when they begin, any future interval that can possibly overlap with the current merged cluster must start before the current cluster ends.
* **Sorting by End Time (`key=lambda x: x[1]`)**:
  * Standard for **Earliest Deadline First (EDF) Scheduling** (LC 435).
  * Why: To minimize removals, we want to maximize non-conflicting intervals. Finishing earlier guarantees leaving the maximum remaining time buffer for future candidates.

---

### Q3: Why can Starts and Ends be Decoupled in Meeting Rooms II? (LC 253)
* **The Suspicion**: *"If we sort starts and ends independently, we lose track of which meeting belongs to which start and end!"*
* **The Resolution**:
  * Conference rooms are completely fungible (interchangeable).
  * We do not need to know *which* specific meeting ended in room 1; we only need to know that *a* meeting ended, meaning room count decreases by 1.
  * Every meeting that starts must eventually end. Sorting both arrays chronologically simulates a continuous time axis where start events increment active room demand and end events decrement active room demand.

---

### Q4: Min-Heap vs. Two-Pointer Sweep in Meeting Rooms II
* **Min-Heap Approach**:
  ```python
  heap = []  # stores end times
  for start, end in sorted(intervals):
      if heap and heap[0] <= start:
          heapq.heappop(heap)
      heapq.heappush(heap, end)
  return len(heap)
  ```
  * Complexity: $\mathcal{O}(N \log N)$ time, $\mathcal{O}(N)$ space.
  * Incurs log-time heap percolation on every element.
* **Two-Pointer Chronological Sweep**:
  * Complexity: $\mathcal{O}(N \log N)$ time, $\mathcal{O}(N)$ space.
  * Avoids heap pointer chasing and node allocations; operates over contiguous CPU cache lines, making it substantially faster in practice.
