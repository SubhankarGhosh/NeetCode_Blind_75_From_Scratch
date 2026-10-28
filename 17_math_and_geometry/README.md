# Module 17: Math & Geometry

Mastering in-place 2D matrix transformations, coordinate reflections, clockwise rotation decomposition, multi-boundary spiral contractions, and $\mathcal{O}(1)$ in-place marker flag state encoding across 3 foundational LeetCode problems.

---

## 📋 Problem Map

| Problem | Difficulty | Key Paradigm | Time | Space | Status |
| :--- | :---: | :--- | :---: | :---: | :---: |
| [48. Rotate Image](https://leetcode.com/problems/rotate-image/) | Medium | Linear Algebra Decomposition (Transpose + Horizontal Reflection) | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Medium | 4-Pointer Boundary Contraction Traversal | $\mathcal{O}(M \cdot N)$ | $\mathcal{O}(1)$ | 🟢 Complete |
| [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Medium | In-Place Header Marker Encoding / Constant Auxiliary Space | $\mathcal{O}(M \cdot N)$ | $\mathcal{O}(1)$ | 🟢 Complete |

---

## 🏃 Execution Instructions

Run exercises standalone with zero third-party dependencies:

```powershell
# Set UTF-8 encoding in PowerShell
$env:PYTHONIOENCODING = "utf-8"

# 1. Practice with compact exercises (fill TODOs)
python 17_math_and_geometry/lc_0048_rotate_image_compact.py
python 17_math_and_geometry/lc_0054_spiral_matrix_compact.py
python 17_math_and_geometry/lc_0073_set_matrix_zeroes_compact.py

# 2. Run verified reference solutions
python 17_math_and_geometry/lc_0048_rotate_image_solution.py
python 17_math_and_geometry/lc_0054_spiral_matrix_solution.py
python 17_math_and_geometry/lc_0073_set_matrix_zeroes_solution.py
```

---

## 📚 Deep-Dive Documentation
- **Theoretical Foundations**: [`docs/summary/module_17_math_and_geometry.md`](../docs/summary/module_17_math_and_geometry.md)
- **Interview Traps & Clarifications**: [`docs/clarifications/module_17_math_and_geometry.md`](../docs/clarifications/module_17_math_and_geometry.md)
