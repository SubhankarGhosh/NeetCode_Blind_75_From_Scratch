"""
LeetCode 435: Non-overlapping Intervals
Module: 16_intervals
Difficulty: Medium
Tags: Array, Dynamic Programming, Greedy, Sorting

PROBLEM DESCRIPTION:
Given an array of intervals intervals where intervals[i] = [starti, endi], return
the minimum number of intervals you need to remove to make the rest of the
intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping.
For example, [1, 2] and [2, 3] are non-overlapping.

Example 1:
    Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
    Output: 1
    Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
    Input: intervals = [[1,2],[1,2],[1,2]]
    Output: 2
    Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
    Input: intervals = [[1,2],[2,3]]
    Output: 0
    Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:
    * 1 <= intervals.length <= 10^5
    * intervals[i].length == 2
    * -5 * 10^4 <= starti < endi <= 5 * 10^4
"""

from typing import List

TODO = None


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Calculates minimum removals using Interval Scheduling Greedy Algorithm.

        Greedy Choice Property:
        Sort intervals by end time. By picking the interval that finishes earliest,
        we leave the maximum possible remaining time for subsequent intervals,
        minimizing the number of removals needed.

        Time Complexity:  O(N log N)
        Space Complexity: O(1) auxiliary space
        """
        # Active Learning:
        # Sort intervals by their end time (key = lambda x: x[1])
        intervals.sort(key=lambda x: x[1])

        removals = 0
        prev_end = float("-inf")

        for start, end in intervals:
            # TODO: If start >= prev_end, no overlap; accept interval and update prev_end
            # Otherwise, an overlap occurs; increment removals
            if start >= prev_end:
                prev_end = end
            else:
                removals += 1

        return removals


def test_non_overlapping_intervals():
    solver = Solution()

    # Case 1: [[1,2],[2,3],[3,4],[1,3]] -> 1 removal ([1,3])
    assert solver.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1, "Case 1 failed"

    # Case 2: Identical overlapping intervals [[1,2],[1,2],[1,2]] -> 2 removals
    assert solver.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2, "Case 2 failed"

    # Case 3: Already disjoint [[1,2],[2,3]] -> 0 removals
    assert solver.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0, "Case 3 failed"

    # Case 4: Single interval
    assert solver.eraseOverlapIntervals([[1, 5]]) == 0, "Case 4 failed"

    # Case 5: Nested intervals [[1,10],[2,3],[3,4]] -> 1 removal ([1,10])
    assert solver.eraseOverlapIntervals([[1, 10], [2, 3], [3, 4]]) == 1, "Case 5 failed"

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_non_overlapping_intervals()
