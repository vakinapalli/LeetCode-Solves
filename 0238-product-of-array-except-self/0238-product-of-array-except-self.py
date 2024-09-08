class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre = 1
        suf = 1
        ans = [1] * len(nums)
        for i in range(len(nums)):
            ans[i] *= pre
            pre *= nums[i]
            ans[len(nums) - 1 - i] *= suf
            suf *= nums[len(nums) - 1 - i]

        return ans

        