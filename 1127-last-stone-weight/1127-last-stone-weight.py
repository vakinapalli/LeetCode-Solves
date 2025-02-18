class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        for i in range(len(stones)):
            stones[i] = stones[i] * -1
        heapq.heapify(stones)
        while(len(stones) > 1):
            a = -1 * heapq.heappop(stones)
            b = -1* heapq.heappop(stones)
            if(abs(a - b)):
                heapq.heappush(stones, -1 * abs(a-b))
        if stones:
            return -1 * stones[0]
        return 0