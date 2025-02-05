class Solution(object):
    def doable(self,piles,h,k):
        time = 0
        pilez = piles[:]
        for i in range(len(pilez)):
            time = time + math.ceil(pilez[i] / k)
            if time > h:
                return False
        return True

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        a = 1
        b = max(piles)
        

        while a <= b:
            m = (a + b)//2
            print("M:", m)
            print("A:", a, " B:", b)
            if self.doable(piles,h,m):
                b = m -1
            else:
                a = m + 1
    
        return a 
