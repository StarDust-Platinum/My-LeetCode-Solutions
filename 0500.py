class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        D = {"A":2,
             "a":2,
             "B":3,
             "b":3,
             "C":3,
             "c":3,
             "D":2,
             "d":2,
             "E":1,
             "e":1,
             "F":2,
             "f":2,
             "G":2,
             "g":2,
             "H":2,
             "h":2,
             "I":1,
             "i":1,
             "J":2,
             "j":2,
             "K":2,
             "k":2,
             "L":2,
             "l":2,
             "M":3,
             "m":3,
             "N":3,
             "n":3,
             "O":1,
             "o":1,
             "P":1,
             "p":1,
             "Q":1,
             "q":1,
             "R":1,
             "r":1,
             "S":2,
             "s":2,
             "T":1,
             "t":1,
             "U":1,
             "u":1,
             "V":3,
             "v":3,
             "W":1,
             "w":1,
             "X":3,
             "x":3,
             "Y":1,
             "y":1,
             "Z":3,
             "z":3
        }
        rt = []
        for i in words:
            ln = []
            for j in i:
                if D[j] not in ln:
                    ln.append(D[j])
            if len(ln) == 1:
                rt.append(i)
        return rt