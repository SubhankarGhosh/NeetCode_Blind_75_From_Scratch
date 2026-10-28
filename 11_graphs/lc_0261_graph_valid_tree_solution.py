"""
LeetCode 261 / LintCode 178: Graph Valid Tree
Module: 11_graphs
Difficulty: Medium
Tags: Depth-First Search, Breadth-First Search, Union-Find, Graph

PROBLEM DESCRIPTION:
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a
pair of nodes), write a function to check whether these edges make up a valid tree.

A valid undirected graph is a tree if and only if:
1. It is fully connected (every node is reachable from any other node).
2. It contains no cycles.

Example 1:
    Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
    Output: true

Example 2:
    Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
    Output: false
    Explanation: The edges [1,2], [2,3], [1,3] form a 3-cycle.

Constraints:
    * 1 <= n <= 2000
    * 0 <= edges.length <= 5000
    * edges[i].length == 2
    * 0 <= ai, bi < n
    * ai != bi
    * There are no self-loops or repeated edges.
"""

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Validates tree properties using Disjoint Set Union (Union-Find) with path compression and rank.

        Mathematical Property:
        For any undirected graph G = (V, E) where |V| = n:
        - If |E| != n - 1, G cannot be a tree.
        - If |E| == n - 1, then: G is connected <=> G is acyclic <=> G is a tree.
        Hence, after the O(1) edge count check |E| == n - 1, checking acyclicity via
        Union-Find guarantees that the graph is a tree.

        Time Complexity:  O(V + E * alpha(V)) where alpha is the Inverse Ackermann function (effectively O(V + E)).
        Space Complexity: O(V) for the parent and rank arrays.
        """
        if len(edges) != n - 1:
            return False

        parent = list(range(n))
        rank = [1] * n
        components = n

        def find(node: int) -> int:
            curr = node
            while curr != parent[curr]:
                parent[curr] = parent[parent[curr]]  # Path halving / compression
                curr = parent[curr]
            return curr

        def union(u: int, v: int) -> bool:
            nonlocal components
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return False  # Both vertices already in the same set -> cycle detected

            if rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            elif rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            else:
                parent[root_v] = root_u
                rank[root_u] += 1

            components -= 1
            return True

        for u, v in edges:
            if not union(u, v):
                return False

        return components == 1


def test_graph_valid_tree():
    solver = Solution()

    # Case 1: Valid tree (5 nodes, 4 edges, star-like)
    assert solver.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True, "Case 1 failed"

    # Case 2: Graph with cycle (5 nodes, 5 edges)
    assert (
        solver.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) is False
    ), "Case 2 failed"

    # Case 3: Disconnected graph with n - 1 edges (triangle + isolated node)
    # 4 nodes, 3 edges: cycle 0-1-2-0 and node 3 isolated
    assert solver.validTree(4, [[0, 1], [1, 2], [2, 0]]) is False, "Case 3 failed"

    # Case 4: Single isolated node (vacuously a tree)
    assert solver.validTree(1, []) is True, "Case 4 failed"

    # Case 5: 2 nodes, 0 edges (disconnected)
    assert solver.validTree(2, []) is False, "Case 5 failed"

    # Case 6: Linear chain
    assert solver.validTree(3, [[0, 1], [1, 2]]) is True, "Case 6 failed"

    print("All solution tests passed successfully!")


if __name__ == "__main__":
    test_graph_valid_tree()
