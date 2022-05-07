class Solution:
    def minimumCardPickup(self, cards: 'List[int]') -> int: #O(N | N )
        hmp = defaultdict(lambda: [])
        for i , c in enumerate(cards): # put the location of each number to the hmp
            hmp[c].append(i)
        
        output = float('inf')
        for k, v in hmp.items():
            if len(v) > 1:
                for i in range(1, len(v)):
                    output = min(output, v[i] - v[i-1]+1)
                    if output == 2: # no need to check the rest. 2 is the minimum it can reach
                        return 2
        return output if output != float('inf') else -1
    
    
    

