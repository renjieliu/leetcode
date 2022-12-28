class Solution:
    def captureForts(self, forts: 'List[int]') -> int: # O( N | 1 )
        prev = [None, None] # [num, loc]
        output = 0
        for i, c in enumerate(forts):
            if c in (-1, 1):
                if prev[0] == -c: # can move to the previous loc:  1 move to -1, -1 move to 1
                    output = max(output, i-prev[1]-1) # how many zeroes in between
                prev = [c, i]
        return output


    
