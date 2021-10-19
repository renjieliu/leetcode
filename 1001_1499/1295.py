class Solution:
    def findNumbers(self, nums: 'List[int]') -> int:
        output = 0 
        for n in nums:
            if len(str(n))%2==0:
                output +=1 
        return output