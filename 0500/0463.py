class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        su = 0
        ma = float('-inf')
        for i, x in enumerate(nums):
            su += x
            if i >= k:
                su -= nums[i-k]
            if i >= k - 1:
                ma = max(ma, su)
        return ma / float(k)