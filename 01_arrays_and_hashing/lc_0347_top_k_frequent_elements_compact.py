"""LeetCode 347: Top K Frequent Elements (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/top-k-frequent-elements/
Difficulty: Medium
Category: Arrays & Hashing

Pattern Context:
    While a min-heap gives O(n log k) time, we can achieve true O(n) linear time
    using Bucket Sort!
    Because no element can appear more than n times, we create n + 1 buckets where
    the index represents the frequency count: bucket[freq] = [elements with that freq].
    Scanning the buckets backwards from n down to 1 collects the top k elements in O(n).

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 01_arrays_and_hashing/lc_0347_top_k_frequent_elements_compact.py
"""

from __future__ import annotations
from typing import List, Dict

# Sentinel placeholder for exercise tasks
TODO = None


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """Returns the k most frequent elements in O(n) linear time using bucket sort.

    Algorithmic Requirements:
    - Time Complexity: O(n) linear time where n = len(nums).
    - Space Complexity: O(n) auxiliary memory for count map and frequency buckets.

    Steps to implement:
    1. Count occurrences of each number using a hash map `count`.
    2. Initialize `buckets = [[] for _ in range(len(nums) + 1)]`.
    3. For each number `n` and its count `c`, append `n` to `buckets[c]`.
    4. Iterate through `buckets` in reverse (from len(nums) down to 1):
       - For each number in `buckets[i]`, append to `result`.
       - When `len(result) == k`, return `result`.

    -------------------------------------------------------------------------
    TODO: Implement the bucket sort collection logic below.
    -------------------------------------------------------------------------
    """
    count: Dict[int, int] = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1

    buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
    for n, c in count.items():
        buckets[c].append(n)

    result: List[int] = []
    # <<< YOUR CODE HERE >>>
    # Hint: Traverse buckets backwards from len(buckets) - 1 down to 1.
    for i in range(len(buckets) - 1, 0, -1):
        for n in buckets[i]:
            result.append(n)
            # Check if we have collected k elements
            should_return = TODO  # Replace with: len(result) == k
            if should_return is None:
                raise NotImplementedError("TODO: Check termination condition for top k.")
            if should_return:
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

    print("Running verification for lc_0347_top_k_frequent_elements_compact.py...")
    for idx, (nums, k, expected_set) in enumerate(test_cases, 1):
        result = top_k_frequent(list(nums), k)
        assert set(result) == expected_set, f"Case {idx} failed: got {set(result)}, expected {expected_set}"
        assert len(result) == k, f"Case {idx} failed length check: got {len(result)}, expected {k}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
