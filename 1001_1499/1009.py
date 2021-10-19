class Solution:
    def bitwiseComplement(self, N: int) -> int:
        digits = 0
        n = N
        while n > 0: #find the 1111 to be Xor'ed
            digits +=1
            n = n >> 1
        return 1 if N == 0 else N ^ (2**digits-1)