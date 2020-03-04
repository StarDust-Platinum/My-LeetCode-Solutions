class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits)==0:
            return None
        res = []
        n = digits.pop()
        if n == 9:
            carry = 1
            res.insert(0, 0)
        else:
            carry = 0
            res.insert(0, n+1)
        while len(digits)>0:
            n = digits.pop()+carry
            if n == 10:
                carry = 1
                res.insert(0, 0)
            else:
                carry = 0
                res.insert(0, n)
        if carry==1:
            res.insert(0, 1)
        return res