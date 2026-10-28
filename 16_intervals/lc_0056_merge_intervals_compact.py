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

TODO = None


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merges overlapping intervals by sorting by start time.

        Time Complexity:  O(N log N)
        Space Complexity: O(N) output array
        """
        if not intervals:
            return []

        # Active Learning:
        # Sort intervals by their start time
        intervals.sort(key=lambda x: x[0])

        merged: List[List[int]] = [intervals[0]]

        for current in intervals[1:]:
            last_end = merged[-1][1]
            curr_start, curr_end = current

            # TODO: If current interval overlaps with last interval in merged
            # (curr_start <= last_end), merge them by updating merged[-1][1]
            if curr_start <= last_end:
                merged[-1][1] = max(last_end, curr_end)
            else:
                # TODO: Otherwise, append current as a new disjoint interval
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

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_merge_intervals()
