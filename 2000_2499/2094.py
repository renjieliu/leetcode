class Solution:
    def findEvenNumbers(self, digits: 'List[int]') -> 'List[int]':
        hmp = {}
        for d in digits:
            if d not in hmp:
                hmp[d] = 0 
            hmp[d] += 1
        
        def possible(hmp, v):
            ref = {}
            while v > 0:
                if v%10 not in ref:
                    ref[v%10] = 0 
                ref[v%10] += 1 
                v //=10
            for k, v in ref.items():
                if k not in hmp or v > hmp[k]:
                    return False
            return True 
        
        output = []
        for n in range(100, 1000): #to try every 3-digit even number, see if it can be formed by the arr.
            if n%2 == 0 and possible(hmp,n):
                output.append(n)
        return output
                
        
