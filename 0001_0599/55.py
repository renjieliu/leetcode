class Solution:
    def canJump(self, nums: 'List[int]') -> bool: # O( N | 1 )
        currMax = 0
        for i, n in enumerate(nums): # check the max index can be reached from current
            if i > currMax: # cannot even reach current index
                return False 
            currMax = max(currMax, i+n)
        return currMax >= len(nums)-1




# previous solution

# class Solution:
#     def canJump(self, nums: 'List[int]') -> bool:
#         if len(nums) == 1:
#             return True
#         currMax = 0
#         for i in range(len(nums) - 1):
#             if i > currMax:  # curr location cannot be reached
#                 return False
#             else:
#                 currMax = max(i + nums[i], currMax)  # furthest can be reached from current location
#                 if currMax >= len(nums) - 1:
#                     return True

#         return False





# previous approach
# class Solution:
#     def canJump(self, nums: 'List[int]') -> bool:
#         if len(nums) <= 1: return True
#         possible = {}  # all the possible position from curr
#         targetPos = {}
#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 if i < len(nums) - 1 and i + nums[i] >= len(nums) - 1: targetPos[
#                     i] = None  # as long it can reach curr, it can reach end
#                 possible[i] = [i + 1, min(len(nums) - 1, i + nums[i])]  # start,  end
#             else:
#                 possible[i] = []
#         if len(targetPos) == 0:  return 0  # no position can reach the last index
#
#         targetPosList = sorted(targetPos.keys())
#
#         # print(possible,targetPos)
#         def helper(k, possible, targetPos, targetPosList, check):
#             if check[k] == -1:  # curr pos has bee checked.
#                 return -1
#             elif possible[k] and (
#                     possible[k][0] <= targetPosList[0] <= possible[k][1] or possible[k][0] <= targetPosList[-1] <=
#                     possible[k][1] or k in targetPos):  # any target is within reach
#                 return 1
#             else:
#                 if possible[k]:  # for curr K, check each one possible, see if can reach the end from it
#                     for c in range(possible[k][0], possible[k][1] + 1):
#                         if helper(c, possible, targetPos, targetPosList, check) == 1:
#                             return 1
#                 check[k] = -1
#                 return 0
#
#         return helper(0, possible, targetPos, targetPosList, [0] * len(nums))


# previous approach
# class Solution:
#     def canJump(self, nums: 'List[int]') -> bool:
#         if nums[0] == 0:
#             if len(nums)>1:
#                 return False
#             else:
#                 return True
#
#         maxReached = 0
#
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 if i == maxReached:
#                     return False
#             else:
#                 maxReached = max(i+nums[i], maxReached)
#                 if maxReached >=len(nums)-1:
#                     return True
#
