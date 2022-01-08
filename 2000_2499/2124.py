class Solution:
    def checkString(self, s: str) -> bool:
        a_loc = -float('inf')
        b_loc = float('inf')
        for i, c in enumerate(s):
            if c == 'a':
                a_loc = i
            elif b_loc == float('inf'): # never met b before
                b_loc = i #record the first b location
        
        return b_loc > a_loc # if there's no 'b' in the string , b_loc is float('inf')
    
