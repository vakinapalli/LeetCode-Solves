class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        if len(nums) is 1:
            return k
        repct = 0
        i = 1
        hold = len(nums)
        while i < hold:
            if nums[i] == nums[i-1]:
                repct += 1
                i += 1
            else:
                for j in range(i,hold):
                    nums[j-repct] = nums[j]

                k += 1
                i = i - repct + 1
                hold = hold - repct
                repct = 0


        
        return k

