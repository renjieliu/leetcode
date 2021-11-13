class Solution:
    def isPossibleDivide(self, nums: 'List[int]', k: int) -> bool:
        if k ==1 :
            return True
        else:
            hmp = {} 
            for n in nums:
                if n not in hmp:
                    hmp[n] = 0
                hmp[n] +=1

        while len(hmp) > 0:
            start =  min(hmp.keys())
            stk = [_  for _ in range (start ,start + k ) ]
            deduction = hmp[start]
            for s in stk:
                if s not in hmp:
                    return False 
                hmp[s] -= deduction #current number should repeat at least the same time as the first number in the stack
                if hmp[s] < 0:
                    return False
                elif hmp[s] ==0:
                    del hmp[s]
        return True



# Notes: 

# ---Leetcode 1296 failed 2 approaches:
# -- 1. dfs
# class Solution:
#     def isPossibleDivide(self, nums: List[int], k: int) -> bool:
#         hm = {}
#         dp = []
#         for i in range(len(nums)):
#             curr = [0,0]
#             prev = nums[i]-1
#             nxt = nums[i] +1
#             if prev in hm:
#                 curr[0] = hm[prev]
#             if nxt in hm:
#                 curr[1] = hm[nxt]
#             if nums[i] not in hm:
#                 hm[nums[i]] = 0
#             hm[nums[i]] +=1
#             dp.append(curr)
        
            
#  def isPossibleDivide(nums, k: int) :
#   def dfs(check, nums, start, nxt, cnt,k):
#       if start == len(nums): # it has reached the end, and it has not found a match
#           return -1
#       elif cnt == k:
#           check[start] = 1
#           return 1             
#       else:
#           check[start] = 1
#           curr = nxt + 1 
#           while curr<len(nums):
#               if nums[curr] == nums[start]+1 and check[curr] != 1:
#                   t = dfs(check, nums, curr, nxt, cnt+1,k)
#                   if t == 1:
#                       return 1
#                   else: 
#                     return -1 
#               curr+=1
     
#       return -1

#   if k ==1:
#       return True
#   else:
#       nums.sort()
#       check = [0 for _ in range(len(nums))]
#       for i in range(len(nums)):
#           if check[i] == 0:
#               if dfs(check,nums,i,1,k) == -1:
#                   return False

#   return True
          


# ----------
# --2. Binary search

# class Solution:
#     def isPossibleDivide(self, nums: List[int], k: int) -> bool:
#         def bin_search(arr, target):
#             start = 0
#             end = len(arr)-1
#             while start<=end:
#                 mid = (start+end) //2
#                 if arr[mid] == target:
#                     return mid
#                 elif arr[mid] > target:
#                     end = mid-1
#                 else:
#                     start = mid+1 
#             return -1      
#         if k ==1:
#             return True
#         else:
#             nums.sort()
#             check = [0 for _ in range(len(nums))]
#             for i in range(len(nums)):
#                 if check[i] == 0: #using binary search for the next number
#                     curr = nums[i]
#                     cnt = 1
#                     check[i] = 1
#                     res = i
#                     target = curr+1 
#                     while cnt < k:
#                         res += bin_search(nums[res:], target)
#                         if res ==-1: #if cannot find the next number
#                             return False
#                         else:
#                             check[res] = 1
#                             cnt+=1
#                             target+=1
#         return True

#  ----------------------





