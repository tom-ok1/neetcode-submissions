import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []

        for i in range(len(points)):
            distance = points[i][0] ** 2 + points[i][1] ** 2
            heapq.heappush(q, (distance, i))

        ans = []
        for _ in range(k):
            _, i = heapq.heappop(q)
            ans.append(points[i])

        return ans