class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c=collections.Counter(nums)
        for k in c.keys():
            if c[k]==1:
                return k