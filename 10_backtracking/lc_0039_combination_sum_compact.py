"""LeetCode 39: Combination Sum (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/combination-sum/
Difficulty: Medium
Category: Backtracking

Pattern Context:
    Given an array of distinct integers `candidates` and a `target`, return all unique
    combinations where the chosen numbers sum to target. The same number may be chosen
    an unlimited number of times.

    The Inclusion/Exclusion Decision Tree:
    At each index `i` with current running combination:
    - Choice A (Include candidates[i]):
      Add candidates[i] to combination, and recurse on index `i` (allowing reuse).
    - Choice B (Exclude candidates[i]):
      Backtrack (remove candidates[i]), and recurse on index `i + 1` (never pick candidates[i] again).
    - Pruning: If total > target or i >= len(candidates), terminate branch immediately.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 10_backtracking/lc_0039_combination_sum_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """Finds all unique combinations summing to target using decision-tree backtracking.

    Algorithmic Requirements:
    - Time Complexity: O(2^(target / min_val)) worst-case state space.
    - Space Complexity: O(target / min_val) maximum call stack depth.

    Steps to implement:
    1. Initialize `res = []`.
    2. Define `dfs(i, cur, total)`:
       - If `total == target`: append a shallow copy of `cur` to `res`, return.
       - If `i >= len(candidates) or total > target`: return.
       - Choice 1: Include `candidates[i]` -> `cur.append(candidates[i])`, recurse `dfs(i, cur, total + candidates[i])`.
       - Choice 2: Exclude `candidates[i]` -> `cur.pop()`, recurse `dfs(i + 1, cur, total)`.
    3. Call `dfs(0, [], 0)`.
    4. Return `res`.

    -------------------------------------------------------------------------
    TODO: Implement the inclusion/exclusion recursive backtracking below.
    -------------------------------------------------------------------------
    """
    res: List[List[int]] = []

    def dfs(i: int, cur: List[int], total: int) -> None:
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target:
            return

        # <<< YOUR CODE HERE >>>
        # Choice 1: Include candidate at index i (can reuse candidates[i])
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])

        # Backtrack state
        cur.pop()

        # Choice 2: Exclude candidate at index i, move to i + 1
        exclude_action = TODO  # Replace with: dfs(i + 1, cur, total)
        if exclude_action is None and i < len(candidates):
            raise NotImplementedError("TODO: Recurse on excluded branch i + 1.")
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    def normalize_combinations(combs: List[List[int]]) -> List[List[int]]:
        return sorted([sorted(c) for c in combs])

    test_cases = [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([2], 1, []),
        ([1], 2, [[1, 1]]),
        ([7, 3, 2], 18, [
            [2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 3, 3],
            [2, 2, 2, 2, 3, 7],
            [2, 2, 2, 3, 3, 3, 3],
            [2, 2, 7, 7],
            [2, 3, 3, 3, 7],
            [3, 3, 3, 3, 3, 3],
        ]),
    ]

    print("Running verification for lc_0039_combination_sum_compact.py...")
    for idx, (cands, tgt, expected) in enumerate(test_cases, 1):
        result = combination_sum(list(cands), tgt)
        norm_res = normalize_combinations(result)
        norm_exp = normalize_combinations(expected)
        assert norm_res == norm_exp, f"Case {idx} failed: got {norm_res}, expected {norm_exp}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
