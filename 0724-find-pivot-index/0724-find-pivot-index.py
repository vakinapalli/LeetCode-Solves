class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        

        summ = 0
        prefix = list()
        prefix.append(0)
        for i in nums:
            summ += i
            prefix.append(summ)
        for i in range(1,len(nums) + 1):
            if prefix[i - 1] == prefix[-1] - prefix[i]:
                return i - 1

        if prefix[len(prefix) - 2] == 0: return len(nums) - 1
        return -1