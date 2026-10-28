"""
LeetCode 57: Insert Interval
Module: 16_intervals
Difficulty: Medium
Tags: Array

PROBLEM DESCRIPTION:
You are given an array of non-overlapping intervals `intervals` where
intervals[i] = [starti, endi] represent the start and the end of the ith interval
and intervals is sorted in ascending order by starti. You are also given an interval
newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending
order by starti and intervals still does not have any overlapping intervals
(merge overlapping intervals if necessary).

Return intervals after the insertion.
Note that you don't need to modify intervals in-place. You can make a new array and return it.

Example 1:
    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

Example 2:
    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
    * 0 <= intervals.length <= 10^4
    * intervals[i].length == 2
    * 0 <= starti <= endi <= 10^5
    * intervals is sorted by starti in ascending order.
    * newInterval.length == 2
    * 0 <= start <= end <= 10^5
"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Inserts and merges newInterval into sorted non-overlapping intervals in linear time.

        Three-Phase Invariant:
        1. Preceding Intervals: Any interval ending before newInterval starts (intervals[i][1] < newInterval[0])
           cannot overlap. Append directly.
        2. Overlapping Intervals: Any interval starting before or when newInterval ends
           (intervals[i][0] <= newInterval[1]) must overlap. Greedily expand newInterval boundaries:
           newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])].
        3. Trailing Intervals: Append the newly expanded newInterval, then append all remaining intervals.

        Time Complexity:  O(N) - Single pass over intervals array.
        Space Complexity: O(N) - Output list storage.
        """
        res: List[List[int]] = []
        i = 0
        n = len(intervals)

        # Phase 1: Preceding non-overlapping intervals
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Phase 2: Overlapping intervals merged into newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)

        # Phase 3: Trailing non-overlapping intervals
        while i < n:
            res.append(intervals[i])
            i += 1

        return res


def test_insert_interval():
    solver = Solution()

    # Case 1: Overlapping with single interval [[1,3],[6,9]], [2,5] -> [[1,5],[6,9]]
    assert solver.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]], "Case 1 failed"

    # Case 2: Overlapping multiple intervals
    intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    expected2 = [[1, 2], [3, 10], [12, 16]]
    assert solver.insert(intervals2, [4, 8]) == expected2, "Case 2 failed"

    # Case 3: Empty intervals
    assert solver.insert([], [5, 7]) == [[5, 7]], "Case 3 failed"

    # Case 4: Insert before all existing intervals
    assert solver.insert([[3, 5], [6, 9]], [1, 2]) == [[1, 2], [3, 5], [6, 9]], "Case 4 failed"

    # Case 5: Insert after all existing intervals
    assert solver.insert([[1, 2], [3, 5]], [6, 8]) == [[1, 2], [3, 5], [6, 8]], "Case 5 failed"

    # Case 6: Subsume all intervals
    assert solver.insert([[2, 3], [4, 5]], [1, 10]) == [[1, 10]], "Case 6 failed"

    print("All solution tests passed successfully!")


if __name__ == "__main__":
    test_insert_interval()
