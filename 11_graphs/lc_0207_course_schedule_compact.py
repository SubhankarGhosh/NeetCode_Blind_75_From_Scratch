"""
LeetCode 207: Course Schedule
Module: 11_graphs
Difficulty: Medium
Tags: Depth-First Search, Breadth-First Search, Graph, Topological Sort

PROBLEM DESCRIPTION:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you
must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take.
    To take course 1 you should have finished course 0. So it is possible.

Example 2:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take.
    To take course 1 you should have finished course 0, and to take course 0 you should
    also have finished course 1. So it is impossible (cycle detected).

Constraints:
    * 1 <= numCourses <= 2000
    * 0 <= prerequisites.length <= 5000
    * prerequisites[i].length == 2
    * 0 <= ai, bi < numCourses
    * All the pairs prerequisites[i] are unique.
"""

from collections import deque
from typing import List

TODO = None


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determines if all courses can be finished using Kahn's Algorithm (BFS Topological Sort).

        Time Complexity:  O(V + E) where V = numCourses, E = len(prerequisites)
        Space Complexity: O(V + E) for the adjacency list and in-degree tracking
        """
        # Active Learning:
        # Step 1: Build adjacency list and compute in-degrees
        # Note: [course, prereq] -> prereq -> course (edge: b -> a)
        adj: List[List[int]] = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degrees[course] += 1

        # Step 2: Enqueue all nodes with in-degree 0 (courses with no prerequisites)
        queue = deque([node for node in range(numCourses) if in_degrees[node] == 0])
        processed_count = 0

        # Step 3: Process the queue
        while queue:
            curr = queue.popleft()
            processed_count += 1

            for neighbor in adj[curr]:
                # TODO: Decrement in_degrees[neighbor]
                # If in_degrees[neighbor] == 0, push to queue
                pass

        # TODO: Return whether all courses could be processed without encountering a cycle
        return processed_count == numCourses


def test_course_schedule():
    solver = Solution()

    # Case 1: Simple linear dependency (0 -> 1)
    assert solver.canFinish(2, [[1, 0]]) is True, "Case 1 failed"

    # Case 2: 2-node cycle (0 -> 1 -> 0)
    assert solver.canFinish(2, [[1, 0], [0, 1]]) is False, "Case 2 failed"

    # Case 3: Disconnected components with no cycles
    assert solver.canFinish(4, [[1, 0], [3, 2]]) is True, "Case 3 failed"

    # Case 4: Diamond dependency graph (0 -> 1, 0 -> 2, 1 -> 3, 2 -> 3)
    assert solver.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) is True, "Case 4 failed"

    # Case 5: 3-node cycle inside a 5-node graph
    assert solver.canFinish(5, [[1, 0], [2, 1], [0, 2], [4, 3]]) is False, "Case 5 failed"

    # Case 6: No prerequisites at all
    assert solver.canFinish(3, []) is True, "Case 6 failed"

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_course_schedule()
