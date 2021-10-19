class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        output = 0
        A = 'ab' if x >= y else 'ba'
        B = 'ab' if A == 'ba' else 'ba'
        if x < y: x,y = y, x #x is always the larger one. and A should always be replaced first

        while A in s or B in s :
            while A in s:
                t = s.replace(A, '')
                output += ((len(s) - len(t))//2) * x
                s = t
                #print(t, output)
            while B in s:
                t = s.replace(B, '')
                output += ((len(s) - len(t))//2) *y
                s = t

        return output
