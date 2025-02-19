class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        ct = 0
        
        def color(row, col):
            if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]):
                return
            if grid[row][col] == "1":
                grid[row][col] = "2"
                color(row + 1, col)
                color(row - 1, col)
                color(row, col - 1)
                color(row, col + 1)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    
                    color(i,j)
                    ct += 1
        
            
        
        return ct