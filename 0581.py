class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        if all(is_same):
            return 0
        else:
            return len(nums) - is_same.index(False) - is_same[::-1].index(False)