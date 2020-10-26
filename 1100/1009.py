class Solution:
    def bitwiseComplement(self, N: int) -> int:
        ret = 0
        n = 0
        bn = bin(N)[2:][::-1] 
        for c in bn:
            if c == '1':
                a = 0
            else:
                a = 1
            ret += int(a)*2**n
            n +=1
        return ret