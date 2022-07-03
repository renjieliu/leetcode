class Solution:
    def wiggleMaxLength(self, nums: 'List[int]') -> int: # O( N | N )
        if len(nums) == 0:
            return 0 
        else:
            arr = [] # delta of each 2 neighbour element
            for i in range(1, len(nums)): 
                arr.append(nums[i] - nums[i-1])
            
            last_pos = 0 
            last_neg = 0 
            for a in arr: #dp. if current gap is positive, the longest the last neg+1. if current gap is negative, the longest is last pos+1
                if a > 0:
                    last_pos = last_neg+1 
                elif a < 0:
                    last_neg = last_pos+1
            return max(last_pos, last_neg)+1 #last_pos, last_neg is the gap between 2 neighbours, +1 to get the count of elements
                
            

# previous solution

# class Solution:
#     def wiggleMaxLength(self, nums: 'List[int]') -> int:
#         if len(nums) == 1: return 1
#         else:
#             arr = []
#             for i in range(1, len(nums)):
#                 arr.append(nums[i] - nums[i-1])
#             neg = 1 if arr[0] < 0 else 0
#             pos = 1 if arr[0] > 0 else 0
#             for i in range(1, len(arr)): # just need to find the prev neg and pos, no need for dp array
#                 if arr[i] > 0:
#                     pos = neg+1 #prev longest neg + 1
#                 elif arr[i] < 0:
#                     neg = pos+1 #prev longest pos + 1
#             return max(neg, pos) + 1

