class Solution:
    def makesquare(self, matchsticks: 'List[int]') -> bool: # O( N * 2**N | 2**N ) RL 20220712: Copied solutions, my code got TLE this time.
        # If there are no matchsticks, then we can't form any square.
        if not matchsticks:
            return False

        # Number of matchsticks
        L = len(matchsticks)

        # Possible perimeter of our square
        perimeter = sum(matchsticks)

        # Possible side of our square from the given matchsticks
        possible_side =  perimeter // 4

        # If the perimeter isn't equally divisible among 4 sides, return False.
        if possible_side * 4 != perimeter:
            return False

        # Memoization cache for the dynamic programming solution.
        memo = {}

        # mask and the sides_done define the state of our recursion.
        def recurse(mask, sides_done):

            # This will calculate the total sum of matchsticks used till now using the bits of the mask.
            total = 0
            for i in range(L - 1, -1, -1):
                if not (mask & (1 << i)):
                    total += matchsticks[L - 1 - i]

            # If some of the matchsticks have been used and the sum is divisible by our square's side, then we increment the number of sides completed.
            if total > 0 and total % possible_side == 0:
                sides_done += 1

            # If we were successfully able to form 3 sides, return True
            if sides_done == 3:
                return True

            # If this recursion state has already been calculated, just return the stored value.
            if (mask, sides_done) in memo:
                return memo[(mask, sides_done)]

            # Common variable to store answer from all possible further recursions from this step.
            ans = False

            # rem stores available space in the current side (incomplete).
            c = int(total / possible_side)
            rem = possible_side * (c + 1) - total

            # Iterate over all the matchsticks
            for i in range(L - 1, -1, -1):

                # If the current one can fit in the remaining space of the side and it hasn't already been taken, then try it out
                if matchsticks[L - 1 - i] <= rem and mask&(1 << i):

                    # If the recursion after considering this matchstick gives a True result, just break. No need to look any further.
                    # mask ^ (1 << i) makes the i^th from the right, 0 making it unavailable in future recursions.
                    if recurse(mask ^ (1 << i), sides_done):
                        ans = True
                        break
            # cache the result for the current recursion state.            
            memo[(mask, sides_done)] = ans
            return ans

        # recurse with the initial mask with all matchsticks available.
        return recurse((1 << L) - 1, 0)

    
# below is my code, got TLE    

# class Solution:
#     def makesquare(self, matchsticks: List[int]) -> bool: # O(4**N | N )
#         total = sum(matchsticks)
#         if total % 4:
#             return False
#         sides = [0] * 4 
        
#         def dfs(sides,arr, idx, target):
#             if idx == len(arr): #it has reached the end of the arr
#                 return sides[0] == sides[1] == sides[2] == target

#             for i in range(4): #try to place the number to any of the sides
#                 if sides[i] + arr[idx] <= target:
#                     sides[i] += arr[idx]
#                     if dfs(sides, arr, idx+1, target):
#                         return True 
#                     sides[i] -= arr[idx]  
            
#             return False
    
#         return dfs(sides, sorted(matchsticks, reverse = True), 0, total//4)

    
    
    

# previous solution

# class Solution:
#     def makesquare(self, matchsticks: 'List[int]') -> bool:
#         if sum(matchsticks)//4 != sum(matchsticks)/4.0:
#             return False
#         else:
#             def dfs(groups, arr, curr, target):
#                 # print(output, curr, target, arr)
#                 if arr == []:
#                     return True if groups == 4 else False
#                 else:
#                     for i in range(len(arr)):
#                         if arr[i] + curr == target:
#                             if dfs(groups+1 , arr[:i] + arr[i+1:], 0, target) == True: # for the rest
#                                 return True
#                         elif arr[i] + curr < target:
#                             if dfs(groups, arr[:i] + arr[i+1:], arr[i] + curr, target) == True:
#                                 return True
#                         else: #current number cannot be put into a group, return False directly
#                             return False
#                     return False
#             groups = 0
#             return dfs(groups, matchsticks, 0, sum(matchsticks)//4)


# previous approach

# class Solution:
#     def makesquare(self, nums: 'List[int]') -> bool:
#         def dfs(taken, target, group_cnt, nums, curr, pos):
#             if group_cnt == 4:
#                 return 1
#             elif curr == target:
#                 return dfs(taken, target, group_cnt+1, nums, 0, 0)
#             else:
#                 for i in range(pos, len(nums)):
#                     if taken[i] == 0 and curr + nums[i] <= target:
#                         taken[i] = 1
#                         if dfs(taken, target, group_cnt, nums, curr + nums[i], i+1)==1:
#                             return 1
#                         else:
#                             taken[i] = 0
#                 return 0
#
#         s = sum(nums)
#         nums.sort()
#         if len(nums) < 4 or s==0 or s/4!=s//4 or nums[-1] > s//4: return False
#         else:
#             target = s//4
#             taken = [0] * len(nums) #to label if each pos has been taken
#             group_cnt = 1
#             curr = 0
#             pos = 0
#             if dfs(taken, target, group_cnt, nums, curr, pos) ==1 :
#                 return True
#             else:
#                 return False



