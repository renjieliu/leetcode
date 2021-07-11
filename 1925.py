class Solution:
    def countTriples(self, n: int) -> int:
        lkp = set([_**2 for _ in range(1, n+1)])
        cnt = 0
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if i**2+j**2 in lkp:
                    cnt += 2 #a2+b2=c2, b2+a2=c2
        return cnt
