class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        arr = str(n)
        p = 1
        s = 0
        for a in arr:
            p*=int(a)
            s+=int(a)
        return p-s