class Solution:
    def isArmstrong(self, N: int) -> bool:
        s = 0
        for i in str(N):
            s+=int(i) **len(str(N))
        if s==N:
            return True
        return False