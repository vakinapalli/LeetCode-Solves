class Solution(object):
    def productExceptSelf(self, nums):
        pre = [0] * len(nums)
        suf = [0] * len(nums)
        pre[0] = 1
        suf[-1] = 1
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
            suf[len(nums) - 1 - i] = suf[len(nums) - i] * nums[len(nums) - i]
        ans = [pre[i] * suf[i] for i in range(len(nums))]
        print(pre)
        print(suf)
        return ans
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        