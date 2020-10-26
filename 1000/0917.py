class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        t = ''
        A = []
        for i in range(65,91):
            A.append(chr(i))
            A.append(chr(i+32))
        for c in S:
            if c in A:
                t = t + c
        t = t[::-1]
        n = 0
        St = list(S)
        for i in range(len(St)):
            if St[i] in A:
                St[i] = t[n]
                n += 1
        return ''.join(St)