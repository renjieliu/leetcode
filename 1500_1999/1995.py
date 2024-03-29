class Solution:
    def countQuadruplets(self, nums: 'List[int]') -> int: #O(N2logN)
        hmp = {}
        for i in range(len(nums)): #O(N2)
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] not in hmp:
                    hmp[nums[i] + nums[j]] = []
                hmp[nums[i] + nums[j]].append(j)

        for k in hmp.keys(): #sort all the hmp.values() #O(NlogN)
            hmp[k].sort()

        cnt = 0
        for i in range(len(nums)-1, -1, -1): #O(N2logN)
            for j in range(i-1, -1,-1):
                curr = nums[i] - nums[j]
                if curr in hmp: # to find how many can be found
                    pos = bisect.bisect_left(hmp[curr], j)
                    #print(hmp[curr], j , pos)
                    cnt += pos if pos > 0 else 0
                    # for _ in hmp[curr]:
                    #     cnt +=1 if _ < j else 0
        return cnt


# previous approach
# class Solution:
#     def countQuadruplets(self, nums: 'List[int]') -> int: #O(N3)
#         hmp = {}
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] not in hmp:
#                     hmp[nums[i] + nums[j]] = []
#                 hmp[nums[i] + nums[j]].append(j)
#         cnt = 0
#         for i in range(len(nums)-1, -1, -1):
#             for j in range(i-1, -1,-1):
#                 curr = nums[i] - nums[j]
#                 if curr in hmp: # to find how many can be found
#                     for _ in hmp[curr]:
#                         cnt +=1 if _ < j else 0
#         return cnt



# previous approach
# class Solution:
#     def countQuadruplets(self, nums: 'List[int]') -> int: #O(N4)
#         cnt = 0
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     for m in range(k+1, len(nums)):
#                         if nums[i] + nums[j] + nums[k] - nums[m] == 0:
#                             cnt +=1
#         return cnt
#
#
#
