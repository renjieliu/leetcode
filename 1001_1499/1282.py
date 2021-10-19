class Solution:
    def groupThePeople(self, groupSizes: 'List[int]'):
        group = {} 
        for i in range(len(groupSizes)): # create a pool of each group size, and push the current i to the pool
            currSize = groupSizes[i]
            if currSize not in group:
                group[currSize] = [[]]
                
            if len(group[currSize][-1]) < currSize:
                group[currSize][-1].append(i)
            else:
                group[currSize].append([i])
        output = []
        for k, v in group.items():
            for e in v:
                output.append(e)
                
        return output
        