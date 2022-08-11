class Solution:
    def taskSchedulerII(self, tasks: 'List[int]', space: int) -> int: #O( N | N )
        date = 1  #current date
        d = {} #to record last time the task was performed
        for t in tasks :
            if t not in d or d[t] + space + 1 < date: #current task can be performed
                d[t] = date
                date += 1
            elif d[t] + space + 1 >= date:
                d[t] += space + 1 
                date = d[t] + 1
            
        return date - 1  # since the date is +1 in the for..loop, the final result needs to minus 1
    


