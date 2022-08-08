class Solution:
    def countBadPairs(self, nums: 'List[int]') -> int: #O( N | N )
        gauss = lambda x: x*(1+x) //2 
        N = len(nums)
        total = gauss(N-1) # total for i < j is 1+2...+len(arr)-1
        dp = defaultdict(lambda :0) 
        good = 0 #good pairs are j - nums[j] == i - nums[i]
        for i, n in enumerate(nums): # j-i != nums[j] - nums[i] ==> j - nums[j] != i - nums[i]
            good += dp[i-n] # how many pairs with previous numbers can be formed with current number
            dp[i-n] += 1 #reason for adding dp after good is - say the cnt is 4, the pair is 1+2+3, it's starting from 1 to cnt-1
        return total - good



# previous solution 

# class Solution:
#     def countBadPairs(self, nums: 'List[int]') -> int: #O( N | N )
#         gauss = lambda x: x*(1+x) //2 
#         N = len(nums)
#         total = gauss(N-1) # total for i < j is 1+2...+len(arr)-1
#         dp = defaultdict(lambda :0) 
#         good = 0 #good pairs are j - nums[j] == i - nums[i]
#         for i, n in enumerate(nums): # j-i != nums[j] - nums[i] ==> j - nums[j] != i - nums[i]
#             good += dp[i-n] # how many pairs with previous numbers can be formed with current number
#             dp[i-n] += 1
#         return total - good


    
