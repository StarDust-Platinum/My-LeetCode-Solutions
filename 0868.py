class Solution:
    def binaryGap(self, N: int) -> int:
        b = bin(N)
        sp = b[2:].split('1')
        if len(sp)<=2:
            return 0
        if b[-1] == '0':
            return max([len(s) for s in sp[:-1]])+1
        else:
            return max([len(s) for s in sp])+1