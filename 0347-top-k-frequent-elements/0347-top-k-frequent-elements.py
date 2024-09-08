class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        ct = [[] for i in range(len(nums) + 1)]
        for i in dic:
            ct[dic[i]].append(i)
        
        result = []
        i = len(nums)
        while k > 0:
            for j in ct[i]:
                result.append(j)
                k -= 1
                if k == 0:
                    break
            i -= 1
        return result
        