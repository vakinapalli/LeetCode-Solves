class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        a = {}
        b = {}
        for i in target:
            a[i] = a.setdefault(i, 0) + 1
        for i in arr:
            b[i] = b.setdefault(i, 0) + 1
        for i in a:
            if a[i] != b.setdefault(i,0):
                return False
        return True            
