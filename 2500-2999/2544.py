class Solution:
    def alternateDigitSum(self, n: int) -> int: # O( logN | 1 )
        A = 0  # no idea how many digits n has, prepare 2 options
        B = 0 
        cnt = 0
        while n > 0: 
            cnt += 1
            c = n%10  # current digit
            A += c if cnt % 2 else -c 
            B += -c if cnt % 2 else c
            n //= 10 
        return A if cnt % 2 else B # if cnt is odd, use option A (+-+-+), else use option B (+-+-)
     


