class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapp = dict()
        mapp[0] = 1
        ct = 0
        cursum = 0
        for i in nums:
            cursum += i
            dif = cursum - k
            ct += mapp.get(dif, 0)
            mapp[cursum] = mapp.get(cursum, 0) + 1
        return ct