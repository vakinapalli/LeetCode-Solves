class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minhp = [((i[0] ** 2) + (i[1] ** 2)) ** (1/2) for i in points]
        dic= dict()
        for i in range(len(minhp)):
           dic.setdefault(minhp[i], list()).append(points[i])
        heapq.heapify(minhp)
        ans = []
        for i in range(k):
            a = heapq.heappop(minhp)
            #print(a)
           # print(dic[a])
            ans.append(dic[a].pop())
        return ans