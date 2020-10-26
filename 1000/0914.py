class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
        
        if len(deck)<2:
            return False
        c = collections.Counter(deck)
        n = min(c.values())
        for key in c.keys():
            if gcd(c[key], n) < 2:
                return False
        return True