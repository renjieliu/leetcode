class Solution:
    def findLHS(self, nums: 'List[int]') -> int:
        hmp = {}
        for n in nums:
            if n not in hmp: hmp[n] = 0
            hmp[n] +=1
        output = 0
        for n in nums: #check how many (n-1, n), and how many (n, n+1) pair in the hmp
            if n-1 in hmp:
                output = max(output, hmp[n] + hmp[n-1])
            if n+1 in hmp:
                output = max(output, hmp[n] + hmp[n+1])
        return output




# previous approach
# def findLHS(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     x=sorted(nums)
#     print("sss") if x[0] + 1 in x else print("ffff")
#     print(x)
#     if x[-1] - x[0] <1:
#         return 0
#     elif x[-1] - x[0] ==1:
#         return len(x)
#
#
#
#     else:
#         LHS = list()
#         for i in range(0, len(x)):
#             if x[i] + 1 in x:
#                 LHS.append(x.index(x[i] + 1, -1) - i + 1)
#             else:
#                 LHS.append(0)
#
#     return max(LHS)
#
# print(findLHS([1,3,2,2,5,2,3,7]))
#
#
