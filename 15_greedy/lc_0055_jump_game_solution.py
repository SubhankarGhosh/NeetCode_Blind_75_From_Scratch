"""
LeetCode 55: Jump Game
Module: 15_greedy
Difficulty: Medium
Tags: Array, Dynamic Programming, Greedy

PROBLEM DESCRIPTION:
You are given an integer array nums. You are initially positioned at the array's first
index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum jump length
    is 0, which makes it impossible to reach the last index.

Constraints:
    * 1 <= nums.length <= 10^4
    * 0 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Determines if the last index is reachable using greedy goal shifting.

        Greedy Invariant:
        We maintain a `goal` index, initially set to the last position `len(nums) - 1`.
        Iterating backwards from right to left:
        - If position i has sufficient jump range to reach `goal` (i + nums[i] >= goal),
          then any path capable of reaching index i is guaranteed capable of reaching the end.
        - Therefore, we greedily relax the goal to `goal = i`.
        - If the goal reaches index 0, the destination is reachable from the starting point.

        Time Complexity:  O(N) - Single linear reverse pass.
        Space Complexity: O(1) - Single scalar pointer.
        """
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0


def test_can_jump():
    solver = Solution()

    # Case 1: Standard reachable array
    assert solver.canJump([2, 3, 1, 1, 4]) is True, "Case 1 failed"

    # Case 2: Trap zero at index 3
    assert solver.canJump([3, 2, 1, 0, 4]) is False, "Case 2 failed"

    # Case 3: Single element (already at last index)
    assert solver.canJump([0]) is True, "Case 3 failed"

    # Case 4: Zeros at end that are leapfrogged
    assert solver.canJump([2, 0, 0]) is True, "Case 4 failed"

    # Case 5: Large single jump from start
    assert solver.canJump([5, 0, 0, 0, 0]) is True, "Case 5 failed"

    # Case 6: Blocked at start
    assert solver.canJump([0, 2, 3]) is False, "Case 6 failed"

    print("All solution tests passed successfully!")


if __name__ == "__main__":
    test_can_jump()
