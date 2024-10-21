class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # create an adjacny list
        # use dijkstras and add up total costs
        #   add cost and node to pq
        # return total if all nodes have been visited else -1
        tot = 0
        adj = {i:[] for i in range(1, n+1)}
        for src, dest, cost in connections:
            adj[src].append((cost,dest))
            adj[dest].append((cost,src))
        pq = [(0, connections[0][0])]
        print(adj)
        visit = set()
       

        while pq:
            cost, v = heapq.heappop(pq)
            if v in visit:
                continue
            visit.add(v)

            # if len(visit) == n:
            #     return tot

            tot += cost
            print(adj[v])
            for neiCost, nei in adj[v]:
                if nei not in visit:
                    heapq.heappush(pq, (neiCost, nei))

        return tot if len(visit) == n else -1
        # return -1