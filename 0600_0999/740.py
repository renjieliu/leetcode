class Solution:
    def deleteAndEarn(self, nums: 'List[int]') -> int:
        hmp = {}
        for n in nums:
            if n not in hmp:
                hmp[n] = 0 
            hmp[n] += 1 
        lst = sorted(hmp.keys())
        dp = [0, lst[0]*hmp[lst[0]]] 
        for v in lst[1:]:
            if v-1 in hmp: #previous number is in the hmp 
                dp.append(max(v * hmp[v] + dp[-2], dp[-1])) #either use the previous one, or the prevprev + curr
            else: #if not, just use the current one
                dp.append(dp[-1]+ v * hmp[v] )
        return dp[-1]


    
