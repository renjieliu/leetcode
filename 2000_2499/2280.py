class Solution:
    def minimumLines(self, stockPrices: 'List[List[int]]') -> int: #O(nlogn | 1)
        def findKB(p1, p2): #find K and B of the line
            k = (p2[1]-p1[1])/(p2[0]-p1[0])
            b = p1[1] - k*p1[0]
            return [k, b]
        
        stockPrices.sort(key = lambda x: x[0])
        # print(stockPrices)
        if len(stockPrices) < 2:
            return 0
        prevK, prevB = findKB(stockPrices[0], stockPrices[1]) 
        cnt = 1
        for i in range(2, len(stockPrices)): #find K, b of current point and prev, and see if it can be connected with prev line
            k, b = findKB(stockPrices[i], stockPrices[i-1])
            if abs(prevK-k) > 0.000000000001  or abs(prevB - b ) > 0.000000000001:
                #print(prevK, k , prevB, b)
                cnt += 1
            prevK = k
            prevB = b
    
        return cnt
    
