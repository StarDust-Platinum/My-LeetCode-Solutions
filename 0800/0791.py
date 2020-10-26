class Solution:
    def customSortString(self, S: str, T: str) -> str:
        def func(x):
            return D[x]
        
        D = dict()
        for i in range(len(S)):
            D[S[i]] = i 
        for i in range(len(T)):
            if T[i] not in D.keys():
                D[T[i]] = float('inf')
        return ''.join(sorted(T, key=func))