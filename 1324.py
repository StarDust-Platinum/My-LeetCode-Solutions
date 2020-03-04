class Solution:
    def printVertically(self, s: str) -> List[str]:
        sp = s.split()
        m = len(sp)
        n = max(len(x) for x in sp)
        res = []
        r = ''
        for i in range(n):
            for j in range(m):
                if len(sp[j])>i:
                    r += sp[j][i]
                else:
                    r += ' '
            while r[-1]==' ':
                r = r[:-1]
            res.append(r)
            r = ''
        return res