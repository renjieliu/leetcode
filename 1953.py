class Solution:
    def numberOfWeeks(self, milestones: 'List[int]') -> int:
        #take one from the smallest, and take one from the current maximum
        #if the maximum cannot be exhausted, then stop
        #else, all the milestones can be finished
        total = sum(milestones)
        largest = max(milestones)
        rest = total - largest
        if largest <= rest: # if the largest is less than the sum of others, it can be split to other projects
            return total
        else: #it cannot be split, and +1 for the unfinished
            return 2*rest + 1


