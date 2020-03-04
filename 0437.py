# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        res = [0]
        
        def find(x, s):
            if x.val == s:
                res[0] += 1
            if x.left:
                find(x.left, s-x.val)
            if x.right:
                find(x.right, s-x.val)
                
        def walk(x):
            find(x, sum)
            if x.left:
                walk(x.left)
            if x.right:
                walk(x.right)
                
        if not root:
            return 0
        else:
            walk(root)
            return res[0]