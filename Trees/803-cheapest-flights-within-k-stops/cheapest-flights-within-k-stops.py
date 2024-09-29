class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float('inf')]*n
        costs[src] = 0

        for i in range(k+1):
            tempCosts = costs.copy()

            for start, end, cost in flights:
                if costs[start] == float('inf'):
                    continue
                if costs[start] + cost < tempCosts[end]:
                    tempCosts[end] = costs[start] + cost

            costs =  tempCosts

        return -1 if costs[dst] == float("inf") else costs[dst]