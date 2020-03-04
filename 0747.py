class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        A = sorted(nums)
        if A[-1]>=2*A[-2]:
            return nums.index(A[-1])
        else:
            return -1