class Solution:
    def hardestWorker(self, n: int, logs: 'List[List[int]]') -> int: # O( N | 1 )
        currMax = logs[0][1]
        output = logs[0][0]

        for i in range(1, len(logs)): # go through the list, to find the smalles person id with longest work time
            person, work = logs[i][0], logs[i][1] - logs[i-1][1]
            if work > currMax:
                output = person
                currMax = work
            elif work == currMax:
                output = min(person, output)
        return output



