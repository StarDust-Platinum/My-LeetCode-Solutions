class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            if i+2>m-1:
                break
            for j in range(n):
                if j+2>n-1:
                    break
                nums = [grid[p][q] for p in range(i, i+3) for q in range(j, j+3) if grid[p][q]>=1 and grid[p][q]<=9]
                if len(set(nums))==9:
                    if nums[0]+nums[8]==nums[2]+nums[6]:
                        if nums[0]+nums[3]+nums[6]==nums[1]+nums[4]+nums[7] and  nums[0]+nums[3]+nums[6]==nums[2]+nums[5]+nums[8]:
                            if nums[0]+nums[1]+nums[2]==nums[3]+nums[4]+nums[5] and nums[0]+nums[1]+nums[2]==nums[6]+nums[7]+nums[8]:
                                count += 1
        return count