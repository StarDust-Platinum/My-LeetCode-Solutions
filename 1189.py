class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        keys = ['b', 'a', 'l', 'o', 'n']
        count = collections.Counter(text)
        n = 10**4/7
        for key in keys:
            if key not in count.keys():
                return 0
            if key == 'l' or key=='o':
                if count[key]//2 < n:
                    n = count[key]//2
            elif count[key] < n:
                n = count[key]
        return n