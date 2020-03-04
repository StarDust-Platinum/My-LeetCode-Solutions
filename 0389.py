class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        S = sorted(s)
        T = sorted(t)
        for i in range(len(S)):
            if S[i]!=T[i]:
                return T[i]
        return T[-1]