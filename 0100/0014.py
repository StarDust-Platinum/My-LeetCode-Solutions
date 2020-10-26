class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        n = 0
        mn = min([len(s) for s in strs])
        while len(set([s[:n] for s in strs]))==1:
            if n==mn:
                return strs[0][:n]
            n += 1
        return strs[0][:n-1]