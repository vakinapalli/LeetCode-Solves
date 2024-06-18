class Solution(object):
    def threeSum(self, nums):
        sort = sorted(nums)
        ans = []
        for i, num in enumerate(sort):
            if num > 0:
                break
            if i > 0 and num == sort[i-1]:
                continue
            low = i + 1
            high = len(sort) - 1
            su = 0
            while low < high:
                su = sort[low] + sort[high] + num
                if su > 0:
                    high -= 1
                elif su < 0:
                    low += 1
                else:
                    print(num, sort[low], sort[high])
                    ans.append([num, sort[low], sort[high]])
                    lowhold = sort[low]
                    highhold = sort[high]

                    while low < high and lowhold == sort[low]:
                        low += 1
                    while low < high and highhold == sort[high]:
                        high -= 1
        return ans

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        