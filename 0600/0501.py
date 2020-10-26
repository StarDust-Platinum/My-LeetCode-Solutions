# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        d = {}        
        
        def walk(x):
            if x.val not in d.keys():
                d[x.val] = 1
            else:
                d[x.val] += 1
            if x.left:
                walk(x.left)
            if x.right:
                walk(x.right)
        
        if not root:
            return None
        else:
            walk(root)
            mx = max(d.values())
            res = []
            for key in d.keys():
                if d[key]==mx:
                    res.append(key)
            return res