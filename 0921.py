class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        res = []
        for c in S:
            if c == '(':
                res.append(c)
            else:
                if len(res)==0 or res[-1]==')':
                    res.append(c)
                else:
                    res.pop()
        return len(res)