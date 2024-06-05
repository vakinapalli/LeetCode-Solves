class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        adic = {}
        bdic = {}

        for a,b in zip(s,t):
            if a not in adic:
                adic[a] = 0
            if b not in bdic:
                bdic[b] = 0
            bdic[b] = bdic[b] + 1
            adic[a] = adic[a] + 1
        for i in adic:
            if adic.get(i) != bdic.get(i):
                return False
        return True
            
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        