class Solution:
    def countSubarrays(self, nums: 'List[int]') -> int: # O( N | 1 )
        gauss = lambda x: (1+x)*x//2 # adding from 1 to x 
        l = 0
        r = 1 
        cnt = 0 
        while r < len(nums):
            if nums[r] <= nums[r-1]: # not strictly increasing, count the total from prev segment
                cnt += gauss(r-1-l+1) #count the start to prev element
                l = r
            r+=1
        cnt += gauss(r-1-l+1) #count the last segment
        return cnt



# previous solution

# class Solution:
#     def countSubarrays(self, nums: 'List[int]') -> int: # O( N | 1 )
#         gauss = lambda x: (1+x)*x//2 # sum from 1 to x 
#         l = 0
#         r = 1 
#         cnt = 0 
#         while r < len(nums):
#             if nums[r] <= nums[r-1]: # not strictly increasing, count the total from prev segment
#                 cnt += gauss(r-1-l+1) #count the start to prev element
#                 l = r
#             r+=1
#         cnt += gauss(r-1-l+1) #count the last segment
#         return cnt



