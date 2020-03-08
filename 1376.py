class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: 'List[int]', informTime: 'List[int]') -> int:
        def dfs(output, curr, sub, person):
            if person not in sub: #no one is reporting to him
                output.append(curr)
            else:
                for x in sub[person]: #for all the subordinates
                    dfs(output, curr+informTime[person], sub,x)
        sub = {}
        i = 0
        while i < len(manager):#[1,0], [2, 0] , time needed to send message to these people
            m = manager[i]
            if m not in sub:
                sub[m] = []
            sub[m].append(i)
            i+=1
        output = [] #add the root to the output.
        for m in sub[manager[headID]]: #for all the subordinates
            dfs(output, 0, sub, m) #the boss will have himself as the subordinates, so pass in 0 here
        return max(output)
