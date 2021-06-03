class Solution:
    def twoEggDrop(self, n: int) -> int:
        #100, 99, 97, 94,90, 85, 79 .... 0 , count how many numbers with this pattern between 0 and n
        cnt = 0
        t = 0
        while n > 0:
            cnt += 1
            t += 1
            n -= t
        return cnt
