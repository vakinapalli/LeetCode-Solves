class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hold = {}
        ans = []
        for i in range(len(nums)):
            if target - nums[i] in hold:
                ans.append(i)
                ans.append(hold[target - nums[i]])
                break
            else:
                hold[nums[i]] = i
        return ans
    
