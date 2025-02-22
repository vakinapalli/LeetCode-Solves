class Solution:
    def countBits(self, n: int) -> List[int]:
        hold = [0] * (n+1)
        for i in range(n + 1):
            ct = 0
            nt = i
            while(nt != 0):
                if nt & 1:
                    ct += 1
                nt = nt >> 1
            hold[i] = ct
        return hold