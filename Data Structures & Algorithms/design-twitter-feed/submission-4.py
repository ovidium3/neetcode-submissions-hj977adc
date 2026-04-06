class Twitter:
    # intuition: we want to set up a bunch of heaps
    # for each user, of size 10
    # most recent tweet ID number determines if it is a maxHeap
    # or a minHeap depending on which counts as more recent - lo or hi

    def __init__(self):
        self.tweets = defaultdict(list) # userId : tweet Heap
        self.feedLimit = 10
        self.following = defaultdict(set) # userId: followingId
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        heapq.heappush(self.tweets[userId], [-self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = list(self.tweets[userId])
        for f in self.following[userId]:
            if f == userId:
                continue # do not want to process self's tweets again
            fList = self.tweets[f]
            feed += fList
        heapq.heapify(feed)
        res = []
        while feed and len(res) < 10:
            res.append(heapq.heappop(feed)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # allow user to follow themselves?
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            return
        if followeeId not in self.following[followerId]:
            return
        self.following[followerId].remove(followeeId) # passed checks
