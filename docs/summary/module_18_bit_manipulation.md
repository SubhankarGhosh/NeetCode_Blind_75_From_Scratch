# Module 18 Summary: Bit Manipulation

This document formalizes the algebraic axioms of bitwise operators, Brian Kernighan's bit-clearing invariant, XOR cancellation properties, and bitwise dynamic programming underlying Module 18.

---

## 1. Axioms of Boolean Algebra & Bitwise Operations

Bitwise operations manipulate the fundamental binary representations of integers at the silicon hardware level.

### Canonical XOR ($\oplus$) Properties
1. **Self-Annihilation**: $x \oplus x = 0$
2. **Identity Element**: $x \oplus 0 = x$
3. **Commutativity**: $x \oplus y = y \oplus x$
4. **Associativity**: $(x \oplus y) \oplus z = x \oplus (y \oplus z)$

### Applications in Uniqueness & Missing Element Search (LC 136 & LC 268)
* In an array where every element appears twice except for an isolated element $u$:
  $$\bigoplus_{i=0}^{N-1} A_i = (x_1 \oplus x_1) \oplus (x_2 \oplus x_2) \oplus \dots \oplus u = 0 \oplus 0 \oplus \dots \oplus u = u$$
* In **Missing Number** (LC 268), XORing the complete index set $[0, N]$ against the array elements cancels all matching values, isolating the missing integer in strictly $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space without arithmetic overflow.

---

## 2. Brian Kernighan's Algorithm (LC 191: Number of 1 Bits)

Counting set bits (Hamming Weight) naively requires testing all 32 bits. Brian Kernighan's algorithm reduces the number of operations to strictly the number of set bits $K \le 32$.

### The Invariant Proof of $n \& (n - 1)$
Let $n$ be written in binary with least significant set bit at position $k$:
$$n = \underbrace{b_{31} \dots b_{k+1}}_{\text{prefix}} \, 1 \, \underbrace{00 \dots 0}_{k \text{ zeros}}$$
Subtracting 1 borrows from position $k$:
$$n - 1 = \underbrace{b_{31} \dots b_{k+1}}_{\text{prefix}} \, 0 \, \underbrace{11 \dots 1}_{k \text{ ones}}$$
Performing bitwise AND:
$$n \& (n - 1) = \underbrace{b_{31} \dots b_{k+1}}_{\text{prefix}} \, 0 \, \underbrace{00 \dots 0}_{k \text{ zeros}}$$
* **Conclusion**: Bit position $k$ is cleared to `0`, while all higher and lower bits remain unchanged or zeroed out.
* Every execution of $n \leftarrow n \& (n - 1)$ removes exactly one set bit. The loop executes in $\mathcal{O}(K)$ time.

---

## 3. Bitwise Dynamic Programming (LC 338: Counting Bits)

To compute the popcount for all numbers $0 \le i \le N$ in linear $\mathcal{O}(N)$ time, we leverage optimal substructure across bit representations.

### Formulation 1: Right-Shift Decomposition
Right-shifting $i$ by 1 ($i \gg 1$) removes the least significant bit (LSB). The set bits in $i$ equal the set bits in $\lfloor i / 2 \rfloor$ plus the LSB:
$$\text{dp}[i] = \text{dp}[i \gg 1] + (i \& 1)$$

### Formulation 2: Kernighan Predecessor Transition
Since $i \& (i - 1)$ has strictly fewer bits and is strictly smaller than $i$ ($i \& (i - 1) < i$):
$$\text{dp}[i] = \text{dp}[i \& (i - 1)] + 1$$
Both formulations compute each table entry in $\mathcal{O}(1)$ time, yielding an optimal single-pass $\mathcal{O}(N)$ solution.

---

## 4. 32-Bit Register Mirroring (LC 190: Reverse Bits)

Reversing the binary representation of a 32-bit unsigned integer $n$ requires mapping bit index $i \in [0, 31]$ to mirrored index $(31 - i)$:

$$\text{bit}_i = (n \gg i) \& 1 \implies \text{res} \leftarrow \text{res} \;|\; (\text{bit}_i \ll (31 - i))$$

Because the bit width $W = 32$ is fixed, the loop runs in strictly $\mathcal{O}(1)$ time using $\mathcal{O}(1)$ register space.
