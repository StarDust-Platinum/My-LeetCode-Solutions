# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        def merge(x, y):
            x.val += y.val
            if x.left != None:
                if y.left != None:
                    merge(x.left, y.left)
            elif y.left != None:
                x.left = y.left
            if x.right != None:
                if y.right != None:
                    merge(x.right, y.right)
            elif y.right != None:
                x.right = y.right
        
        if t1==None:
            if t2==None:
                return None
            else:
                return t2
        elif t2==None:
            return t1
        
        merge(t1, t2)
        return t1