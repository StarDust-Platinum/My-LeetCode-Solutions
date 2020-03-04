class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i = 0
        j = 1
        n = len(A)
        while i < n and j < n:
            if A[i] % 2 == 0:
                i += 2
            elif A[j] % 2 == 1:
                j += 2
            else:
                A[i], A[j] = A[j], A[i]
                i += 2
                j += 2
        return A