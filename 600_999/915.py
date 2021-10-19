class Solution:
    def partitionDisjoint(self, nums: 'List[int]') -> int:
        mx = [-float('inf')] #max on the left
        mi = [float('inf')] # min on the right
        for i in range(1, len(nums)):
            mx.append(max(nums[i-1], mx[-1]))

        for i in range(len(nums)-2, -1, -1):
            mi.append(min(nums[i+1], mi[-1]))
        mi = mi[::-1]

        #print(mx, mi)
        for i in range(len(nums)): #max on the left is smaller than the smallest on the right
            if mx[i] <= mi[i] and nums[i] <= mi[i]:
                return i+1 #return the length if cut here, including current to the left array


# previous approach
# class Solution:
#     def partitionDisjoint(self, A: 'List[int]') -> int:
#         leftMax = []
#         currMax = -float('inf')
#         for i, c in enumerate(A):
#             currMax = max(c, currMax)
#             leftMax.append(currMax)
#
#         currMin = float('inf')
#         rightMin = [0] * len(A)
#         for i in range(len(A) - 1, -1, -1):
#             currMin = min(currMin, A[i])
#             rightMin[i] = currMin
#
#         # print(leftMax)
#         # print(rightMin)
#         for i in range(len(A) - 1):
#             if leftMax[i] <= rightMin[i + 1]: #if maxup to now is <= the min on the right.
#                 return i + 1
#         return len(A) - 1
