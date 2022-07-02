class Solution:
    def minMoves2(self, nums: 'List[int]') -> int: # O( N | 1 )
        nums.sort()
        n = len(nums)
        med = (nums[(n-1)//2] + nums[n//2])//2
        cnt = 0
        for n in nums: #to sum the distance from curr number to medium
            cnt += abs(n-med)
        return cnt
    



# previous solution

# class Solution:
#     def minMoves2(self, nums: 'List[int]') -> int:
#         nums.sort()
#         output = float('inf')
#         currTotal = 0 
#         total = sum(nums)
#         for i, n in enumerate(nums): #assume move all to n, total move is [n*idx - SUM(before)] + [sum(after) - c*count(remaining)]
#             before = (i*n - currTotal)
#             after = abs(n * (len(nums)-i) - (total - currTotal))
#             move = before + after
#             output = min(output, move)
#             currTotal +=n 
#         return output
        
#         # nums.sort()
#         # medium = nums[len(nums)//2]
#         # return sum([abs(n-medium) for n in nums]) 


    
# previous solution

# class Solution:
#     def minMoves2(self, nums: 'List[int]') -> int:
#         nums.sort()
#         medium = nums[len(nums)//2]
#         return sum([abs(n-medium) for n in nums])



# previous solution


# class Solution:
#     def minMoves2(self, nums: 'List[int]') -> int:
#         # t = sum(nums)//len(nums)
#         # a = sum([abs(n-t) for n in nums])
#         # b = sum([abs(n-t-1) for n in nums])
#         output = float('inf') #min(a, b) #avg
#         nums.sort()
#         if len(nums) % 2: #medium number 
#             t = nums[len(nums)//2]
#             c = sum([abs(n-t) for n in nums]) 
#             output = min(output, c) 
#         else:
#             t = nums[len(nums)//2] + nums[len(nums)//2-1]
#             t //=2
#             c = sum([abs(n-t) for n in nums]) 
#             d = sum([abs(n-t-1) for n in nums]) 
#             output = min(output, c, d)
#         return output



