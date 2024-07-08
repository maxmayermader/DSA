class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # for i in range(len(stones)):
        #     stones[i] = -1*stones[i]
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -1*heapq.heappop(stones)
            x = -1*heapq.heappop(stones)

            if x == y:
                continue
            newStone = y - x
            heapq.heappush(stones, -1*newStone)
            
        # if not stones:
        #     return 0
        return -1*stones[0] if stones else 0
        