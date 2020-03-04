class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls += 1
        c1 = collections.Counter(secret)
        c2 = collections.Counter(guess)
        for key in c1.keys():
            if key in c2.keys():
                cows += min(c1[key],c2[key])
        cows -= bulls
        return "%sA%sB"%(bulls, cows)