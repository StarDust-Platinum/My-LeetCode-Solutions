"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        def walk(x):
            res.append(x.val)
            for child in x.children:
                walk(child)
        
        if root == None:
            return None
        
        res = []
        walk(root)
        return res