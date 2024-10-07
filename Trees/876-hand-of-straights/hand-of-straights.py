class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hm = collections.Counter(hand)
        pq = []
        for key in hm:
            heapq.heappush(pq, key)
        print(pq)

        while pq:
            top = pq[0]
            for val in range(top, groupSize+top):
                if val not in hm:
                    return False
                hm[val] -= 1
                if hm[val] == 0:
                    if val != pq[0]:
                        return False
                    heapq.heappop(pq)

        return True
        