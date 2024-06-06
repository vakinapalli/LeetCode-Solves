class Solution(object):
    def twoSum(self, nums, target):
        hold = {}
        
        for ind, num in enumerate(nums):
            if target - num in hold:
                return [ind, hold[target-num]]
                
            hold[num] = ind
        
       
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        