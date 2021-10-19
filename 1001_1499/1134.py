class Solution:
    def isArmstrong(self, n: int) -> bool:
        s = str(n)
        calc = 0
        for c in s:
            calc += (int(c)**len(s))
        return calc == n

