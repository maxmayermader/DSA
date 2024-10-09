class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counts = [0]* len(nums)
        # for num
        hm = Counter(nums)
        pq = []
        for key in hm:
            heapq.heappush(pq, (hm[key], key))
            if len(pq) > k:
                heapq.heappop(pq)
        
        return [val[1] for val in pq]