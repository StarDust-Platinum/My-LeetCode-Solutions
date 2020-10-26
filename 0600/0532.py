class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k<0:
            return 0
        c = collections.Counter(nums)
        keys = c.keys()
        res = 0
        if k==0:
            for key in keys:
                if c[key]>1:
                    res += 1
            return res
        for key in keys:
            if key+k in keys:
                res += 1
        return res