class Solution:
    dic = {}
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        if n in self.dic:
            return self.dic[n]
        
        self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]