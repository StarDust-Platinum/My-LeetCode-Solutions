class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        n = len(nums)//2
        for key in c.keys():
            if c[key]>n:
                return key