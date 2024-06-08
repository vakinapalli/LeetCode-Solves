class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1
        ans = []
        sorteddict = sorted(freq.items(), key = lambda item: item[1], reverse = True)
        
        ans = [item[0] for item in sorteddict[0:k]]
        return ans

            
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        