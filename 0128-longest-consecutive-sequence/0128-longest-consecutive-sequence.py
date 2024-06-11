class Solution(object):
    def longestConsecutive(self, nums):
        init = set(nums)
        top = 0
        for num in nums:
            if num + 1 in init:
                continue
            hold = num
            curr = 1
            while hold - 1 in init:
                hold -= 1
                curr += 1
            top = max(curr, top)
        return top



        """
        :type nums: List[int]
        :rtype: int
        """
        