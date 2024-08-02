class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        ans = 0
        for i in details:
            if int(i[11:13]) > 60:
                ans +=1
        return ans