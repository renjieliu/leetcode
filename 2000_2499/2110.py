class Solution:
    def getDescentPeriods(self, prices: 'List[int]') -> int:
        cnt = 0
        days = 1
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] == -1: # add to the days, if smooth  
                days += 1
            else:
                if days > 1: # calc the previous smooth periods
                    a = 1 
                    e = days-1 # except for 1-day period, it will be added in return
                    cnt += ((a+e) * (e-a+1)//2) # (s+e)*h//2
                days = 1 
            # print(s, cnt)
        
        if days > 1: #the last smooth period of the array
            a = 1 
            e = days-1 # except for 1-day period, it will be added in return
            cnt += ((a+e) * (e-a+1)//2) # (s+e)*h//2
        
        return cnt + len(prices)                
    
