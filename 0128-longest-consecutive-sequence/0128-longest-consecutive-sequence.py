class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        top = 0
        ct = set(nums)
        for i in nums:
            if i - 1 in ct:
                continue
            p = i
            seq = 1
            while p + 1 in ct:
                 seq += 1
                 p += 1
            top = max(top, seq)

        return top
            