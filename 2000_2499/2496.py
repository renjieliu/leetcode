class Solution:
    def maximumValue(self, strs: 'List[str]') -> int: # O( N | N )
        output = -float('inf') 
        num = set('0123456789')
        for s in strs:
            if set(s) - num: # it has letters in it 
                output = max(output, len(s))
            else: # all are numbers
                output = max(output, int(s))
        return output
    

