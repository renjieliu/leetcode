class Solution:
    def pacificAtlantic(self, heights: 'List[List[int]]') -> 'List[List[int]]': #O( MN | MN )
        def helper(r, c, heights, output): # check 4 directions, and see if the next cell can flow into current one
            output.add((r,c)) 
            direction = [[1,0], [0,-1], [-1, 0], [0,1]]
            for a, b in direction:
                if -1 < r+a < len(heights) and -1 < c+b < len(heights[0]) and heights[r+a][c+b] >= heights[r][c] and (r+a, c+b) not in output:
                    helper(r+a, c+b, heights, output)
        
        
        reach_pacific = set()
        reach_atlantic = set() 
        for r in range(len(heights)): 
            helper(r, 0, heights, reach_pacific)# all the elements in the first column can reach pacific 
            helper(r, len(heights[0])-1, heights, reach_atlantic) # all the elements in the final column can reach atlantic
        
        for c in range(len(heights[0])):
            helper(0, c, heights, reach_pacific)  #all the elements in the first row can reach pacific
            helper(len(heights)-1, c, heights, reach_atlantic)  #all the elements in the final row can reach atlantic
            
         
        return list(reach_pacific & reach_atlantic)
    
    


# previous solution

# class Solution:
#     def pacificAtlantic(self, matrix: 'List[List[int]]') -> 'List[List[int]]':
#         # Check if input is empty
#         if not matrix or not matrix[0]:
#             return []

#         # Initialize variables, including sets used to keep track of visited cells
#         num_rows, num_cols = len(matrix), len(matrix[0])
#         pacific_reachable = set()
#         atlantic_reachable = set()

#         def dfs(row, col, reachable):
#             # This cell is reachable, so mark it
#             reachable.add((row, col))
#             for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]: # Check all 4 directions
#                 new_row, new_col = row + x, col + y
#                 # Check if the new cell is within bounds
#                 if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
#                     continue
#                 # Check that the new cell hasn't already been visited
#                 if (new_row, new_col) in reachable:
#                     continue
#                 # Check that the new cell has a higher or equal height,
#                 # So that water can flow from the new cell to the old cell
#                 if matrix[new_row][new_col] < matrix[row][col]:
#                     continue
#                 # If we've gotten this far, that means the new cell is reachable
#                 dfs(new_row, new_col, reachable)

#         # Loop through each cell adjacent to the oceans and start a DFS
#         for i in range(num_rows):
#             dfs(i, 0, pacific_reachable)
#             dfs(i, num_cols - 1, atlantic_reachable)
#         for i in range(num_cols):
#             dfs(0, i, pacific_reachable)
#             dfs(num_rows - 1, i, atlantic_reachable)

#         # Find all cells that can reach both oceans, and convert to list
#         return list(pacific_reachable.intersection(atlantic_reachable))


# # class Solution:
# #     def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
# #         def dfs(dp, res, seen, arr, r, c, v):
# #             if r <= 0 or c <= 0: # reach pacific
# #                 res[0] = 1
# #             if r >= len(arr)-1 or c >=len(arr[0])-1: #reach atlantic
# #                 res[1] = 1
# #             if res == [1,1]:
# #                 return
# #             else:
# #                 direction = [[-1,0], [0,1], [1,0],[0,-1]] #up, right, down, left
# #                 for a, b in direction:
# #                     nxt_r = r+a
# #                     nxt_c = c+b
# #                     if (nxt_r,nxt_c) in dp:
# #                         if dp[(nxt_r,nxt_c)] == [1,1]:
# #                             res = [1,1]
# #                             return
# #                         else:
# #                             continue
# #                     elif (nxt_r,nxt_c) not in seen and 0 <= nxt_r <= len(arr)-1 and 0 <= nxt_c <= len(arr[0])-1 and v >= arr[nxt_r][nxt_c] :
# #                             seen.add((nxt_r,nxt_c))
# #                             dfs(dp, res, seen ,arr, nxt_r,nxt_c, arr[nxt_r][nxt_c])
# #                             seen.remove((nxt_r,nxt_c))
# #                             if res == [1,1]:
# #                                 return

# #         output = []
# #         dp = {}
# #         for r in range(len(matrix)):
# #             for c in range(len(matrix[0])):
# #                 res = [-1,-1]
# #                 seen = set()
# #                 seen.add((r,c))
# #                 dfs(dp, res, seen, matrix, r,c, matrix[r][c])
# #                 dp[(r,c)] = res
# #                 if res == [1,1]:
# #                     output.append([r,c])
# #         return output






