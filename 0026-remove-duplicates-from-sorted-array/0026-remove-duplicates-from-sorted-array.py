class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        L = 1
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[L] = nums[r]
                L += 1
        return L