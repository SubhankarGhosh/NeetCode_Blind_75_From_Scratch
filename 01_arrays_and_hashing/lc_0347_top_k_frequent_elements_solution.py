"""LeetCode 347: Top K Frequent Elements (Reference Solution)

Problem URL: https://leetcode.com/problems/top-k-frequent-elements/
Difficulty: Medium
Category: Arrays & Hashing

Complexity Analysis:
- Time Complexity: O(n) where n is the length of nums.
  1. Counting frequencies: O(n)
  2. Populating frequency buckets: O(n)
  3. Scanning buckets from n down to 1: O(n) total iterations
  Overall Time: O(n), beating the O(n log k) heap approach.
- Space Complexity: O(n) auxiliary space to store frequency map and buckets.
"""

from __future__ import annotations
from typing import List, Dict


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """Finds the k most frequent elements in linear O(n) time using Bucket Sort."""
    count: Dict[int, int] = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1

    # buckets[i] contains all numbers that appear with frequency i
    buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
    for n, c in count.items():
        buckets[c].append(n)

    result: List[int] = []
    # Traverse from highest possible frequency down to 1
    for i in range(len(buckets) - 1, 0, -1):
        for n in buckets[i]:
            result.append(n)
            if len(result) == k:
                return result

    return result


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2, {1, 2}),
        ([1], 1, {1}),
        ([4, 1, -1, 2, -1, 2, 3], 2, {-1, 2}),
        ([1, 2], 2, {1, 2}),
    ]

    print("Running verification for lc_0347_top_k_frequent_elements_solution.py...")
    for idx, (nums, k, expected_set) in enumerate(test_cases, 1):
        result = top_k_frequent(list(nums), k)
        assert set(result) == expected_set, f"Case {idx} failed: got {set(result)}, expected {expected_set}"
        assert len(result) == k, f"Case {idx} failed length check: got {len(result)}, expected {k}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
