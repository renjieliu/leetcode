class Solution:
    def minimumTotal(self, triangle: 'List[List[int]]') -> int: #O(N**2 | N**2)
        dp = [[0] * (len(triangle[-1]) + 1)] #pad one more row, to avoid additional "if row number"
        for row in triangle[::-1]: #bottom up, to find the min cost path sum from current to bottom
            dp.append([])
            for c in range(len(row)):
                dp[-1].append(row[c] + min(dp[-2][c], dp[-2][c+1])) # compare with the previous row in the dp
        return dp[-1][-1]  # return the last element. With bottom up, this is the top element in the original triangle.





# class Solution:
#     def minimumTotal(self, triangle: 'List[List[int]]') -> int:
#         def helper(hmp, arr, r, c ):
#             if (r,c) in hmp:
#                 return hmp[(r,c)]
#             else:
#                 if r == len(arr)-1:
#                     hmp[(r,c)] = arr[r][c]
#                 else:
#                     A = arr[r][c] + helper(hmp, arr, r+1, c)
#                     B = arr[r][c] + helper(hmp, arr, r+1, c+1)
#                     hmp[(r,c)] = min(A,B)
#                 return hmp[(r,c)]
#         hmp = {}
#         helper(hmp, triangle, 0, 0)
#         return hmp[(0,0)]


