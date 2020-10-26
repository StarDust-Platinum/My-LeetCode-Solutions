# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        res1 = set()
        res2 = set()
        
        def dfs(x, s, res):
            s = s + str(x.val)
            print(s)
            if x.left:
                dfs(x.left, s, res)
            if x.right:
                dfs(x.right, s, res)
            if not x.left and not x.right:
                res.add(s)
        
        if not root1 or not root2: 
            return root1 == root2
        else:
            dfs(root1, '', res1)
            dfs(root2, '', res2)
            return res1==res2
