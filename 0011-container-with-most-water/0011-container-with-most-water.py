class Solution:
    def maxArea(self, height: List[int]) -> int:
        a = 0
        b = len(height) - 1
        ht = 0
        while a < b:
            ht = max(ht, (b-a) * min(height[b], height[a]))
            if height[a] < height[b]:
                a+=1
            else:
                b-=1
        return ht
