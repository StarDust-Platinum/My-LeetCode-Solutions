class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(grid, i, j, area, n):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != 1:
                return
            grid[i][j] = '#'
            area[n] += 1
            dfs(grid, i+1, j, area, n)
            dfs(grid, i-1, j, area, n)
            dfs(grid, i, j+1, area, n)
            dfs(grid, i, j-1, area, n)
        
        area = []
        n = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area.append(0)
                    n += 1
                    dfs(grid, i, j, area, n)
        if not area:
            return 0
        else:
            return max(area)