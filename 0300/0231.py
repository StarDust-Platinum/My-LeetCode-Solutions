class Solution:
    def toLowerCase(self, str: str) -> str:
        rt = ''
        for i in str:
            n = ord(i)
            if n>=65 and n<=90:
                rt += chr(n+32)
            else:
                rt += i
        return rt