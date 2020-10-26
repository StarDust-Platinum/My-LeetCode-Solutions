class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        if n<=2:
            return True
        increase = True
        decrease = True
        for i in range(n-1):
            if A[i]>A[i+1]:
                increase = False
            elif A[i]<A[i+1]:
                decrease = False
        if increase or decrease:
            return True
        else:
            return False
            