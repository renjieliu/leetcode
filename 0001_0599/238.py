class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        zeroloc = -1 # record the location of 0.
        total = 1
        for i, n in enumerate(nums):
            if n == 0:
                if zeroloc == -1:
                    zeroloc = i 
                else:
                    return [0 for _ in nums ] # if 2 zeroes, return all 0 
            else:
                total *= n
       
        output = []
        if zeroloc != -1:  # if no zero, using total//curr. if 1 zero, return total for the zero loc. others are 0
            output = [0 for _ in nums]
            output[zeroloc] = total
        
        else:
            for i, n in enumerate(nums):
                output.append(total//n)
        
        return output


# previous approach
# def productExceptSelf(nums: 'List[int]'):
#     #from left to right, make the first element as 1.
#     ini =1
#     output =[]
#     for i in range(len(nums)):
#         output.append(ini)
#         ini*=nums[i]

#     #from right to left

#     ini = 1
#     for i in range(len(nums) - 1, -1, -1):
#         output[i] = output[i] * ini
#         ini *= nums[i]
#     return output

# print(productExceptSelf([1,2,3,4]))