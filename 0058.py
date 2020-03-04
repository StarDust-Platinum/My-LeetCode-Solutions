class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sp = s.split()
        if len(sp)==0:
            return 0
        return len(sp[-1])