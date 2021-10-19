class TopVotedCandidate:

    def __init__(self, persons: 'List[int]', times: 'List[int]'):
        self.persons = persons
        self.times = times
        self.currentWinning = [None] * len(times)  # this is same as len(persons)
        self.maxVote = 0
        self.winningHash = {}

        for i in range(len(persons)):
            p = persons[i]
            if p not in self.winningHash:
                self.winningHash[p] = 0
            self.winningHash[p] += 1

            if self.winningHash[p] >= self.maxVote:
                self.maxVote = self.winningHash[p]
                self.currentWinning[i] = p
            else:
                self.currentWinning[i] = self.currentWinning[i - 1]

    def q(self, t: int) -> int:
        # use binary search to find the index of the time, and get the corresponding winning as pre-calculated.
        if t>self.times[-1]:
            return self.currentWinning[-1]
        start = 0
        end = len(self.times)
        while start <= end:
            mid = (start + end) // 2
            if self.times[mid] == t:
                return self.currentWinning[mid]
            elif self.times[mid] > t:
                end = mid -1
            else:
                start = mid +1

        if self.times[mid] > t:
            return self.currentWinning[mid-1]
        else:
            return self.currentWinning[mid]

# Your TopVotedCandidate object will be instantiated and called as such:
obj = TopVotedCandidate([0,1,0,1,1],[24,29,31,76,81])

print (obj.q(77))



