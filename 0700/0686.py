class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if A=="":
            return -1
        la = len(A)
        lb = len(B)
        n = lb//la+2
        for i in range(1, n+1):
            if B in A*i:
                return i
        else:
            return -1