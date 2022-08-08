class Solution:
    def lengthOfLIS(self, nums: 'List[int]') -> int: # O( NlogN | N )
        def binFind(arr, v): # find the first one in arr >= v
            s = 0 
            e = len(arr) - 1 
            output = None
            while s <= e:
                mid = s - (s-e)//2
                if arr[mid] >= v:
                    e = mid - 1
                    output = mid
                else:
                    s = mid + 1
            return output
    
        dp = []
        output = 0
        for n in nums: # to find the first one in the dp, >= current n
            if len(dp) == 0 or n > dp[-1]:
                dp.append(n)
            else:
                idx = binFind(dp, n)
                dp[idx] = n
            
            output = max(output, len(dp))
        
        return output
                




# previous solution

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         dp = [1] * len(nums)
#         for i in range(1, len(nums)):
#             for j in range(i-1, -1, -1):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#                     if nums[j] == nums[i]-1:
#                         break
                        
#         return max(dp)
    


# previous solution

# class Solution:
#     def lengthOfLIS(self, nums: 'List[int]') -> int:
#         if nums ==[]: return 0
#         else:
#             dp = [1]
#             for i in range(1, len(nums)):
#                 m = 1
#                 for j in range(i-1, -1, -1):
#                     if nums[j] < nums[i]:
#                         m = max(m, dp[j]+1)
#                 dp.append(m)
#             return max(dp)



# previous solution 

# class Solution:
#     def lengthOfLIS(self, nums: 'List[int]') -> int:
#         dp = [1] * len(nums)
#         ans = 1
#         for i in range(1, len(nums)):
#             for j in range(i-1, -1, -1):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#                     if nums[j] == nums[i]-1:
#                         break
#             ans = max(ans, dp[i])
#         return ans


# previous solution

# class Solution:
#     def lengthOfLIS(self, nums: 'List[int]') -> int:
#         if len(nums) in [0,1]:
#             return len(nums)
#         long = [None] * len(nums)
#         long[0] = None

#         for i in range(len(nums)):
#             find = 1
#             tempMax = [-99]
#             for j in range(i, -1, -1):
#                 if long[j] != None and nums[j]<nums[i]:
#                     tempMax.append(long[j]+find)

#                 elif nums[j]<nums[i]:
#                     find+=1

#             long[i] =max(find, max(tempMax) )

#         return max(long)
