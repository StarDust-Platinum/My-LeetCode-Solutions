class Solution:
    def judgeCircle(self, moves: str) -> bool:
        D= {}
        D['L'] = 0
        D['R'] = 0
        D['U'] = 0
        D['D'] = 0
        for c in moves:
            D[c]+=1
        if D['L']==D['R'] and D['U']==D['D']:
            return True
        else:
            return False