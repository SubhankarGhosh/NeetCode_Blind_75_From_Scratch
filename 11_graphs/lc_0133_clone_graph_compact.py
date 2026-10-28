"""
LeetCode 133: Clone Graph
Module: 11_graphs
Difficulty: Medium
Tags: Hash Table, Depth-First Search, Breadth-First Search, Graph

PROBLEM DESCRIPTION:
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

Test case format:
An adjacency list is a collection of unordered lists used to represent a finite graph.
Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy
of the given node as a reference to the cloned graph.

Example 1:
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
    Explanation: There are 4 nodes in the graph.
    1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
    3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
    Input: adjList = [[]]
    Output: [[]]
    Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:
    Input: adjList = []
    Output: []
    Explanation: This an empty graph, it does not have any nodes.

Constraints:
    * The number of nodes in the graph is in the range [0, 100].
    * 1 <= Node.val <= 100
    * Node.val is unique for each node.
    * There are no repeated edges and no self-loops in the graph.
    * The Graph is connected and all nodes can be visited starting from the given node.
"""

from typing import Dict, List, Optional

TODO = None


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        """
        Creates a deep copy of the undirected graph using DFS / Hash Map.

        Time Complexity:  O(V + E) where V is vertices and E is edges
        Space Complexity: O(V) for the hash map and recursion stack
        """
        if not node:
            return None

        old_to_new: Dict[Node, Node] = {}

        def dfs(curr: Node) -> Node:
            if curr in old_to_new:
                # Active Learning: Return already cloned counterpart to prevent infinite recursion
                return old_to_new[curr]

            # TODO: Create a new clone of curr
            # TODO: Register it in old_to_new
            # TODO: Recursively clone and populate clone.neighbors
            clone = Node(curr.val)
            old_to_new[curr] = clone
            for neighbor in curr.neighbors:
                # clone.neighbors.append(...)
                pass

            return clone

        return dfs(node)


def build_graph(adj_list: List[List[int]]) -> Optional[Node]:
    """Helper to reconstruct a graph from LeetCode 1-indexed adjacency list."""
    if not adj_list:
        return None

    n = len(adj_list)
    nodes = {i + 1: Node(i + 1) for i in range(n)}
    for i, neighbors in enumerate(adj_list):
        u = i + 1
        nodes[u].neighbors = [nodes[v] for v in neighbors]

    return nodes[1]


def graph_to_adj(node: Optional[Node]) -> List[List[int]]:
    """Helper to serialize a graph to 1-indexed adjacency list."""
    if not node:
        return []

    visited = {}

    def dfs(curr: Node):
        visited[curr.val] = curr
        for neighbor in curr.neighbors:
            if neighbor.val not in visited:
                dfs(neighbor)

    dfs(node)
    adj_list = []
    for val in sorted(visited.keys()):
        adj_list.append([nbr.val for nbr in visited[val].neighbors])
    return adj_list


def is_deep_copy(original: Optional[Node], clone: Optional[Node]) -> bool:
    """Verifies that no nodes are shared in memory."""
    if not original and not clone:
        return True
    if not original or not clone:
        return False

    orig_nodes = set()
    stack = [original]
    while stack:
        curr = stack.pop()
        if curr not in orig_nodes:
            orig_nodes.add(curr)
            stack.extend(curr.neighbors)

    clone_stack = [clone]
    clone_nodes = set()
    while clone_stack:
        curr = clone_stack.pop()
        if curr in orig_nodes:
            return False  # Shared memory pointer detected!
        if curr not in clone_nodes:
            clone_nodes.add(curr)
            clone_stack.extend(curr.neighbors)

    return len(orig_nodes) == len(clone_nodes)


def test_clone_graph():
    solver = Solution()

    # Case 1: 4-node diamond graph
    adj1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
    g1 = build_graph(adj1)
    cloned1 = solver.cloneGraph(g1)
    assert graph_to_adj(cloned1) == adj1, "Case 1 topology failed"
    assert is_deep_copy(g1, cloned1), "Case 1 deep copy memory check failed"

    # Case 2: Single node
    adj2 = [[]]
    g2 = build_graph(adj2)
    cloned2 = solver.cloneGraph(g2)
    assert graph_to_adj(cloned2) == [[]], "Case 2 topology failed"
    assert is_deep_copy(g2, cloned2), "Case 2 deep copy memory check failed"

    # Case 3: Empty graph
    cloned3 = solver.cloneGraph(None)
    assert cloned3 is None, "Case 3 failed"

    # Case 4: 2 connected nodes
    adj4 = [[2], [1]]
    g4 = build_graph(adj4)
    cloned4 = solver.cloneGraph(g4)
    assert graph_to_adj(cloned4) == adj4, "Case 4 topology failed"
    assert is_deep_copy(g4, cloned4), "Case 4 deep copy memory check failed"

    print("All compact tests passed successfully!")


if __name__ == "__main__":
    test_clone_graph()
