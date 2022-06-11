class Solution:
    def minOperations(self, nums: 'List[int]', x: int) -> int: #O( N | N )
        left_hmp = {0:-1} # record the prefix sum loc
        left = [0] # pre-fix sum
        right_hmp = {0:-1} # record the prefix sum loc
        right = [0] 
        curr = 0 
        output = float('inf')
        for i, n in enumerate(nums):
            curr += n 
            left_hmp[curr] = i
            left.append(curr)
            if curr == x:
                output = min(output, i+1) 
                break
            elif curr > x:
                break
        
        curr = 0
        for i, n in enumerate(nums[::-1]): 
            curr += n 
            right_hmp[curr] = i
            if curr == x:
                output = min(output, i+1) 
                break
            elif curr > x:
                break

        for i in range(1, len(left)): # check each accu sum, and see if x-curr is available in right.
            curr = left[i] 
            if x-curr in right_hmp and i + right_hmp[x-curr] < len(nums): #the right should not overlap with left
                oper = i + right_hmp[x-curr] + 1
                output = min(oper, output)
        
        return output if output!=float('inf') else -1
    
    
        

# previous solution

# class Solution:
#     def minOperations(self, nums: 'List[int]', x: int) -> int:
#         right = {0:len(nums)} # sum and the index
#         output = float('inf')
#         s = 0
#         a = nums[::-1] #check sum from right end
#         for i, n in enumerate(a):
#             s+=a[i]
#             right[s] = len(a)-1-i

#         output = (len(nums)- right[x]) if x in right else float('inf')

#         s = 0
#         for i, n in enumerate(nums): # to see if x-currsum exists on the right side
#             s+=nums[i]
#             if x-s in right:
#                 if right[x-s] > i:
#                     leftOperation = i+1
#                     rightOperation= len(nums)-right[x-s]
#                     output = min(output, leftOperation+rightOperation )
#         return output if output!=float('inf') else -1



# previous solution


# class Solution:
#     def minOperations(self, nums: 'List[int]', x: int) -> int:
#         if sum(nums) < x :
#             return -1
#         A = float('inf') 
#         t = x
#         for i, c in enumerate(nums): #sliding from the left
#             t -= c
#             if t == 0:
#                 A = i+1
#         B = float('inf')
#         t = x 
#         for i, c in enumerate(nums[::-1]): #sliding from the right
#             t -= c
#             if t == 0:
#                 B = i+1 
#         #sliding from both side
#         sum_left = [nums[0]]
#         for n in nums[1:]:
#             sum_left.append(sum_left[-1]+n)
#         right = {}
#         curr = 0
#         find = [float('inf')]
#         for i, c in enumerate(nums[::-1]):
#             curr+=c
#             right[curr] = i 
        
#         for i, c in enumerate(sum_left):
#             if x-c in right: # the combination exists
#                 action = i+1+right[x-c] +1 
#                 if action <=len(nums):
#                     find.append(action)
        
#         C = min(find)
        
#         output = min(A,B,C)
        
#         return -1 if output == float('inf') else output
        
        

        
        
        
        
        
        
        
        
        
        
        









