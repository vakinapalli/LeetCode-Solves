class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        currow = [0] * (n + 1)
        dummy = [0] * n
        currow[-1] = 1
        for i in range(m - 1,-1, -1):
            for j in range(n-1, -1, -1):
                currow[j] = currow[j + 1] + dummy[j]
            dummy = currow
            currow = [0] * (n + 1)
        return dummy[0]
