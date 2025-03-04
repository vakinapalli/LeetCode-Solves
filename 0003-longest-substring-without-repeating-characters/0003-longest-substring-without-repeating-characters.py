class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = 0
        hold = set()

        lngth = 0
        for i in range(len(s)):
            while s[i] in hold:
                hold.remove(s[a])
                a += 1
            hold.add(s[i])
            lngth = max(len(hold), lngth)
        return lngth