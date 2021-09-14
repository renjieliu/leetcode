class Solution:
    def interchangeableRectangles(self, rectangles: 'List[List[int]]') -> int:
        def gcd(a, b):
            while b!=0:
                a,b=b, a%b
            return a
        hmp = {}
        for a, b in rectangles:
            g = gcd(a, b)
            sig = str(a//g) + "-" + str(b//g) #signature of the rectangle
            if sig not in hmp:
                hmp[sig] = 0
            hmp[sig] += 1
        cnt = 0
        fact = lambda x: 1 if x in (0,1) else x * fact(x-1)
        combo = lambda n, p: fact(n)//(fact(p) * fact(n-p))
        for k, v in hmp.items(): #every 2 of them can form a pair
            if v > 1:
                cnt += combo(v, 2)
        return cnt


