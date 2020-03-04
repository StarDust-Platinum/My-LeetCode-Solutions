class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        n = len(A)
        D = {}
        for i in range(int(n/2)+2):
            if A[i] in D.keys():
                return A[i]
            else:
                D[A[i]] = 1