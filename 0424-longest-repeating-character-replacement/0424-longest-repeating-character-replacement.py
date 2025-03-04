class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqmap = dict()
        a = 0
        lnth = 0
        for i in range(len(s)):
            freqmap[s[i]] = freqmap.get(s[i],0) + 1
            while i - a + 1 -max(freqmap.values()) > k:
                freqmap[s[a]] -= 1
                a += 1
            lnth = max(lnth, i-a+1)
        return lnth
            
        