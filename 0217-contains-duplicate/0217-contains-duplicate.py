class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        record = set(nums)
        return not len(record) == len(nums)

        