# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = n
        m = n
        while guess(m) != 0:
            m = (a+b)//2
            if guess(m) == -1:
                b = m -1
            elif guess(m) == 1:
                a = m + 1
        return m