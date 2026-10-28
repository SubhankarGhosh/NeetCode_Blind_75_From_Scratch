"""Master Test Runner for NeetCode Blind 75 From Scratch.

Discovers and executes all reference solutions sequentially across all modules,
reporting individual module metrics and total curriculum pass rate.
"""

from __future__ import annotations
import os
import sys
import subprocess
from pathlib import Path

# Ensure UTF-8 output encoding on Windows consoles
if sys.platform == "win32":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
    os.environ["PYTHONIOENCODING"] = "utf-8"

REPO_ROOT = Path(__file__).resolve().parent

MODULE_DIRS = [
    ("Module 01: Arrays & Hashing", REPO_ROOT / "01_arrays_and_hashing"),
    ("Module 02: Two Pointers", REPO_ROOT / "02_two_pointers"),
    ("Module 03: Sliding Window", REPO_ROOT / "03_sliding_window"),
    ("Module 04: Stack", REPO_ROOT / "04_stack"),
    ("Module 05: Binary Search", REPO_ROOT / "05_binary_search"),
    ("Module 06: Linked List", REPO_ROOT / "06_linked_list"),
    ("Module 07: Trees", REPO_ROOT / "07_trees"),
    ("Module 08: Tries", REPO_ROOT / "08_tries"),
    ("Module 09: Heap / Priority Queue", REPO_ROOT / "09_heap_priority_queue"),
    ("Module 10: Backtracking", REPO_ROOT / "10_backtracking"),
    ("Module 11: Graphs", REPO_ROOT / "11_graphs"),
    ("Module 12: Advanced Graphs", REPO_ROOT / "12_advanced_graphs"),
    ("Module 13: 1-D Dynamic Programming", REPO_ROOT / "13_1d_dynamic_programming"),
    ("Module 14: 2-D Dynamic Programming", REPO_ROOT / "14_2d_dynamic_programming"),
    ("Module 15: Greedy", REPO_ROOT / "15_greedy"),
    ("Module 16: Intervals", REPO_ROOT / "16_intervals"),
    ("Module 17: Math & Geometry", REPO_ROOT / "17_math_and_geometry"),
    ("Module 18: Bit Manipulation", REPO_ROOT / "18_bit_manipulation"),
]


def run_all() -> int:
    print("=" * 80)
    print("  NEETCODE BLIND 75 FROM SCRATCH: CURRICULUM VERIFICATION SUITE")
    print("=" * 80)

    total_passed = 0
    total_failed = 0
    failures = []

    for mod_title, mod_dir in MODULE_DIRS:
        if not mod_dir.exists():
            continue

        solution_files = sorted(mod_dir.glob("*_solution.py"))
        if not solution_files:
            continue

        print(f"\n[+] {mod_title}")
        print("-" * 80)

        for sol_path in solution_files:
            rel_path = sol_path.relative_to(REPO_ROOT)
            cmd = [sys.executable, str(sol_path)]
            result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

            if result.returncode == 0:
                print(f"    [PASS] {sol_path.name}")
                total_passed += 1
            else:
                print(f"    [FAIL] {sol_path.name}")
                total_failed += 1
                failures.append((str(rel_path), result.stderr))

    total_executed = total_passed + total_failed
    print("\n" + "=" * 80)
    print("  SUMMARY REPORT")
    print("=" * 80)
    print(f"  Total Solutions Executed: {total_executed}")
    print(f"  Passed:                   {total_passed}")
    print(f"  Failed:                   {total_failed}")
    if total_executed > 0:
        print(f"  Success Rate:             {(total_passed / total_executed * 100):.1f}%")

    if failures:
        print("\n[!] Failures:")
        for file, err in failures:
            print(f"  - {file}:\n{err}")
        return 1

    print("\n[SUCCESS] All executed reference solutions passed deterministically!")
    return 0


if __name__ == "__main__":
    sys.exit(run_all())
