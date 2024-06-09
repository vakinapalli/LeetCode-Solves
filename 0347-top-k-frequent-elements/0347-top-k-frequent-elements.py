class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1
        ar = [[] for _ in range((len(nums) + 1))]
        ans = []
        #sorteddict = sorted(freq.items(), key = lambda item: item[1], reverse = True)
        for a in freq:
            print(a, "len", len(ar))
            
            ar[freq[a]].append(a)
        
        for i in range(len(nums), 0, -1):
            if ar[i]:
                for elem in ar[i]:
                    ans.append(elem)
                    k -= 1
                    if k == 0: 
                        break
                if k == 0:
                    break
        return ans

            
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        