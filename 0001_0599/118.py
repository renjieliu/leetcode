class Solution:
    def generate(self, numRows: int) -> 'List[List[int]]': #O( numRows**2 | numRows**2 )
        dp = [[1]]
        for r in range(1, numRows): #go through each row. 
            curr = [1] #initiate current row
            for c in range(1, r): #add r-2 number elements to current row
                curr.append(dp[r-1][c-1] + dp[r-1][c] )  # prev row col-1 + prev row col
            curr.append(1) # add the last element
            dp.append(curr)
        return dp





# previous solution

# class Solution:
#     def generate(self, numRows: int) -> 'List[List[int]]':
#         dp = [[1]]
#         for row in range(2, numRows+1):
#             dp.append([1])
#             for i in range(1, row-1):
#                 dp[-1].append(dp[-2][i-1] + dp[-2][i])
#             dp[-1].append(1)
#         return dp




# previous approach
# def generate(numRows: int):
#     if numRows ==0:
#         return []
#     if numRows ==1 :
#         return [[1]]
#     elif numRows == 2:
#         return [[1],[1,1]]
#
#     else:
#         output=[[1], [1,1]]
#         for i in range(2,numRows): #for the rows.
#             temp = [1]
#             for j in range(0,i-1): # for the columns
#                 t = output[i-1][j] + output[i-1][j+1]
#                 temp.append(t)
#             temp.append(1)
#             output.append(temp)
#
#     return output
#
#
# print(generate(1))
# print(generate(2))
# print(generate(3))
# print(generate(4))
# print(generate(5))
# print(generate(6))
#
#
#
