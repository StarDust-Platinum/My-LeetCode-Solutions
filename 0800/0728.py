class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        r = []
        for i in range(left, right+1):
            b = 1
            for c in str(i):
                if c=='0':
                    b = 0
                    break
                if i%int(c)!=0:
                    b = 0
                    break
            if b:
                r.append(i)
        return r