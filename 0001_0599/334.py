class Solution:
    def increasingTriplet(self, nums: 'List[int]') -> bool: # O( N | 1 )
        a = b = float('inf') # first and second number
        for n in nums:
            if n <= a: # n <= a 
                a = n  
            elif n <= b: # n > a and n <= b 
                b = n 
            else: # n > b > a 
                return True 
        return False 
    

    


# previous solution

# class Solution:
#     def increasingTriplet(self, nums: 'List[int]') -> bool: # O( N | N )
#         if len(nums) == 1:
#             return False
#         minLeft = [float('inf')]
#         for i in range(1, len(nums)): # find the min on the left
#             minLeft.append(min(nums[i-1], minLeft[-1]))
#         maxRight = [-float('inf')]
        
#         for i in range(len(nums)-2, -1, -1): # find the max on the right
#             maxRight.append(max(maxRight[-1], nums[i+1]))
        
#         maxRight = maxRight[::-1]
#         return any(True for i in range(len(nums)) if minLeft[i]  < nums[i] < maxRight[i]) #return any one if minLeft < curr < maxRight
        

 


# previous solution

# class Solution:
#     def increasingTriplet(self, nums: 'List[int]') -> bool:
#         a = b = float('inf') #first number, second number, the goal is to find the third number
#         for n in nums:
#             if n <= a: #a need to be smallest
#                 a = n
#             elif n<= b:# b> a
#                 b = n
#             else: # n > b and b > a
#                 return True
#         return False

# previous approach
# class Solution:
#     def increasingTriplet(self, nums: 'List[int]') -> bool:
#         minStk = [nums[0]]
#         for n in nums[1:]:  # find the minStk up to curr
#             minStk.append(min(minStk[-1], n))
#         maxStk = [nums[-1]]
#         for n in nums[:-1][::-1]:  # find the max on the right
#             maxStk.append(max(maxStk[-1], n))
#         maxStk = maxStk[::-1]
#
#         for i in range(len(nums)):  # check if there's smaller on the left, and larger on the right
#             if minStk[i] < nums[i] < maxStk[i]:
#                 return True
#         return False
#
