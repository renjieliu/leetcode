class Solution:
    def countEven(self, num: int) -> int:   
        def digitSum(n): #calc the digitsum
            output = 0
            while n > 0:
                output += n%10
                n //= 10
            return output
        
        cnt = 0
        for n in range(2, num+1):
            cnt += 0 if digitSum(n) % 2 else 1 # add 1 to count if digitSum is even, else 0 
        return cnt
    
    
