class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user_t = {} # user tweet ID
        self.follower = {} #user's following
        self.counter = 0



    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.counter += 1
        if userId not in self.user_t:
            self.user_t[userId] = []
        self.user_t[userId].append([self.counter, tweetId])



    def getNewsFeed(self, userId: int) -> 'List[int]':
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """

        people = [userId] + (list(self.follower[userId]) if userId in self.follower else [])
        # print(people)
        output = []
        pool = []
        for p in people:
            if p in self.user_t:
                pool += self.user_t[p] #add all the user tweets to the pool

        pool.sort(key = lambda x : x[0], reverse = True) #sort the tweet by counter

        for i in range(min(len(pool), 10)):
            output.append(pool[i][1])

        return output


    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.follower:
            self.follower[followerId] = set()
        self.follower[followerId].add(followeeId)



    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """

        if followerId in self.follower and followeeId in self.follower[followerId]:
            self.follower[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)