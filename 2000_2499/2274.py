class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: 'List[int]') -> int: #O(nlogn | 1)
        special.sort()
        output = 0 if special[0] == bottom else special[0]-bottom # in case the first floor is special
        for i in range(1, len(special)):
            output = max(output, special[i] - special[i-1] -1 ) #how many consecutive floor in between
        
        if special[-1] == top: # in case the last floor is special
            return output
        else:
            return max(output, top - special[-1])

    
