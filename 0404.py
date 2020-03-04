# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = [0]
        
        def walk(x):
            if x.left:
                if x.left.left == None and x.left.right == None:
                    ans[0] += x.left.val
                else:
                    walk(x.left)
            if x.right:
                walk(x.right)
                
        if not root:
            return 0
        walk(root)
        return ans[0]