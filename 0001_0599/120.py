class Solution:
    def minimumTotal(self, triangle: 'List[List[int]]') -> int: #O(N**2 | N**2)
        dp = [[0] * (len(triangle[-1]) + 1)] #pad one more row, to avoid additional "if row number"
        for row in triangle[::-1]: #bottom up, to find the min cost path sum from current to bottom
            dp.append([])
            for c in range(len(row)):
                dp[-1].append(row[c] + min(dp[-2][c], dp[-2][c+1])) # compare with the previous row in the dp
        return dp[-1][-1]  # return the last element. With bottom up, this is the top element in the original triangle.



# previous solution

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


# previous solution

# class Solution:
#     def minimumTotal(self, triangle: 'List[List[int]]') -> int:
#         if len(triangle)==1 :
#             return min(triangle[0])
#         else:
#             path =0
#             output = triangle.copy()
#             output[1][0] += output[0][0]
#             output[1][1] += output[0][0]
#             for i in range(2, len(triangle)):
#                 for j in range(len(triangle[i])):
#                     if j==0:
#                         output[i][j] += output[i-1][0]
#                     elif j==len(triangle[i])-1:
#                         output[i][j] += output[i-1][-1]
#                     else:
#                         output[i][j] += min(output[i-1][j], output[i-1][j-1])

#             return min(output[-1])



