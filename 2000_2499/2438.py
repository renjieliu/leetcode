class Solution:
    def productQueries(self, n: int, queries: 'List[List[int]]') -> 'List[int]':  # O( N | N )
        arr = []
        mod = 10**9+7
        p = 0
        while n > 0: # the shortest arr is where the bit location of n is 1
            if n % 2:
                arr.append(2**p)
            p+=1
            n>>=1

        pre = [1] # initialize the prefix product to 1. 
        for a in arr:
            pre.append(pre[-1]*a) 
        
        output = []
        for a, b in queries:
            output.append( ( pre[b+1]//pre[a] ) % mod ) # calc the delta using the prefix array

        return output

    

    

