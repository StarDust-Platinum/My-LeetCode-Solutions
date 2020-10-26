class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:
            return False
        ans = 0
        SQRT = int(num ** 0.5)
        ans = sum(i + num//i for i in range(1, SQRT+1) if not num % i)
        if num == SQRT ** 2:
            ans -= SQRT
        return ans - num == num