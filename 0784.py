class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        p = []
        ans = []
        for i in range(len(S)):
            if S[i].isalpha():
                p.append(i)
        for x in range(2**len(p)):
            res = ''
            k = '0'*(len(p)-len(bin(x)[2:]))+bin(x)[2:]
            i = 0
            for c in S:
                if c.isalpha():
                    if k[i]=='0':
                        res = res + c.lower()
                        i += 1
                    else:
                        res = res + c.upper()
                        i += 1
                else:
                    res = res + c
            ans.append(res)
        return ans