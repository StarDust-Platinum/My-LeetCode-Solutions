class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A)<3:
            return False
        reachpeak = False
        for i in range(len(A)-1):
            if A[i]==A[i+1]:
                return False
            if not reachpeak and A[i+1]<A[i]:
                if i==0:
                    return False
                reachpeak = True
            if reachpeak and A[i+1]>A[i]:
                return False
        return reachpeak