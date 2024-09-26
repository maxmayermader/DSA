class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def getDist(p1, p2):
            return abs(p2[1]-p1[1]) + abs(p2[0] - p1[0])
            
        N = len(points)
        # adj = collections.defaultdict(list)
        adj = {i:[] for i in range(N)}

        for i in range(N):
            p1 = points[i]
            for j in range(i+1, N):
                p2 = points[j]
                dist = getDist(p1, p2)
                adj[i].append((j, dist))
                adj[j].append((i, dist))

        pq = [(0, 0)]
        visit = set()
        t = 0

        while len(visit) < N:
            cost, point = heapq.heappop(pq)

            if point in visit:
                continue
            visit.add(point)
            t += cost

            for nei, neiCost in adj[point]:
                if nei not in visit:
                    heapq.heappush(pq, (neiCost, nei))


        # print(adj)

        return t
