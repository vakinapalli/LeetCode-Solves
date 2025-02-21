class Solution:
    def check(self, str1, str2):
        if str1 == str2:
            return 1
        return 0

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        matr = [[0] * len(text2) for i in range(len(text1))]
        for i in range(len(text2)):
            if i == 0:
                matr[0][i] = self.check(text1[0],text2[0])
            else:
                matr[0][i] = max(matr[0][i-1],self.check(text1[0], text2[i]))
        for i in range(len(text1)):
            if i == 0:
                matr[i][0] = self.check(text1[0],text2[0])
            else:
                matr[i][0] = max(matr[i-1][0],self.check(text1[i], text2[0]))
        
        for i in range(1, len(matr)):
            for j in range(1, len(matr[0])):
                matr[i][j] = max(matr[i-1][j], matr[i][j-1], matr[i-1][j-1] + self.check(text1[i],text2[j]))
        return matr[-1][-1]