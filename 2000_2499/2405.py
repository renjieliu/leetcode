class Solution:
    def partitionString(self, s: str) -> int: # O( N | N )
        lkp = set()
        r = 0
        cnt = 0
        while r < len(s): #check if current character is already in the lkp set
            if s[r] not in lkp:
                lkp.add(s[r])
            else:
                cnt += 1 
                lkp = set(s[r])
            r += 1
        cnt += 1
        return cnt 
    

                
            
