class Solution(object):
    def containsDuplicate(self, nums):
        seta = set()
        for a in nums:
            if a in seta:
                return True
            seta.add(a)
        return False

        """
        :type nums: List[int]
        :rtype: bool
        """
        