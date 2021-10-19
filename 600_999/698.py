class Solution:
    def canPartitionKSubsets(self, nums: 'List[int]', k: int) -> bool:
        def dfs(k, arr, pos, curr, target, check):
            if k==0: return True
            else:
                if curr == target:
                    return dfs(k-1, arr, 0, 0, target, check)
                else:
                    for p in range(pos,len(arr)):
                        if check[p] == 0 :
                            check[p] = 1
                            if dfs(k, arr, p, curr+arr[p], target, check):
                                return True
                            else:
                                check[p] = 0
                    return False


        s = sum(nums)
        if s%k!=0: return False
        else:
            target = s//k
            return dfs(k, nums, 0, 0, target,[0]*len(nums))



# class Solution: #RL 20210930  my new solution, TLE
#     def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
#         total = sum(nums)
#         if total % k != 0 or max(nums) > total//k:
#             return False
#         target = total // k

#         def helper(arr, curr, target, taken):
#             if len(taken) == len(arr): #all are taken
#                 return True
#             elif curr == target:
#                 return helper(arr, 0, target, taken)
#             elif curr > target:
#                 return False
#             else:
#                 for i in range(len(arr)):
#                     if i not in taken:
#                         taken.add(i)
#                         if helper(arr, curr+arr[i], target, taken) == 1:
#                             return True
#                         else:
#                             taken.remove(i)
#                 return False

#         return helper(nums, 0, target, set())




# previous approach
# class Solution:
#     def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
#         def dfs(k, arr, pos, curr, target, check):
#             if k==1: return True
#             else:
#                 if curr == target:
#                     return dfs(k-1, arr, 0, 0, target, check)
#                 else:
#                     for p in range(pos,len(arr)):
#                         if check[p] == 0 :
#                             check[p] = 1
#                             if dfs(k, arr, p, curr+arr[p], target, check):
#                                 return True
#                             else:
#                                 check[p] = 0
#                     return False
#
#
#         s = sum(nums)
#         if s%k!=0: return False
#         else:
#             target = s//k
#             return dfs(k, nums, 0, 0, target,[0]*len(nums))



