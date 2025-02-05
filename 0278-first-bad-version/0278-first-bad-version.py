# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        a = 1
        b = n

        while a <= b:
            m = (a + b) // 2
            if isBadVersion(m):
                b = m - 1
            else:
                a = m + 1
        return a
        