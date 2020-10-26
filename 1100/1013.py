class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s%3!=0:
            return False
        s = s//3
        n = len(A)
        sum_first_part = 0
        sum_second_part = 0
        for i in range(n):
            sum_first_part += A[i]
            if sum_first_part == s:
                for j in range(i+1, n):
                    sum_second_part += A[j]
                    if sum_second_part==s:
                        return True
                return False