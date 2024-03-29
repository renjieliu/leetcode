class Solution:
    def findPairs(self, nums: 'List[int]', k: int) -> int:
        counter = {}
        for n in nums:
            if n not in counter: #count each number occurrence
                counter[n] = 0
            counter[n] += 1 
        
        output = 0 
        for n, v in counter.items():
            if k == 0:
                output += 1 if v > 1 else 0  #if k == 0 and current number occurs more than once.
            else:
                output += 1 if n+k in counter else 0 # if n+k also appears in the nums
        return output



# previous approach

# class Solution:
#     def findPairs(self, nums: 'List[int]', k: int) -> int:
#         output = 0
#         hmp = {}
#         for n in nums:
#             if n not in hmp:
#                 hmp[n] = 0
#             hmp[n] += 1
#         for v in hmp.keys():
#             if k == 0:
#                 if hmp[v] > 1:
#                     output += 1
#             else:
#                 if v + k in hmp:  # only check v+k, to elimindate double counting
#                     output += 1
#         return output




    # previous solution
# def findPairs(nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: int
#     """
#     t = list()
#     g = list(nums)
#
#     if k == 0:
#         check = {}
#         count = 0
#         for n in nums:
#             if n in check.keys():
#                 check[n] += 1
#             else:
#                 check[n] = 1
#         for v in check.values():
#             if v > 1:
#                 count+=1
#         return count
#
#
#     elif k < 0:
#         return 0
#     else:
#         for x in nums:
#             t.append(x + k)
#         return len(set(t) & set(nums))
#
#
# print(findPairs([1,3,1,5,4], 0 ))
# print(findPairs([1,1,1,1,1], 0 ))