class Solution:
    def smallestNumber(self, pattern: str) -> str: # O( N | N ) N = len(pattern)
        stk = [1] # initialize the stk as 1
        output = []
        for i, p in enumerate(pattern):
            if p == "I": #dump the previous stk in reverse 
                output += stk[::-1]
                stk = [] 
            stk.append(i+2) #add the next number to the stk
        
        output += stk[::-1]        
        return "".join([str(_) for _ in output])
            
