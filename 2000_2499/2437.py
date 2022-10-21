class Solution:
    def countTime(self, time: str) -> int: # O( 1440 | 1440 )
        total = set()
        for i in range(24): # all the possible time
            for j in range(60):
                total.add( ("0" if i < 10 else "") + str(i) + ":" + ("0" if j < 10 else "") + str(j))
        cnt = 0 
        loc = []
        for i, t in enumerate(time): #find the loc in time where it's not ?
            if t != "?":
                loc.append(i)
        
        for curr in total:
            cnt += all( curr[i] == time[i] for i in loc) # all the non ? location in the time is same as current
        
        return cnt
    
    
