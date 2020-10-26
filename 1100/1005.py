class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        l = sorted(A)
        for i in range(len(l)):
            if l[i]<0 and K>0:
                l[i] = -l[i]
                K -= 1
        if K>0 and K%2==1:
            l.sort()
            l[0] = -l[0]
        return sum(l)