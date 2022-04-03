class Solution:
    def triangularSum(self, nums: 'List[int]') -> int:
        while len(nums) > 1:
            for i in range(1, len(nums)):
                nums[i-1] = (nums[i-1] + nums[i])%10 #put result back to prev loc. As current loc will be used for next calc
            nums.pop() #take out the last element of the nums
        return nums[0]
    
    


# previous solution

# class Solution:
#     def triangularSum(self, nums: 'List[int]') -> int:
#         while len(nums) > 1: #using the same structure as BFS, to eliminate the nums until only 1 element left
#             nxt =[]
#             for i in range(1, len(nums)):
#                 nxt.append((nums[i] + nums[i-1])%10)
#             nums = nxt 
#         return nums[0]
    
    

            
