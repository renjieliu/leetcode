class Solution:
    def combinationSum4(self, nums: 'List[int]', target: int) -> int:  # O( N*K | K) K is same as target
        dp = [0] #pad the 0 to make the lookup easier
        for i in range(1, target+1):
            curr = 0 # how many ways to reach current number
            for n in nums:
                curr += 1 if i == n else (dp[i-n] if i-n >=0 else 0) # pick current number or (prevWays + current number)
            dp.append(curr)
        # print(dp)
        return dp[-1]
                

        
        
# previous solution 

# class Solution:
#     def combinationSum4(self, nums: 'List[int]', target: int) -> int:
#         nums.sort()
#         dp = [0] * (target+1)
#         for i in range(1, target+1):
#             for n in nums:
#                 if n > i:
#                     break
#                 else:
#                     if n == i: #just use the current number
#                         dp[i] +=1
#                     else:
#                         if dp[i-n] != 0: # use the dp[i-n], and current to form the i
#                             dp[i] += dp[i-n]
#         return dp[-1]


# class Solution:
#     def combinationSum4(self, nums: 'List[int]', target: int) -> int:
#         dp = [0] * (target + 1)
#         dp[0] = 1  # current number is "target"
#         for i in range(1,
#                        target + 1):  # calculate from 1 to target --let's assume each one is target. how many ways to get "current target"
#             for n in nums:
#                 if i - n >= 0:  # how many ways to generat i-n
#                     dp[i] += dp[i - n]
#         return dp[-1]
#
