class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i:[] for i in range(n)}
        for node, nei, cost in flights:
            adj[node].append((cost, nei))

        pq = [(0, src, k+1)]
        visit = {}
        # totStops = k

        while pq:
            cost, node, stops = heapq.heappop(pq)

            if node == dst:
                return cost

            if stops > 0:
                if node not in visit or visit[node] < stops:
                    visit[node] = stops
                    for neiCost, nei in adj[node]:
                        heapq.heappush(pq, (cost+neiCost, nei, stops-1))

        return -1

