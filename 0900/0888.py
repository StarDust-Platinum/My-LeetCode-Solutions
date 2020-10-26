class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        dif = (sum(B) - sum(A)) / 2
        B = set(B)
        for a in set(A):
            t = a+dif
            if t in B:
                return [a, t]