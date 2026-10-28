"""
LeetCode 56: Merge Intervals
Module: 16_intervals
Difficulty: Medium
Tags: Array, Sorting

PROBLEM DESCRIPTION:
Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

Example 1:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
    * 1 <= intervals.length <= 10^4
    * intervals[i].length == 2
    * 0 <= starti <= endi <= 10^4
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merges all overlapping intervals.

        Invariant:
        By sorting intervals by their start times:
        If interval B starts after interval A (A.start <= B.start), an overlap occurs
        if and only if B.start <= A.end.
        When overlapping, the merged interval spans [A.start, max(A.end, B.end)].
        If B.start > A.end, interval A is closed and will never overlap with any subsequent interval.

        Time Complexity:  O(N log N) dominated by sorting.
        Space Complexity: O(N) for output list (or O(log N) auxiliary sorting space).
        """
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged: List[List[int]] = [intervals[0]]

        for current in intervals[1:]:
            last_end = merged[-1][1]
            curr_start, curr_end = current

            if curr_start <= last_end:
                merged[-1][1] = max(last_end, curr_end)
            else:
                merged.append(current)

        return merged


def test_merge_intervals():
    solver = Solution()

    # Case 1: Standard overlapping intervals
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    expected1 = [[1, 6], [8, 10], [15, 18]]
    assert solver.merge(intervals1) == expected1, "Case 1 failed"

    # Case 2: Touching endpoints [1, 4] and [4, 5]
    assert solver.merge([[1, 4], [4, 5]]) == [[1, 5]], "Case 2 failed"

    # Case 3: Fully nested intervals
    assert solver.merge([[1, 10], [2, 3], [4, 5]]) == [[1, 10]], "Case 3 failed"

    # Case 4: Single interval
    assert solver.merge([[1, 5]]) == [[1, 5]], "Case 4 failed"

    # Case 5: Already disjoint intervals
    assert solver.merge([[1, 2], [3, 4], [5, 6]]) == [[1, 2], [3, 4], [5, 6]], "Case 5 failed"

    print("All solution tests passed successfully!")


if __name__ == "__main__":
    test_merge_intervals()
