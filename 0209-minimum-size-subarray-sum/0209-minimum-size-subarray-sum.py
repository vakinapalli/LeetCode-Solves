class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = 10 ** 6
        amt = 0
        l = r = 0

        for i in range(len(nums)):
            amt += nums[i]

            while amt >= target:
                length = min(length, i - l + 1)
                amt -= nums[l]
                l += 1
                



        if length == 10**6:
            return 0
        return length
        