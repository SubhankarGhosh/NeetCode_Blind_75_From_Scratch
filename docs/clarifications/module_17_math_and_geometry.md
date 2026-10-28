# Module 17 Clarifications & Pitfalls: Math & Geometry

This document details subtle mid-loop boundary bugs, update ordering hazards, and in-place marker corruptions for Module 17.

---

### Q1: The Mid-Loop Guard Trap in Spiral Matrix (LC 54)
* **The Bug**: Omitting `if not (left <= right and top <= bottom): break` between the second and third sweeps.
* **Why it breaks on $1 \times N$ or $M \times 1$ matrices**:
  * Consider `matrix = [[1, 2, 3, 4]]` ($1 \times 4$):
    1. Sweep 1 (Left to Right along `top`): Appends `1, 2, 3, 4`. Increments `top` from 0 to 1.
    2. Sweep 2 (Top to Bottom along `right`): `top (1) > bottom (0)`, loop does 0 iterations. Decrements `right` to 2.
    3. Sweep 3 (Right to Left along `bottom`): If the guard is missing, this loop executes for `col` from 2 down to 0 along row 0, appending `3, 2, 1`!
  * Result: `[1, 2, 3, 4, 3, 2, 1]` (corrupted duplicate output).
* **Rule**: Whenever 4 sequential boundary sweeps mutate bounds independently, check that bounds remain valid before executing the reverse sweeps.

---

### Q2: The Execution Order Hazard in Set Matrix Zeroes (LC 73)
* **The Bug**: Zeroing out the header row or column *before* updating the interior cells:
  ```python
  # DISASTROUS UPDATE ORDER:
  if row_zero:
      for c in range(cols):
          matrix[0][c] = 0  # WIPES OUT ALL COLUMN MARKERS!

  # Now every column marker is 0, turning the ENTIRE matrix to 0!
  for r in range(1, rows):
      for c in range(1, cols):
          if matrix[0][c] == 0: ...
  ```
* **The Rule**: Always update from the inside out:
  1. Interior cells first ($r \ge 1, c \ge 1$) using header markers.
  2. First column next.
  3. First row last.

---

### Q3: Transpose Double-Swap Trap (LC 48)
* **The Bug**: Running the inner transpose loop over the full row:
  ```python
  for i in range(n):
      for j in range(n):  # WRONG: Swaps twice!
          matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
  ```
* **Why it fails**:
  * At $(i, j) = (0, 1)$, elements are swapped.
  * Later at $(i, j) = (1, 0)$, elements are swapped back to their original positions!
* **The Fix**: Only iterate above the main diagonal:
  ```python
  for i in range(n):
      for j in range(i + 1, n):  # Strictly upper triangular matrix
          matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
  ```

---

### Q4: Clockwise vs. Counter-Clockwise Rotation Formulae
* **$90^\circ$ Clockwise**:
  $$\text{Transpose} \longrightarrow \text{Reverse each row horizontally}$$
* **$90^\circ$ Counter-Clockwise**:
  $$\text{Transpose} \longrightarrow \text{Reverse rows vertically (top-to-bottom)}$$
  Or equivalently:
  $$\text{Reverse each row horizontally} \longrightarrow \text{Transpose}$$
* **$180^\circ$ Rotation**:
  $$\text{Reverse vertically} \longrightarrow \text{Reverse each row horizontally}$$
