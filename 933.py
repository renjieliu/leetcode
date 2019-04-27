class RecentCounter(object):

    def __init__(self):
        self.pings = []
        self.currMax = -1

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.pings.append(t)
        if self.pings[0] >=t-3000:
            return len(self.pings)
        else:
            start = self.currMax if self.currMax!=-1 else 0
            for i in range(start, len(self.pings)):
                if self.pings[i] < t-3000:
                    self.currMax=i  #find how many need to removed...
                else:
                    break
            if self.currMax ==-1:
                return len(self.pings)
            else:
                return len(self.pings) - (self.currMax+1)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)