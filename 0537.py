class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        ar = int(a.split('+')[0])
        ac = int(a.split('+')[1][:-1])
        br = int(b.split('+')[0])
        bc = int(b.split('+')[1][:-1])
        return str(ar*br-ac*bc) + '+' + str(ar*bc+ac*br) + 'i'