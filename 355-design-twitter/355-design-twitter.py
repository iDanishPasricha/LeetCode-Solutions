class Twitter:

    def __init__(self):
        self.count = 0 # basically it's the time which will tell us the timing of the tweets
        self.tweetmap = defaultdict(list) #userid = list of [count,tweetid]
        self.followmap = defaultdict(set) #userid = set of followeeid 
        
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count , tweetId]) #this user has posted this time at this time (count)
        self.count-=1 # we want our next tweet to be at a different time 0,-1,-2...
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        ans = []
        minheap = []
        
        self.followmap[userId].add(userId)
        for followeeId in self.followmap[userId]:  #iterate through every followee this user follows
            if followeeId in self.tweetmap:  #if this person has atleast one tweet
                
                index = len(self.tweetmap[followeeId])-1  #get the tweets and index will represent most recent tweet which will be [count,tweetid]
                count,tweetId = self.tweetmap[followeeId][index]
                minheap.append([count,tweetId,followeeId,index-1])  #--> beacuse we have to get the same person's next most recent tweet (index-1)
        heapq.heapify(minheap)
        while minheap and len(ans)<10:
            count,tweetId,followeeId,index = heapq.heappop(minheap)
            ans.append(tweetId)
            if index>=0:  #still tweets remaining
                count,tweetId = self.tweetmap[followeeId][index]
                heapq.heappush(minheap,[count,tweetId,followeeId,index-1])
        return ans
        
        
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]: #if you are following that person then only we can remove
            self.followmap[followerId].remove(followeeId)
        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)