class Solution(object):
    def sortColors(self, nums):
        freq = [0 for i in range(0,3)]
        for i in nums:
            freq[i] += 1
        hold = 0
        for i in range(len(freq)):
            for j in range(0,freq[i]):
                nums[hold] = i
                hold += 1
        
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        