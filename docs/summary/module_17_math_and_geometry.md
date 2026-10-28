# Module 17 Summary: Math & Geometry

This document formalizes matrix coordinate transformations, rotation decomposition theorems, boundary contraction dynamics, and constant-space state encoding underlying Module 17.

---

## 1. Linear Algebra of Matrix Rotations

Let $M$ be an $N \times N$ matrix. Rotating $M$ by $90^\circ$ clockwise maps coordinate $(r, c)$ according to:
$$(r, c) \longmapsto (c, \; N - 1 - r)$$

### The Decomposition Theorem (LeetCode 48: Rotate Image)
Direct 4-way element cycling requires managing 4 variables across concentric square rings, which is highly prone to indexing and parity bugs.
Instead, we decompose the rotation into two fundamental linear algebra operators:
$$R_{90^\circ} = \text{Reflect}_{\text{horizontal}} \circ \text{Transpose}$$

1. **Transpose across Main Diagonal**:
   $$(r, c) \longmapsto (c, r) \quad \text{via } M[r][c] \longleftrightarrow M[c][r] \quad \forall r < c$$
2. **Horizontal Reflection**:
   $$(c, r) \longmapsto (c, \; N - 1 - r) \quad \text{via reversing each row in-place}$$

```
Initial:          Transpose:        Horizontal Reverse:
[ 1  2  3 ]       [ 1  4  7 ]       [ 7  4  1 ]
[ 4  5  6 ]  ==>  [ 2  5  8 ]  ==>  [ 8  5  2 ]
[ 7  8  9 ]       [ 3  6  9 ]       [ 9  6  3 ]
```

* **Complexity**: $\mathcal{O}(N^2)$ operations with strictly $\mathcal{O}(1)$ auxiliary space.

---

## 2. Boundary Contraction Dynamics (LeetCode 54: Spiral Matrix)

Spiral traversal models a 4-phase perimeter walk that progressively shrinks the active rectangular coordinate space:
$$\mathcal{B} = \langle \text{top}, \; \text{bottom}, \; \text{left}, \; \text{right} \rangle$$

```
    left                    right
top  +------------------------+
     |   →   →   →   →   →    |
     |   ↑   +------------+   ↓
     |       |            |   |
     |   ↑   +------------+   ↓
bot  |   ←   ←   ←   ←   ←    |
     +------------------------+
```

* **Perimeter Sequence**:
  1. $\text{Row}(\text{top}): \quad c \in [\text{left}, \text{right}] \implies \text{top} \leftarrow \text{top} + 1$
  2. $\text{Col}(\text{right}): \quad r \in [\text{top}, \text{bottom}] \implies \text{right} \leftarrow \text{right} - 1$
  3. **Mid-Loop Invariant Check**: Verify $\text{top} \le \text{bottom} \land \text{left} \le \text{right}$ before continuing!
  4. $\text{Row}(\text{bottom}): \quad c \in [\text{right}, \text{left}] \implies \text{bottom} \leftarrow \text{bottom} - 1$
  5. $\text{Col}(\text{left}): \quad r \in [\text{bottom}, \text{top}] \implies \text{left} \leftarrow \text{left} + 1$

---

## 3. In-Place State Encoding (LeetCode 73: Set Matrix Zeroes)

When an algorithm requires zeroing rows and columns without allocating $\mathcal{O}(M + N)$ external tracking sets, the input matrix itself must serve as its own scratchpad.

### Header Row/Column Reutilization
* **Row Markers**: $M[0][c] = 0$ indicates column $c$ must be zeroed.
* **Column Markers**: $M[r][0] = 0$ indicates row $r$ must be zeroed.
* **The Intersection Disambiguation**:
  The origin cell $M[0][0]$ resides simultaneously in row 0 and column 0. Assigning $M[0][0]$ to track both creates an ambiguity (zeroing column 0 would trigger row 0 to be zeroed even if row 0 contained no original zeros).
* **Resolution**:
  * $M[0][0]$ tracks Column 0.
  * A single boolean scalar variable `row_zero` tracks Row 0.
* **Execution Ordering**:
  1. Scan and flag ($1 \dots M-1, 1 \dots N-1$).
  2. Update interior cells first ($1 \dots M-1, 1 \dots N-1$) so markers are not prematurely overwritten.
  3. Update Column 0 using $M[0][0]$.
  4. Update Row 0 using `row_zero`.
* **Complexity**: $\mathcal{O}(M \cdot N)$ time, strictly $\mathcal{O}(1)$ space.
