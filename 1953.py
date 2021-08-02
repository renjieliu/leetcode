class Solution:
    def numberOfWeeks(self, milestones: 'List[int]') -> int:
        total = sum(milestones)
        largest = max(milestones)
        rest = total - largest
        if largest <= rest: # if the largest is less than the sum of others, it can be split to other projects
            return total
        else: #it cannot be split, and +1 for the unfinished
            return 2*rest + 1

