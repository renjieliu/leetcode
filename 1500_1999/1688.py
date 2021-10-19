class Solution:
    def numberOfMatches(self, n: int) -> int:
        cnt = 0
        while n > 1:
            if n % 2 != 0:
                cnt +=1
            cnt += n//2
            n//=2
        return cnt