# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def plant(A):
            l = len(A)
            root = TreeNode(A[l//2])
            if l>1:
                root.left = plant(A[:l//2])
            if l>2:
                root.right = plant(A[l//2+1:])
            return root
        
        if len(nums)==0:
            return None
        return plant(nums)