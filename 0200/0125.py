class Solution:
    def isPalindrome(self, s: str) -> bool:
        A = []
        for i in range(48,58):
            A.append(chr(i))
        for i in range(65,91):
            A.append(chr(i))
            A.append(chr(i+32))
        t = ''
        for c in s:
            if c in A:
                t+=c
        t = t.lower()
        return t==t[::-1]