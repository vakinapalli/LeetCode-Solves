class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = (10**9) + 7

        dp = [0] * (26 + t)
        for i in range(26):
            dp[i] = 1
        for i in range(26, t + 26):
            dp[i] = (dp[i-26] + dp[i-25]) % mod
        
        ans = 0
        for char in s:
             ans += (dp[ord(char) - ord('a') + t]) % mod
        return ans % mod