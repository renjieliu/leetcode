class Solution:
    def findingUsersActiveMinutes(self, logs: 'List[List[int]]', k: int) -> 'List[int]':
        hmp = {}
        for u,m in logs: #add minute to the set, and see the length of the set, which is the "user active minutes"
            if u not in hmp:
                hmp[u] = set()
            hmp[u].add(m)
        output = [0]*(k+1) #answer is 1-indexed
        for v in hmp.values():
            output[len(v)]+=1
        return output[1:] #answer is 1-indexed