class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: int) -> int: # O( N**2 | N )
        diff = float('inf')
        nums.sort() 
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1 
            while l < r:
                total = nums[i] + nums[l] + nums[r] 
                if abs(target - total) < abs(diff): #current dist is closer than prev
                    diff = target - total #compare diff with abs, but assign the real diff
                if total < target:
                    l += 1 
                else:
                    r -= 1 
                
                if diff == 0 : # found the exact numbers
                    return target
        return target - diff #target - diff is the actual total 3 sum can be found in the nums
                



# previous solution

# class Solution:
#     def threeSumClosest(self, nums: 'List[int]', target: int) -> int:
#         def binFind(arr, v): #to find the closest element in arrr to v
#             if v >= arr[-1]:
#                 return arr[-1]
#             elif v <= arr[0]:
#                 return arr[0]
#             else:
#                 s = 0
#                 e = len(arr)-1
#                 diff = float('inf')
#                 while s<=e:
#                     mid = (s+e)//2
#                     if arr[mid] == v:
#                         return arr[mid]
#                     else:
#                         if abs(arr[mid] - v) < diff:
#                             diff = abs(arr[mid]-v)
#                             output = arr[mid]
#                         if arr[mid] > v:
#                             e = mid - 1
#                         elif arr[mid] <  v:
#                             s = mid + 1
#                 return output

#         output = None
#         diff = float('inf')
#         nums.sort()
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)-1):
#                 curr = nums[i] + nums[j]
#                 t = binFind(nums[j+1:], target - curr) #for each curr, find the closet to the remaining in arr
#                 if abs(curr + t - target) < diff: #current found is the closest to the target
#                     diff = abs(curr + t - target)
#                     output = curr + t
#         return output






# previous approach
# def threeSumClosest(nums: 'List[int]', target: int):
#     nums.sort()
#     i = len(nums) - 1
#     compare = float('inf')
#     value = None
#     while i > -1:
#         start = 0
#         end = i - 1
#         while start < end:
#             t = nums[i]+nums[start]+nums[end]
#             if abs(t-target ) < compare:
#                 compare = abs(t-target )
#                 value = t
#
#
#             if t<target:
#                 start +=1
#             elif t>target:
#                 end -=1
#             if t==target:
#                 return value
#
#         i-=1
#
#     return value
#
# print(threeSumClosest( [-1, 2, 1, -4],1))
# print(threeSumClosest( [-1,0,1,2,-1,-4],0))
# print(threeSumClosest( [1,2,4,8,16,32,64,128],82))
# print(threeSumClosest( [-3,-2,-5,3,-4],-1))
# print(threeSumClosest( [1,1,-1,-1,3],1))

