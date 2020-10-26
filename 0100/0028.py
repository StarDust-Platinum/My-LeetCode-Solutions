class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        if haystack[:n]==needle:
            return 0
        s = haystack.split(needle)
        if len(s)>1:
            return len(s[0])
        elif haystack[-n:]==needle:
            return len(haystack)-n
        else:
            return -1