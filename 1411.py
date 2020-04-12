class Solution:
    def numOfWays(self, n: int) -> int: # pattern 121 means RYR, RGR.. 123 means RYG, YRG.... 
        mod = 10**9 + 7
        if n == 1:
            return 12
        if n == 2:
            return 54
        else:
            n_121 = 30
            n_123 = 24
            output = 0
            for i in range(3, n+1): #start from 3, every 121 pattern has 5 patterns available, 3 are 121, 2 are 123, every 123 pattern has 4 patterns matching, 2 are 121, and 2 are 123.
                n_121 = n_121 * 5
                n_123 = n_123 * 4
                
                n_121_121 = 3 * n_121 //5
                n_121_123 = 2* n_121 // 5
                
                n_123_121 = 2*n_123//4
                n_123_123= 2*n_123//4
                
                n_121 = n_121_121 + n_123_121
                n_123 = n_121_123 + n_123_123

                output = n_121+ n_123
            return output % mod
            