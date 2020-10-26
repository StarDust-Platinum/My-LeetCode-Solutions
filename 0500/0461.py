class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xb = bin(x)[2:]
        yb = bin(y)[2:]
        d = len(xb)-len(yb)
        if d>0:
            yb = '0'*d+yb
        else:
            xb = '0'*-d+xb
        ret = 0
        for i in range(len(xb)):
            if xb[i]!=yb[i]:
                ret += 1
        return ret