# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def tree_sum(x, L, R, l):
            if x != None:
                if x.val>=L and x.val<=R:
                    l.append(x.val)
                tree_sum(x.left, L, R, l)
                tree_sum(x.right, L, R, l)
        
        l = []
        tree_sum(root, L, R, l)
        return sum(l)