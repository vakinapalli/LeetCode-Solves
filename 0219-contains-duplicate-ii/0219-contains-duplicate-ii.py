class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return False
        if len(nums) == 2 and nums[0] != nums[1]:
            return False
        a = 0
        b = a + k
        hold = set()
        for i in range(0,min(len(nums),b+1)):
            if nums[i] in hold:
                return True
            hold.add(nums[i])
        for i in range(b+1, len(nums)):
            hold.remove(nums[a])
            if nums[i] in hold:
                return True
            hold.add(nums[i])
            a += 1
        return False
