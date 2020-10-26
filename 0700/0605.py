class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        A = ''.join([str(x) for x in flowerbed])
        if '1' not in A:
            return len(A)-len(A)//2>=n
        A = A.split('1')
        res = 0
        l = len(A)        
        for i in range(l):
            if i==0 or i==l-1:
                res += len(A[i])//2
            else:
                if len(A[i])%2==1:
                    res += len(A[i])//2
                else:
                    res += len(A[i])//2-1
        return res>=n