"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def cloneGraph(self, node):
        if node is None:
            return None

        clones = {}

        def dfs(node):
            if node in clones:
                return clones[node]

            copy = Node(node.val)
            clones[node] = copy

            for neighbor in node.neighbors:
                neighbor_copy = dfs(neighbor)
                copy.neighbors.append(neighbor_copy)

            return copy

        return dfs(node)