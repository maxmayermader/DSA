class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDist(x1, y1, x2=0, y2=0):
            return math.sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))

        #distance, cord
        closest = []

        for cord in points:
            dist = getDist(cord[0], cord[1])
            n = [dist, cord]
            heapq.heappush(closest, n)

            res= []
        
        for i in range(k):
            res.append(heapq.heappop(closest)[1])
            


        return res


        