class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [nums[i % len(nums)] for i in range(2 * len(nums))]
        return ans