class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        k1 = c1.keys()
        k2 = c2.keys()
        for key in k1:
            if key not in k2:
                c1[key] = 0
            elif c2[key]<c1[key]:
                c1[key] = c2[key]
        for key in k1:
            ans = ans + [key]*c1[key]
        return ans