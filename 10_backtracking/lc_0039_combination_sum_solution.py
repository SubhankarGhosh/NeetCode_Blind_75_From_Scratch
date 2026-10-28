"""LeetCode 39: Combination Sum (Reference Solution)

Problem URL: https://leetcode.com/problems/combination-sum/
Difficulty: Medium
Category: Backtracking

Complexity Analysis:
- Time Complexity: O(2^(target / min(candidates))) in worst case.
  The maximum depth of the decision tree is bounded by target / min_candidate.
  At each node, there are 2 recursive decisions: include current candidate or advance index.
- Space Complexity: O(target / min(candidates)) call stack frames and combination buffer.
"""

from __future__ import annotations
from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """Generates all combinations that sum to target using a binary inclusion/exclusion tree."""
    res: List[List[int]] = []

    def dfs(i: int, cur: List[int], total: int) -> None:
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target:
            return

        # Decision 1: Include candidates[i] (can be reused)
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])

        # Backtrack
        cur.pop()

        # Decision 2: Exclude candidates[i] (move forward to next candidate)
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

    print("Running verification for lc_0039_combination_sum_solution.py...")
    for idx, (cands, tgt, expected) in enumerate(test_cases, 1):
        result = combination_sum(list(cands), tgt)
        norm_res = normalize_combinations(result)
        norm_exp = normalize_combinations(expected)
        assert norm_res == norm_exp, f"Case {idx} failed: got {norm_res}, expected {norm_exp}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
