class Solution(object):
    def twoSum(self, nums, target):
        hold = set()
        ans = []
        for ind, num in enumerate(nums):
            if target - num in hold:
                ans.append(ind)
                break
            hold.add(num)
        for ind, num in enumerate(nums):
            if num == target - nums[ans[0]]:
                ans.append(ind)
                break
        return ans
       
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        