# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        res = []
        
        def walk(x, depth):
            if len(res)<depth:
                res.append(x.val)
            else:
                res[depth-1] += x.val
            if x.left:
                walk(x.left, depth+1)
            if x.right:
                walk(x.right, depth+1)
                
        if not root:
            return 0
        else:
            walk(root, 1)
            return res[-1]