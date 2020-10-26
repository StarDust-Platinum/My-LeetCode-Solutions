class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ss = ''
        l = 0
        for i in range(int(len(s)/2)):
            ss = ss + s[i]
            l += 1
            if len(s)%l==0:
                if s == ss*(len(s)//l):
                    return True
        return False