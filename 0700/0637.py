# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        d = dict()
        
        def search(x, level):
            if level not in d.keys():
                d[level] = [x.val, 1]
            else:
                d[level][0] = d[level][0] + x.val
                d[level][1] = d[level][1] + 1
            if x.left:
                search(x.left, level+1)
            if x.right:
                search(x.right, level+1)
        
        if not root:
            return []
        search(root, 1)
        res = []
        for key in d.keys():
            res.append(d[key][0]/d[key][1])
        return res