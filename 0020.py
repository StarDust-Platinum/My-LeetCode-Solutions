class Solution:
    def isValid(self, s: str) -> bool:
        A = []
        d = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in d.values():
                A.append(c)
            if c in d.keys():
                if len(A)==0:
                    return False
                x = A.pop()
                if x != d[c]:
                    return False
        if len(A)==0:
            return True
        else:
            return False