class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
            else:
                if d[s[i]] != t[i]:
                    return False
        e = {}
        for i in range(len(t)):
            if t[i] not in e:
                e[t[i]] = s[i]
            else:
                if e[t[i]] != s[i]:
                    return False
        return True