# Module 01 Summary: Arrays & Hashing

This document outlines the core algorithmic foundations, mathematical invariants, and data structure principles underlying the 8 problems of Module 01.

---

## 1. Hash Table Mechanics & Amortized Complexity

A hash table maps arbitrary keys to bucket slots using a deterministic hash function:
$$h: \mathcal{K} \to \{0, 1, \dots, M - 1\}$$

* **Expected Lookup & Insertion**: Under the Uniform Hashing Assumption (SUHA), average search, insertion, and deletion run in $\mathcal{O}(1)$ time with load factor $\alpha = N / M$.
* **Worst-Case Degradation**: When collisions spike (adversarial input or hash clustering), chain lengths can grow to $\mathcal{O}(N)$. Modern runtimes (Python's SipHash/dict design) mitigate this via randomized per-process seeds and open addressing with quadratic probing.

---

## 2. Algorithmic Invariants & Key Patterns

### Pattern 1: Complement Search (LeetCode 1: Two Sum)
* **Mathematical Invariant**: For an equation $a + b = T$, knowing $a$ uniquely fixes the required complement $b = T - a$.
* **State Formulation**: At step $i$ with element $x_i$:
  $$\text{Query: } (T - x_i) \in \mathcal{H} \implies \text{Pair Found: } (\mathcal{H}[T - x_i], i)$$
  $$\text{Update: } \mathcal{H}[x_i] = i$$
* **Complexity**: $\mathcal{O}(n)$ time and $\mathcal{O}(n)$ space in a single pass.

### Pattern 2: Canonical Hashable Signatures (LeetCode 49: Group Anagrams)
* Two strings $s_1$ and $s_2$ are anagrams if their character multisets are identical: $\mathcal{M}(s_1) \equiv \mathcal{M}(s_2)$.
* **Signature Choice**:
  * *Sorted String*: $\mathcal{O}(k \log k)$ time per word.
  * *Fixed Alphabet Tuple*: A 26-element tuple $\vec{c} = (c_0, c_1, \dots, c_{25})$ where $c_j$ counts the frequency of character $j$. Because tuples in Python are immutable, $\vec{c}$ serves as a direct dictionary key in $\mathcal{O}(k)$ time, reducing total runtime to $\mathcal{O}(n \cdot k)$.

### Pattern 3: Linear-Time Bucket Sort (LeetCode 347: Top K Frequent Elements)
* Standard sorting of frequency entries takes $\mathcal{O}(u \log u)$ where $u$ is the number of unique elements.
* Min-heap maintenance takes $\mathcal{O}(n \log k)$.
* **Bucket Sort Invariant**: The maximum possible frequency of any element in an array of size $n$ is $n$.
* **Construction**:
  $$\text{bucket}[f] = \{x \in \text{nums} \mid \text{count}(x) = f\}, \quad \forall f \in [0, n]$$
  Scanning $\text{bucket}[n], \text{bucket}[n-1], \dots, \text{bucket}[1]$ until $k$ elements are gathered guarantees strict $\mathcal{O}(n)$ time and $\mathcal{O}(n)$ auxiliary space.

### Pattern 4: Running Cumulative Accumulation (LeetCode 238: Product of Array Except Self)
* To calculate $P_i = \prod_{j \ne i} x_j$ without using division:
  $$P_i = \left(\prod_{j < i} x_j\right) \times \left(\prod_{j > i} x_j\right) = \text{Prefix}_i \times \text{Postfix}_i$$
* **In-Place Space Optimization**:
  1. Forward Pass: compute $\text{Prefix}_i$ into `output[i]`.
  2. Reverse Pass: accumulate $\text{Postfix}_i$ in a scalar register variable and multiply into `output[i]` in-place.
  3. Achieves $\mathcal{O}(n)$ time and $\mathcal{O}(1)$ auxiliary space.

### Pattern 5: Length-Prefixed Chunking (LeetCode 271: Encode & Decode Strings)
* Delimiter-based serialization (`join(",")`) fails when payload data contains the delimiter.
* **Length-Prefix Protocol**:
  $$\text{Chunk}(s) = \text{len}(s) + \text{"\#"} + s$$
* Even if $s$ contains "\#", digits, newlines, or Unicode, the delimiter "\#" is only parsed at the index indicated by the length counter, preventing delimiter collision.

### Pattern 6: Sequence Head Identification (LeetCode 128: Longest Consecutive Sequence)
* A number $x$ is the beginning (head) of a contiguous integer sequence if and only if:
  $$(x - 1) \notin \mathcal{S}$$
* By only initiating inner streak traversals ($x+1, x+2, \dots$) when $x$ is verified as a sequence head, no number is traversed as part of an inner streak more than once. Total inner operations across all numbers is bounded by $n$.
* Total Time: $\mathcal{O}(n)$, Space: $\mathcal{O}(n)$.
