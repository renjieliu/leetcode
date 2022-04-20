class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def calc(s, k): # go through the s, calc the sum of each k digits
            output = ""
            curr = 0
            i = 0
            while i < len(s):
                if i%k != 0:
                    curr += int(s[i])
                else:
                    output += str(curr) 
                    curr = 0
                    curr += int(s[i])
                i+=1
            output += str(curr)
            return output[1:] # take out the first "0"
            
            
        while len(s) > k: # simulation.
            s = calc(s, k)
            # print(s)
        return s
    
    
    

    
