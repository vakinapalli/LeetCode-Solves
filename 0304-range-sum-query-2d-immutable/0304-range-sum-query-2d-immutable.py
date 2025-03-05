class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matpre = [([0] * len(matrix[0])) for i in range(len(matrix))]
        summ = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                summ = summ + matrix[i][j] 
                self.matpre[i][j] = summ

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1,row2 + 1):
            
            if col1 == 0 and i > 0:
                ans += self.matpre[i][col2] - self.matpre[i-1][-1]
            elif col1 == 0 and i == 0:
                ans += self.matpre[i][col2]
            else:
                
                ans += self.matpre[i][col2] - self.matpre[i][col1-1]
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)