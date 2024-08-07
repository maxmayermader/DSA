class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1*num)

        if ((self.small and self.large) and (-1*self.small[0] > self.large[0])):
            heapq.heappush(self.large, -1* heapq.heappop(self.small))

        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -1* heapq.heappop(self.small))

        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -1* heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]
        return (-1*self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# class MedianFinder:

#     def __init__(self):
#         self.stream = []
        

#     def addNum(self, num: int) -> None:
#         # self.stream.append(num)
#         heapq.heappush(self.stream, num)

#     def findMedian(self) -> float:
#         if len(self.stream) == 1:
#             return self.stream[0] * 1.0

#         if len(self.stream) % 2 != 0:
#             newStream = self.stream.copy()
#             i = 0
#             to = -(len(self.stream) // -2) - 1
#             while i <= to:
#                 if i == to:
#                     return heapq.heappop(newStream)
#                 heapq.heappop(newStream)
#                 i+=1

#         else:
#             newStream = self.stream.copy()
#             i = 0
#             to = len(self.stream) / 2 + 1 - 1
#             a, b = 0, 0
#             while i <= to:
                
#                 if i == to - 1:
#                     a = heapq.heappop(newStream) * 1.0
#                     i+=1
#                     continue
#                 if i == to:
#                     b=heapq.heappop(newStream)
#                     return (a + b) / 2
#                 heapq.heappop(newStream)
#                 i+=1
                