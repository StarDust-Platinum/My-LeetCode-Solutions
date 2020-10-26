class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        count = collections.Counter(nums)
        for key in count.keys():
            if count[key]==1:
                res.append(key)
        return res