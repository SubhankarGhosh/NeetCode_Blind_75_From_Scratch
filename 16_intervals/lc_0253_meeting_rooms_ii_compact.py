"""
LeetCode 253 / LintCode 919: Meeting Rooms II
Module: 16_intervals
Difficulty: Medium
Tags: Array, Two Pointers, Greedy, Sorting, Heap (Priority Queue), Prefix Sum

PROBLEM DESCRIPTION:
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
return the minimum number of conference rooms required.

Example 1:
    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: 2
    Explanation:
    Room 1: [0, 30]
    Room 2: [5, 10], [15, 20]

Example 2:
    Input: intervals = [[7,10],[2,4]]
    Output: 1
    Explanation: Only one room is needed because [2,4] finishes before [7,10] starts.

Constraints:
    * 1 <= intervals.length <= 10^4
    * 0 <= starti < endi <= 10^6
"""

from typing import List

TODO = None


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Finds minimum rooms required using Chronological Two-Pointer Sweep-Line.

        Time Complexity:  O(N log N)
        Space Complexity: O(N)
        """
        if not intervals:
            return 0

        # Active Learning:
        # Separate and sort start times and end times independently
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])

        s_ptr = 0
        e_ptr = 0
        curr_rooms = 0
        max_rooms = 0

        while s_ptr < len(intervals):
            # TODO: If a meeting starts before the earliest ending meeting finishes,
            # we need a new room: increment curr_rooms and advance s_ptr
            if starts[s_ptr] < ends[e_ptr]:
                curr_rooms += 1
                s_ptr += 1
            else:
                # TODO: Otherwise, an ongoing meeting has ended: free a room and advance e_ptr
                curr_rooms -= 1
                e_ptr += 1

            max_rooms = max(max_rooms, curr_rooms)

        return max_rooms


def test_meeting_rooms_ii():
    solver = Solution()

    # Case 1: Standard 3 meetings [[0,30],[5,10],[15,20]] -> 2 rooms
    assert solver.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2, "Case 1 failed"

    # Case 2: 2 disjoint meetings [[7,10],[2,4]] -> 1 room
    assert solver.minMeetingRooms([[7, 10], [2, 4]]) == 1, "Case 2 failed"

    # Case 3: Empty intervals
    assert solver.minMeetingRooms([]) == 0, "Case 3 failed"

    # Case 4: Back-to-back meetings touching at boundary [[1, 5], [5, 10]] -> 1 room (can reuse)
    assert solver.minMeetingRooms([[1, 5], [5, 10]]) == 1, "Case 4 failed"

    # Case 5: 3 simultaneous overlapping meetings -> 3 rooms
    assert solver.minMeetingRooms([[1, 10], [2, 10], [3, 10]]) == 3, "Case 5 failed"

    # Case 6: Nested meetings [[1, 10], [2, 6], [3, 5], [7, 9]] -> 3 rooms
    assert solver.minMeetingRooms([[1, 10], [2, 6], [3, 5], [7, 9]]) == 3, "Case 6 failed"

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_meeting_rooms_ii()
