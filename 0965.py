# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        valset = set()
        
        def walk(x):
            valset.add(x.val)
            if x.left!=None:
                walk(x.left)
            if x.right!=None:
                walk(x.right)

        if root == None:
            return True
        walk(root)
        if len(valset) == 1:
            return True
        else:
            return False