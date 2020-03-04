# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        
        def trim(x):
            while x.left!=None and x.left.val<L:
                if x.left.right == None:
                    x.left = None
                else:
                    x.left = x.left.right
            while x.right!=None and x.right.val>R:
                if x.right.left == None:
                    x.right = None
                else:
                    x.right = x.right.left
            if x.left!=None:
                trim(x.left)
            if x.right!=None:
                trim(x.right)
        
        if root == None:
            return        
        while root.val<L or root.val>R:
            if root.val<L:
                root = root.right
            else:
                root = root.left
            if root == None:
                return
        trim(root)
        return root