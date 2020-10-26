# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        dl = []
        
        def dfs(x, depth):
            if x.left==None and x.right==None:
                dl.append(depth)
            else:
                depth += 1
                if x.left:
                    dfs(x.left, depth)
                if x.right:
                    dfs(x.right, depth)
                
        if not root:
            return 0
        dfs(root, 1)
        return min(dl)