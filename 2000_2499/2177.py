class Solution:
    def sumOfThree(self, num: int) -> 'List[int]': #if n cannot be divided 3 parts, return [] else, return [n//3-1, n//3, n//3+1]
        return [] if num % 3 else [num//3-1, num//3, num//3+1] 


    
