# Module 16 Summary: Intervals

This document formalizes interval topology, overlap criteria, earliest deadline first (EDF) greedy proofs, and chronological sweep-line algorithms underlying Module 16.

---

## 1. Formal Topology of 1D Intervals

An interval $I = [s, e]$ defines a continuous, closed segment on the real line:
$$\mathcal{I} = \{x \in \mathbb{R} \mid s \le x \le e\}$$

### Overlap Invariant
Two intervals $I_1 = [s_1, e_1]$ and $I_2 = [s_2, e_2]$ intersect ($I_1 \cap I_2 \neq \emptyset$) if and only if:
$$\max(s_1, s_2) \le \min(e_1, e_2)$$
* If the intervals are sorted by start time such that $s_1 \le s_2$, the condition simplifies to:
  $$s_2 \le e_1$$
* When overlap occurs, their convex hull union is a single interval:
  $$I_{\text{merged}} = \big[\min(s_1, s_2), \; \max(e_1, e_2)\big]$$

---

## 2. Invariants & Algorithmic Paradigms

### Pattern 1: Sorted Insertion & Partitioning (LC 57: Insert Interval)
When inserting $I_{\text{new}}$ into a pre-sorted, pairwise-disjoint list $\mathcal{L}$:
1. **Left Disjoint Set**: All $I \in \mathcal{L}$ with $I.e < I_{\text{new}}.s$. These cannot intersect $I_{\text{new}}$ and are appended unchanged.
2. **Intersecting Cluster**: All $I \in \mathcal{L}$ with $I.s \le I_{\text{new}}.e$. Each such interval expands the bounds of $I_{\text{new}}$:
   $$I_{\text{new}}.s \leftarrow \min(I_{\text{new}}.s, I.s), \quad I_{\text{new}}.e \leftarrow \max(I_{\text{new}}.e, I.e)$$
3. **Right Disjoint Set**: All remaining intervals are appended unchanged.
* **Complexity**: $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space without sorting.

### Pattern 2: Start-Time Sorting & Monotonic Merging (LC 56 & LC 252)
* By sorting intervals in $\mathcal{O}(N \log N)$ time by start time ($s_i \le s_{i+1}$):
  * Merging (LC 56): A running interval $I_{\text{last}}$ is extended if $s_{i} \le I_{\text{last}}.e$. Otherwise, $I_{\text{last}}$ is finalized.
  * Conflict Detection (LC 252): If any adjacent pair satisfies $s_{i+1} < e_i$, a conflict exists immediately. Transitivity guarantees no non-adjacent pair can conflict without adjacent pairs conflicting.

### Pattern 3: Earliest Deadline First (EDF) Greedy Scheduling (LC 435)
* **The Theorem**: To minimize interval removals, maximize the number of mutually compatible intervals.
* **Greedy-Choice Property**: Selecting the compatible interval with the **earliest end time** ($e_i$) leaves maximal time available for future selections.
* **Proof Sketch (Exchange Argument)**:
  Let $A = \langle a_1, a_2, \dots \rangle$ be the greedy schedule sorted by end time, and $O = \langle o_1, o_2, \dots \rangle$ be any optimal schedule.
  * By construction, $a_1.e \le o_1.e$.
  * Replacing $o_1$ with $a_1$ in $O$ yields a valid compatible schedule $O' = \langle a_1, o_2, \dots \rangle$ since $a_1$ finishes no later than $o_1$, leaving at least as much room for $o_2$.
  * By induction, the greedy schedule contains at least as many compatible intervals as any arbitrary schedule.
* **Complexity**: $\mathcal{O}(N \log N)$ time, $\mathcal{O}(1)$ space.

### Pattern 4: Chronological Event Sweep-Line (LC 253: Meeting Rooms II)
* To determine the peak concurrent overlapping intervals:
  * Each interval $[s, e]$ produces two discrete point events:
    * Start event: $+1$ room needed at time $s$
    * End event: $-1$ room needed at time $e$
  * Sorting start times and end times into independent arrays allows a two-pointer sweep:
    $$\text{If } \text{starts}[s] < \text{ends}[e] \implies \text{rooms} \leftarrow \text{rooms} + 1, \quad s \leftarrow s + 1$$
    $$\text{Else } \implies \text{rooms} \leftarrow \text{rooms} - 1, \quad e \leftarrow e + 1$$
  * Peak concurrent count $\max(\text{rooms})$ across all timestamps is the minimum capacity required.
  * Avoids heap allocation overhead while retaining $\mathcal{O}(N \log N)$ time and $\mathcal{O}(N)$ cache-friendly array space.
