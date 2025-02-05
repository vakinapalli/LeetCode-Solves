class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a = 0
        b = len(nums)-1

        while a <= b:
            mid = (a + b)//2

            if target > nums[mid]:
                a = mid + 1
            elif target < nums[mid]:
                b = mid - 1
            else:
                return mid
        
        
        return -1