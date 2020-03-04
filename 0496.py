class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        D = {i:-1 for i in nums1}
        n = len(nums2)
        for i in range(n):
            if nums2[i] in D.keys():
                for j in range(i+1, n):
                    if nums2[j]>nums2[i]:
                        D[nums2[i]] = nums2[j]
                        break
        return [D[i] for i in nums1]