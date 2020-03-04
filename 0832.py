class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        m = int(n/2)
        for i in range(n):
            for j in range(m):
                A[i][j], A[i][n-1-j] = A[i][n-1-j], A[i][j]
        for i in range(n):
            for j in range(n):
                if A[i][j] == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        return A