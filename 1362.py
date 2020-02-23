class Solution:
    def closestDivisors(self, num: int) -> 'List[int]':
        a=num+1
        b=num+2
        for i in range( int(a**0.5)+1, 0, -1):
            if a%i ==0:
                output = [i, a//i]
                diff = abs( i- (a//i) )
                break
        for i in range( int(b**0.5)+1, 0, -1):
            if b%i ==0:
                if abs(b//i - i) < diff:
                    output = [i, b//i]
                break
        return output
    