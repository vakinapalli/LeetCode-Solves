class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        hold = {}
        
        for num in arr1:
            hold[num] = hold.get(num, 0) + 1
            
                
        ans = []
        for num in arr2:
            while hold[num] > 0:
                ans.append(num)
                hold[num] -= 1
            del hold[num]
        for k in sorted(hold.keys()):
            while hold[k] > 0:
                ans.append(k)
                hold[k] -= 1
        return ans
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        