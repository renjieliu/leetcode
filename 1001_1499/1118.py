class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        hmp = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if Y % 4 != 0:
            hmp[2] = 28
        else:
            if Y % 100 == 0 and Y % 400 != 0:
                hmp[2] = 28
            elif Y % 4 == 0 or Y % 400 == 0:
                hmp[2] = 29
        return hmp[M]
