class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                k += 1
        
        L = 0
        R = len(nums) - 1
        for i in range(k):
            if nums[i] == val:
                while nums[R] == val:
                    R -= 1
                nums[i] = nums[R]
                nums[R] = val
            

        return k
