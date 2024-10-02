class Solution(object):
    def __init__(self):
        self.hold = [0]
    def recur(self, n):
        if n == 1 or n == 2 or n == 3:
            return n
        if self.hold[n] != 0:
            return self.hold[n]
        a = self.recur(n-1)
        b = self.recur(n-2)
        self.hold[n-1] = a
        self.hold[n-2] = b
        return a + b 
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.hold = [0] * (n + 1)
        return self.recur(n)
        