class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        """
        
        I THINK YOU SHOULD ROLL THE DIE AND BE GREEDY ABOUT THIS :)


        """

        time = 0

        # (time, (coords))
        pq = [(0, (0,0))]
        visited = set()
        visited.add((0,0))

        while pq:
            time, coord = heappop(pq)
            i, j = coord

            if coord == (len(moveTime) - 1, len(moveTime[0]) - 1):
                return time

            for i2, j2 in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if (i + i2, j + j2) not in visited and i + i2 < len(moveTime) and i + i2 > -1 and j + j2 < len(moveTime[0]) and j + j2 > -1:
                    heappush(pq, (max(time, moveTime[i+i2][j + j2]) + 1, (i+i2, j + j2)))
                    visited.add((i+i2, j+j2))
            