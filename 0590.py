"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root == None:
            return res

        def recursion(x, res):
            for child in x.children:
                recursion(child, res)
            res.append(x.val)

        recursion(root, res)
        return res

    def postorder_iter(self, root):
        res = []
        if root == None:
            return res

        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            stack.extend(curr.children)

        return res[::-1]