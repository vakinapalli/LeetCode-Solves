class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxi = nums[0]
        mini = nums[0]
        curmax = 0
        curmin = 0
        sum = 0
        for i in nums:
            sum += i
            curmax = max(0,curmax)
            curmax += i
            maxi = max(curmax, maxi)

            curmin = min(0, curmin)
            curmin += i
            mini = min(curmin, mini)
        if sum != mini: 
            return max(maxi, sum - mini)
        return maxi