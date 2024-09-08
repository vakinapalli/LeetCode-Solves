class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        hold = {}
        ans = []
        for i in strs:
            hold.setdefault("".join(sorted(i)), []).append(i)
        
        ans = [hold[i] for i in hold]
        return ans
