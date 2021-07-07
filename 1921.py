class Solution:
    def eliminateMaximum(self, dist: 'List[int]', speed: 'List[int]') -> int:
        ceiling = lambda x : int(x) + (1 if int(x)!=x else 0)
        arrive = sorted([ceiling(a/b) for a, b in zip(dist, speed)])
        time = 0
        while arrive: #keep shooting every minute, until the monster arrives, and it cannot be eliminate before current time.
            if time < arrive[0]:
                time+=1
                arrive.pop(0)
            else:
                return len(dist) - len(arrive) #total - left = eliminated
        return len(dist)

