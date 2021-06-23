class Solution:
    def maxDepthBST(self, order: 'List[int]') -> int:
        arr = []
        hmp = {}
        for v in order:
            pos = bisect.bisect_left(arr, v)
            if pos == 0:
                if arr:
                    hmp[v] = hmp[arr[0]] + 1
                else:
                    hmp[v] = 1
            elif pos == len(arr):
                hmp[v] = hmp[arr[-1]] + 1
            else:
                hmp[v] = max(hmp[arr[pos-1]], hmp[arr[pos]]) + 1
            arr.insert(pos, v)
        return max(hmp.values())


# previous approach
# from sortedcontainers import SortedDict
#
# class Solution:
#     def maxDepthBST(self, order: List[int]) -> int:
#         # python way for binary treemap
#         depths = SortedDict()
#         # add dummy bounds to avoid extra ifs
#         depths[-math.inf] = 0
#         depths[math.inf] = 0
#
#         # for every value find bounds and take the lowest depth + 1
#         # put the value back to depths
#         for x in order:
#             i = depths.bisect_left(x)
#             depths[x] = 1 + max(depths.values()[i - 1:i + 1])
#         # return the maximum value so far
#         return max(depths.values())


# below is my approach, same idea as above 2, but got TLE
# from sortedcontainers import SortedDict
# class Solution:
#     def maxDepthBST(self, order: List[int]) -> int:
#         def binFindLess(arr, v): #find the closet smaller item in the map
#             if v < arr[0]:
#                 return -1
#             elif v > arr[-1]:
#                 return len(arr)-1
#             else:
#                 s = 0
#                 e = len(arr)-1
#                 output = -1
#                 while s<=e:
#                     mid = (s+e)//2
#                     if arr[mid] < v:
#                         output = mid
#                         s = mid + 1
#                     else:
#                         e = mid - 1
#                 return output

#         depth = SortedDict() #all the keys are sorted. Check the level of left number inserted, and check the right.
#         depth[order[0]] = 1
#         for v in order[1:]:
#             left = binFindLess(depth.keys(), v)
#             if left == -1: #smaller than all
#                 depth[v] = depth[depth.keys()[0]] + 1
#             elif left == len(depth.keys())-1: #larger than all
#                 depth[v] = depth[depth.keys()[-1]] +1
#             else: # 1+ max(left, right). The one to be inserted will not be on the same level of left or right, will always be one level below
#                   # if 12-7-22, 7 and 22 are children of 12, if to insert 8, 8 will be left of 22 or right of 7.
#                   # if 12 --> 7 and 22 are on different tree, the closet number on the right is 12. we can only add 8 to the left tree, vice versa.
#                 depth[v] = 1 + max(depth[depth.keys()[left]], depth[depth.keys()[left+1]]) #left is the one smaller than v, left+1 is the smallest > v
#             #print(v, left, depth)
#         return max(depth.values())







