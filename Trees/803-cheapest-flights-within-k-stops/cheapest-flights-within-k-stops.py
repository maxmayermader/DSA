class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}
        for frm, to, price in flights:
            adj[frm].append((to, price))
        
        pq = [(0, src, k + 1)]
        visited = {}
        
        while pq:
            price, node, stops = heapq.heappop(pq)
            
            if node == dst:
                return price
            
            if stops > 0:
                if node not in visited or visited[node] < stops:
                    visited[node] = stops
                    for nei, cost in adj[node]:
                        heapq.heappush(pq, (price + cost, nei, stops - 1))
        
        return -1


# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         res = 0
#         adj = {i:[] for i in range(n)}
#         resArr = [[float('inf') for j in range(k+2)] for i in range(n)]
#         for i, edge, cost in flights:
#             adj[i].append([edge, cost])

#         pq = []
#         heapq.heappush(pq, [0, src, k+1])
#         print(resArr)
#         while pq:
#             dist, u, stops = heapq.heappop(pq)

#             if u == dst:
#                 return dist
            
#             if stops > 0:
#                 for nei, cost in adj[u]:
#                     newDist = dist + cost
#                     if resArr[nei][stops -1] > newDist:
#                         heapq.heappush(pq, [newDist, nei, stops-1])
            


#         return -1

#         # visit = set()
#         # q = deque()
#         # q.append(adj[0])
#         # lvl = 0
        
#         # while q:
#         #     for i in range(len(q)):
#         #         node = q.popleft()
#         #         print(node)
            
#         #     lvl += 1

#         # print(resArr)
#         # return res
        