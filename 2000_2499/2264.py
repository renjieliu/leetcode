class Solution:
    def largestGoodInteger(self, num: str) -> str: #O(n | 1 )
        output = ""
        a = num[0] #first
        b = num[1] #second
        for i in range(2, len(num)):
            c = num[i] # third
            if a == b and b == c: # all three are same characters
                output = max(output, a+b+c) # check the global max
            else:
                a = b 
                b = c
        return output
    
    
    
