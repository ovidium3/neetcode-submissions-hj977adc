class Twitter:

    def __init__(self):
        # use default dicts here to avoid dealing with keys that don't exist
        self.tweetMap = defaultdict(list) # map of user IDs to a list of [tweetNum, tweet IDs]
        self.followingMap = defaultdict(set) # map of user IDs to a list of user IDs
        self.tweetNum = 0 # track of how many overall tweets posted, to assign a recency ranking

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetNum -= 1 # decrement tweet count since new tweet posted
        self.tweetMap[userId].append([self.tweetNum, tweetId]) # insert pair

    def getNewsFeed(self, userId: int) -> List[int]: # O(n) + O(10 log n) = O(n)
        allTweets = list(self.tweetMap[userId]) # init giant list with user's own tweets
        
        for user in self.followingMap[userId]: # add to list of pairs of freq, tweet id for the user's following
            if user != userId: # avoid double counting user that follows themselves
                userTweets = list(self.tweetMap[user])
                for i in range(len(userTweets)):
                    allTweets.append(userTweets[i]) # concatenate to allTweets list

        heapq.heapify(allTweets) # now heapify the whole list into a max Heap
        # most recent have highest num, since all recency ranking are negative to simulate maxHeap

        res = heapq.nsmallest(10, allTweets) # get n smallest
        res = [n[1] for n in res] # only take index 1 val since first serves only as a recency ordering
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # no need to check if follower already follows since using a set
        self.followingMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # need to check since using a dict, not a set here
        if followeeId in self.followingMap[followerId]:
            self.followingMap[followerId].remove(followeeId)