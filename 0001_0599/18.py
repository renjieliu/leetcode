class Solution: #O(n2logN)
    def fourSum(self, nums: 'List[int]', target: int) -> 'List[List[int]]':
        def binFind(arr, pos):  # to find if any arr[0] > pos
            if pos < arr[0][0]:
                return 0
            elif pos > arr[-1][0]:
                return -1
            else:
                s = 0
                e = len(arr) - 1
                output = -1
                while s <= e:
                    mid = (s + e) // 2
                    if arr[mid][0] < pos:
                        s = mid + 1
                    else:
                        output = mid
                        e = mid - 1
                return output

        output = []
        nums.sort()
        hmp = {}
        for i in range(len(nums)):  # get the last combination sum loc
            for j in range(i + 1, len(nums)):
                curr = nums[i] + nums[j]
                if curr not in hmp:
                    hmp[curr] = {}
                hmp[curr][(nums[i], nums[j])] = i

        lkp = {}
        for k, v in hmp.items():  # clean up the items in hmp, to the format of (location, (i, j))
            lkp[k] = []
            for (a, b), loc in v.items():
                lkp[k].append([loc, [a, b]])

        for k, v in lkp.items():  # sort the v, to be used for the binary search
            v.sort(key=lambda x: x[0])

        pool = []
        seen = set()
        for i in range(len(nums)):  # for each 2 pointers, check if can find the remaining in the lkp.
            for j in range(i + 1, len(nums)):
                if (nums[i], nums[j]) not in seen:
                    curr = nums[i] + nums[j]
                    if target - curr in lkp:
                        loc = binFind(lkp[target - curr], j + 1)
                        if loc != -1:
                            pool.append([nums[i], nums[j],
                                         lkp[target - curr][loc:]])  # get all the valid combinations from the lkp

        output = []
        added = set()
        for i, j, follow in pool:  # follow is [location, [a, b] ]
            for loc, [a, b] in follow:  # to check if this is a unique combination.
                x = tuple(sorted([i, j, a, b]))
                if x not in added:
                    output.append(list(x))
                    added.add(x)
        return output

# previous approach: O(N3)
# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         nums.sort()  # O(N3), fixed first 3, find 4th, and check if first 2 and 3 is seen to speed up.
#         seen = set()
#         hmp = {}
#         for i, n in enumerate(nums):
#             hmp[n] = [i]
#
#         output = []
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if (nums[i], nums[j]) not in seen:
#                     seen.add((nums[i], nums[j]))
#                     for k in range(j + 1, len(nums)):
#                         if (nums[i], nums[j], nums[k]) not in seen:
#                             rem = target - sum((nums[i], nums[j], nums[k]))
#                             if rem in hmp and hmp[rem][0] > k:
#                                 output.append([nums[i], nums[j], nums[k], nums[hmp[rem][0]]])
#                                 seen.add((nums[i], nums[j], nums[k]))
#         return output
#
