class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        n = 1
        ans = ""
        while True:
            if l1%n==0 and l2%n==0:
                if str1[:n]*(l1//n)==str1 and str1[:n]*(l2//n)==str2:
                    ans = str1[:n]
            n += 1
            if n>l1 or n>l2:
                break
        return ans