class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        D = {}
        for i in arr:
            if i not in D.keys():
                D[i] = 0
            else:
                D[i] += 1
        return len(set(D.values())) == len(D.values()):
