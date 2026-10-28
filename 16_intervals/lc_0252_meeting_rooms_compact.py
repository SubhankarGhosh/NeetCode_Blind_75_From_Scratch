"""
LeetCode 252 / LintCode 920: Meeting Rooms
Module: 16_intervals
Difficulty: Easy
Tags: Array, Sorting

PROBLEM DESCRIPTION:
Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.

Example 1:
    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: false
    Explanation: The person cannot attend meeting [0,30] and [5,10] at the same time.

Example 2:
    Input: intervals = [[7,10],[2,4]]
    Output: true
    Explanation: Since [2,4] finishes before [7,10] starts, the person can attend both.

Constraints:
    * 0 <= intervals.length <= 10^4
    * intervals[i].length == 2
    * 0 <= starti < endi <= 10^6
"""

from typing import List

TODO = None


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Determines if any meetings conflict by sorting by start time.

        Time Complexity:  O(N log N)
        Space Complexity: O(1) auxiliary space
        """
        # Active Learning:
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        for i in range(len(intervals) - 1):
            # TODO: If current meeting ends AFTER next meeting starts, conflict occurs!
            # intervals[i][1] > intervals[i + 1][0]
            if intervals[i][1] > intervals[i + 1][0]:
                return False

        return True


def test_meeting_rooms():
    solver = Solution()

    # Case 1: Overlapping meetings [[0,30],[5,10],[15,20]] -> False
    assert solver.canAttendMeetings([[0, 30], [5, 10], [15, 20]]) is False, "Case 1 failed"

    # Case 2: Disjoint meetings [[7,10],[2,4]] -> True
    assert solver.canAttendMeetings([[7, 10], [2, 4]]) is True, "Case 2 failed"

    # Case 3: Empty intervals
    assert solver.canAttendMeetings([]) is True, "Case 3 failed"

    # Case 4: Back-to-back meetings touching at boundary [[1, 5], [5, 10]] -> True
    assert solver.canAttendMeetings([[1, 5], [5, 10]]) is True, "Case 4 failed"

    # Case 5: Single meeting
    assert solver.canAttendMeetings([[0, 100]]) is True, "Case 5 failed"

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_meeting_rooms()
