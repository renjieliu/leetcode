class Solution:
    def countDigits(self, num: int) -> int: # O( logN | 1 )
        cnt = 0
        k = num
        while k > 0: # check each digit, and see if it can divide num
            cnt += (num%(k%10) == 0)
            k //= 10
        return cnt

    
