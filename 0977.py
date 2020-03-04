class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        i = 0
        j = n-1
        r = []
        while i<=j:
            if abs(A[i])>abs(A[j]):
                r.insert(0, A[i]**2)
                i += 1
            else:
                r.insert(0, A[j]**2)
                j -= 1
        return r