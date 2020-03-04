class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A)
        i = 0
        j = n-1
        while True:
            while A[i]%2 == 0:
                i += 1
                if i == n:
                    break
            while A[j]%2 != 0:
                j -= 1
                if j == -1:
                    break
            if i>=j:
                break
            A[i], A[j] = A[j],A[i]
            i += 1
            j -= 1
        return A