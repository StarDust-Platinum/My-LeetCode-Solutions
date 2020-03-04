class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chardict = {}
        for c in chars:
            if c not in chardict.keys():
                chardict[c]=1
            else:
                chardict[c]+=1
        count = 0
        for word in words:
            isGood = True
            D = chardict.copy()
            for c in word:
                if c not in D.keys():
                    isGood = False
                    break
                elif D[c]==0:
                    isGood =False
                    break
                else:
                    D[c] -= 1
            if isGood:
                count += len(word)
        return count