class Solution:
    def countNicePairs(self, nums: 'List[int]') -> int:
        def rev(n):
            output = 0
            while n > 0:
                output *= 10
                output += (n % 10)
                n//=10
            return output
        hmp = defaultdict(int) #a+f(b)=b+f(a) ==> a-f(a) = b-f(b), find all the a-f(a), put into a hashmap, and combo(n, 2)
        for n in nums:
            hmp[n-rev(n)]+=1
        fact = lambda x: 1 if x <= 1 else x * fact(x-1)
        combo = lambda m,n: fact(m)//(fact(n) * fact(m-n))
        output = 0
        mod = 10**9+7
        for v in hmp.values():
            if v > 1:
                output += combo(v,2)
        return output % mod
