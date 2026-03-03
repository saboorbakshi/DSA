"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        start = node
        visited = set()
        hashmap = {}

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            hashmap[node] = Node(val=node.val)
            for neighbor in node.neighbors:
                dfs(neighbor)
        
        dfs(node)
        
        for node in hashmap:
            cloned_node = hashmap[node]
            for neighbor in node.neighbors:
                cloned_node.neighbors.append(hashmap[neighbor])
        
        return hashmap[start]



        