class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        b = bin(num)[2:]
        if b[0]=='1' and '1' not in b[1:] and len(b[1:])%2==0:
            return True
        else:
            return False