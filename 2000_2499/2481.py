class Solution:
    def numberOfCuts(self, n: int) -> int: # O( 1 | 1 )
        if n == 1 : # no need to cut
            return 0
        else:
            return n if n % 2 else n // 2 # if even, just cut in the middle, else need to divide it by n pieces
    
