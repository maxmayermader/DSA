class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # heapq.heappush(self.tweets, [self.count, tweetId])
        self.tweets[userId].append([self.count, tweetId])
        self.count = self.count - 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.follows[userId].add(userId)
        for followeeId in self.follows[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId])-1
                count, tweetId = self.tweets[followeeId][index]
                # minHeap.append([count, tweetId, followeeId, index-1])
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])


        return res


        # res = []
        # newTweets = self.tweets.copy()
        # i = 0
        # while newTweets and i < 10:
        #     res.append( heapq.heappop(newTweets)[1])
        #     i += 1


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)