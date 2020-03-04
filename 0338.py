class Solution:
    def countBits(self, num: int) -> List[int]:
        return [collections.Counter(bin(x)[2:])['1'] if '1' in collections.Counter(bin(x)[2:]).keys() else 0 for x in range(num+1)]