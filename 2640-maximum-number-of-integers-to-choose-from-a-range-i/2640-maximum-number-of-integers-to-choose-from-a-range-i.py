class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        curSum = 0
        
        banned = set(banned)

        ans = 0

        for i in range(1, n + 1):
            if i in banned:
                continue

            if curSum + i <= maxSum:
                curSum += i
                ans += 1
            elif curSum + 1 > maxSum:
                break

        return ans
            
