class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        res = []
        ac = collections.Counter(A.split())
        bc = collections.Counter(B.split())
        for key in ac.keys():
            if ac[key] == 1:
                if key not in bc.keys():
                    res.append(key)
        for key in bc.keys():
            if bc[key] == 1:
                if key not in ac.keys():
                    res.append(key)
        return res