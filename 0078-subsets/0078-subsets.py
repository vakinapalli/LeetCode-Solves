class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        p = []
        def rpt(ph, it):
            #print(ph)
            ans.append(list(ph))
            a = list(ph)
            #print(a)
            for i in range(it,len(nums)):
                if nums[i] not in a:
                    a.append(nums[i])
                    print(a)
                    rpt(a, i + 1)
                    a.pop()
        rpt(p, 0)
        return ans
        
        
