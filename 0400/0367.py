class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        h = num
        mid = (l+h)//2
        while True:
            n = mid**2
            if n==num:
                return True
            elif n>num:
                h = mid
                mid = (l+h)//2
            else:
                l = mid
                mid = (l+h)//2
            if l==mid:
                return False