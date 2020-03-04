class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        res = 0
        prime_set = (2,3,5,7,11,13,17,19)
        for i in range(L, R+1):
            count = 0
            for one in bin(i)[2:]:
                if one=='1':
                    count += 1
            if count in prime_set:
                res += 1
        return res