class Solution:
    def sortEvenOdd(self, nums: 'List[int]') -> 'List[int]':
        odd = []
        even = []
        while nums:
            even.append(nums.pop(0))
            if nums:
                odd.append(nums.pop(0))
        output = []    
        odd.sort() #sort increasing, and pop from end, to be non-increasing
        even.sort(reverse = True) #sort decreasing, and pop from end, to be non-decreasing
        while even:
            output.append(even.pop()) # even indices non-decreasing, 
            if odd:
                output.append(odd.pop()) #odd need to be decreasing
        
        if odd: 
            output.append(odd.pop())
        
        return output
    

