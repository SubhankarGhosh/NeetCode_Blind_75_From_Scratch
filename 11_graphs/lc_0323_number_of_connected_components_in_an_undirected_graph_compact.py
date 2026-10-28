"""
LeetCode 323 / LintCode 591: Number of Connected Components in an Undirected Graph
Module: 11_graphs
Difficulty: Medium
Tags: Depth-First Search, Breadth-First Search, Union-Find, Graph

PROBLEM DESCRIPTION:
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and an array
`edges` where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Example 1:
    Input: n = 5, edges = [[0,1],[1,2],[3,4]]
    Output: 2
    Explanation:
        0 - 1 - 2       3 - 4
        There are 2 connected components.

Example 2:
    Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
    Output: 1
    Explanation:
        0 - 1 - 2 - 3 - 4
        All nodes are connected in a single component.

Constraints:
    * 1 <= n <= 2000
    * 1 <= edges.length <= 5000
    * edges[i].length == 2
    * 0 <= ai <= bi < n
    * ai != bi
    * There are no repeated edges.
"""

from typing import List

TODO = None


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Counts connected components in an undirected graph using Disjoint Set Union (DSU).

        Time Complexity:  O(V + E * alpha(V)) ≈ O(V + E)
        Space Complexity: O(V) for the parent and rank arrays
        """
        parent = list(range(n))
        rank = [1] * n
        components = n

        def find(node: int) -> int:
            # Active Learning: Path compression
            curr = node
            while curr != parent[curr]:
                parent[curr] = parent[parent[curr]]
                curr = parent[curr]
            return curr

        def union(u: int, v: int) -> bool:
            # Active Learning: Union by rank
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return False  # Already connected

            # TODO: Merge smaller tree into larger tree
            if rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            elif rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            else:
                parent[root_v] = root_u
                rank[root_u] += 1

            nonlocal components
            components -= 1
            return True

        for u, v in edges:
            union(u, v)

        return components


def test_count_components():
    solver = Solution()

    # Case 1: 2 components (0-1-2 and 3-4)
    assert solver.countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2, "Case 1 failed"

    # Case 2: 1 single component (linear chain)
    assert solver.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1, "Case 2 failed"

    # Case 3: Completely disconnected (5 isolated vertices)
    assert solver.countComponents(5, []) == 5, "Case 3 failed"

    # Case 4: Complete triangle + 2 isolated vertices
    assert solver.countComponents(5, [[0, 1], [1, 2], [2, 0]]) == 3, "Case 4 failed"

    # Case 5: Single node
    assert solver.countComponents(1, []) == 1, "Case 5 failed"

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_count_components()
