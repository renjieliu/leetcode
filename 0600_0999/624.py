class Solution:
    def maxDistance(self, arrays: 'List[List[int]]') -> int:
        # min for each arr, and maxx for each arr, sort, and check if they are from the same array
        minn = sorted([[i, a[0]] for i, a in enumerate(arrays)], key = lambda x: x[1]) 
        maxx = sorted([[i, a[-1]] for i, a in enumerate(arrays)], key = lambda x: x[1])
        # print(minn, maxx)
        if minn[0][0]!=maxx[-1][0]: #check if they are from the same array
            return maxx[-1][1] - minn[0][1]
        else:
            return max(maxx[-1][1] - minn[1][1], maxx[-2][1] - minn[0][1])
        



# previous approach
# class Solution:
#     def maxDistance(self, arrays: 'List[List[int]]') -> int:
#         maxx, minn = -float('inf'), float('inf')
#         loc = -1
#         for i, a in enumerate(arrays):
#             maxx = max(maxx, a[-1])
#             minn = min(minn, a[0])
#             if maxx == a[-1] and minn == a[0]:  # same array
#                 loc = i

#         if loc == -1:
#             return abs(maxx - minn)
#         else:
#             output = -float('inf')
#             for i, a in enumerate(arrays):
#                 if i != loc:
#                     output = max(output, abs(a[-1] - minn))
#                     output = max(output, abs(a[0] - maxx))
#             return output


