# Module 08 Summary: Tries

This document outlines the core architectural mechanics, retrieval tree complexity proofs, and grid search pruning principles underlying Module 08.

---

## 1. The Trie (Prefix Tree) Data Structure

A **Trie** (re**trie**val tree) is a specialized rooted $k$-ary search tree used to store associative arrays where keys are usually strings:
* **The Prefix Sharing Principle**: Rather than storing entire strings as monolithic keys (like a Hash Table), all descendants of a node share a common string prefix associated with that node.
* **Node Anatomy**:
  $$\text{TrieNode} = \langle \text{children}: \Sigma \to \text{TrieNode}, \text{is\_terminal}: \mathbb{B}, [\text{word}: \text{str}] \rangle$$

### Complexity Analysis
* **Time**: Inserting, searching, or prefix-matching a string of length $L$ takes strictly $\mathcal{O}(L)$ operations. Unlike a hash table where string hashing takes $\mathcal{O}(L)$ followed by potential collision resolution, a Trie provides deterministic worst-case $\mathcal{O}(L)$ guarantees.
* **Space**: $\mathcal{O}(N \cdot L)$ in the worst case (no shared prefixes), but approaches $\mathcal{O}(\text{Unique Prefix Count})$ in natural language datasets.

---

## 2. Invariants & Key Algorithmic Paradigms

### Pattern 1: Deterministic Retrieval vs. Hash Tables (LC 208)
* While a hash set answers `word in dict` in average $\mathcal{O}(L)$ time, it **cannot** efficiently answer `starts_with(prefix)` without inspecting all keys ($\mathcal{O}(N \cdot L)$) or storing all prefix substrings ($\mathcal{O}(N \cdot L^2)$ space).
* A Trie resolves both `search(word)` and `starts_with(prefix)` in strict $\mathcal{O}(L)$ time by walking down the character path.

### Pattern 2: Wildcard Branching Search (LC 211)
* For search pattern $P$:
  * If $P[i] \in \Sigma_{\text{char}}$: follow deterministic single edge $u \leftarrow u.\text{children}[P[i]]$ in $\mathcal{O}(1)$.
  * If $P[i] = \text{"."}$: evaluate nondeterministic branch over all active edges:
    $$\bigvee_{v \in \text{children}(u)} \text{match}(P[i+1 \dots], v)$$
* If $d$ is the number of wildcard dots, maximum states explored is bounded by $\mathcal{O}(26^d \cdot L)$.

### Pattern 3: Trie-Guided Backtracking & Dynamic Pruning (LC 212)
* **The Naive Flaw**: Running DFS on an $M \times N$ board for each of $W$ words individually takes $\mathcal{O}(W \cdot M \cdot N \cdot 4^L)$.
* **The Trie-Guided Invariant**:
  * Insert all $W$ words into a Trie in $\mathcal{O}(\sum |W|)$ preprocessing time.
  * Execute DFS on the 2D grid while simultaneously traversing the Trie from its root.
  * If the character at `board[r][c]` is not in `curr_trie_node.children`, **prune the entire subgrid exploration tree immediately**.
* **Dynamic Leaf Pruning**:
  * Once a word is matched, clear its `node.word = None` to prevent duplicate discoveries.
  * If a leaf node has no remaining children (`len(node.children) == 0`), pop it from its parent dictionary:
    $$\text{parent.children.pop}(c)$$
  * This prunes completed vocabulary branches, eliminating redundant passes on subsequent cell scans.
