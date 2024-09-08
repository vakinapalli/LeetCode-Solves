class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        record = set()

        for i in range(len(nums)):
            if nums[i] in record:
                return True
            record.add(nums[i])

        return False

        