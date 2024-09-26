class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n+1)}
        for node, nei, cost in times:
            adj[node].append([cost, nei])
        
        costMap = {i:float('inf') for i in range(1, n+1)}
        costMap[k] = 0  # Set the starting node's cost to 0
        visit = set()
        pq = [(0, k)]  # Use a tuple instead of a list
        
        while pq:
            cost, node = heapq.heappop(pq)
            
            if node in visit:
                continue
            
            visit.add(node)
            
            for neiCost, nei in adj[node]:
                newCost = cost + neiCost  # Use the current cost, not costMap[node]
                if newCost < costMap[nei]:
                    costMap[nei] = newCost
                    heapq.heappush(pq, (newCost, nei))  # Use a tuple
        
        maxCost = max(costMap.values())
        return maxCost if maxCost < float('inf') else -1