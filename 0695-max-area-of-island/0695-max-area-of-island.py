class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        trck = [0]

        def color(i,j):
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]):
                return
            if grid[i][j] == 1:
                trck[0] += 1
                grid[i][j] = 2
                color(i + 1, j)
                color(i - 1, j)
                color(i, j + 1)
                color(i, j - 1)

        maxim = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:

                    color(i,j)
                    maxim = max(maxim, trck[0])
                    trck[0] = 0
        return maxim