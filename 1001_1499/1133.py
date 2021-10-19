class Solution:
    def largestUniqueNumber(self, A: 'List[int]') -> int:
        hmp = {}
        for a in A:
            if a not in hmp:
                hmp[a] = 0
            hmp[a]+=1
        output = -1
        for k in list(hmp.keys()):
            if hmp[k] == 1:
                output = max(output, k)
        return output

# previous approach
# class Solution:
#     def largestUniqueNumber(self, A: 'List[int]') -> int:
#         hmp = {}
#         output = [-1]  # default return value
#         for a in A:
#             if a not in hmp:
#                 hmp[a] = 0
#             hmp[a] += 1
#         for k, v in hmp.items():
#             if v == 1:
#                 output.append(k)
#         return max(output)
