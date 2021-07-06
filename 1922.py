class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(a, p, mod): #a**p % mod. The same approach as SuperPow, Leetcode No.372
            if p == 0:
                return 1
            else:
                output = 1
                while p > 0:
                    temp = 1
                    for i in range(10):
                        if i == p%10:
                            output = (output * temp) % mod
                        temp = (a * temp)%mod
                    a = temp
                    p//= 10
                return output
        mod = 10**9+7
        combo = n//2 #check how many 5*4 combination are there in the total digits
        A = power(20, combo, mod) #total = [(20**combo) * last % mod = [(20**combo)% mod * (last% mod)]%mod
        #A = pow(20, combo, mod) # using the internal power function, it has the mod paratmeter
        B = (5 if n % 2 == 1 else 1) % mod
        return (A*B) % mod








