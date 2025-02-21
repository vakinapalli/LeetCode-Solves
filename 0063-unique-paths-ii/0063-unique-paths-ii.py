class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        currow = [0] * (n + 1)
        dummy = [0] * n
        currow[-1] = 1
        for i in range(m - 1,-1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    currow[j] = 0
                else:
                    currow[j] = currow[j + 1] + dummy[j]
            dummy = currow
            currow = [0] * (n + 1)
        return dummy[0]
