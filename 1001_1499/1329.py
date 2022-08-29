class Solution:
    def diagonalSort(self, mat: 'List[List[int]]') -> 'List[List[int]]': #O( MNlogM | M ) M = len(mat), N = len(mat[0])
        currLoc = []
        currVal = []
        ptr = len(mat) + len(mat[0])-1 # have the pointer at the left bottom
        while ptr > 0:
            r = max(0, ptr - len(mat[0])) # get the starting r
            c = 0 if ptr >= len(mat[0]) else (len(mat[0]) - ptr - 1)  # get the starting c
            while True: #keep taking current diagonal numbers
                currLoc.append([r,c])
                currVal.append(mat[r][c])
                r += 1 
                c += 1 
                if r >= len(mat) or c >= len(mat[0]):
                    break
            currVal.sort()
            for r, c in currLoc: #put back to the mat
                mat[r][c] = currVal.pop(0)
            currLoc = []
            currVal = []           
            ptr -= 1
            
        return mat
            

            


# previous solution

# class Solution:
#     def diagonalSort(self, mat: 'List[List[int]]') -> 'List[List[int]]':
#         def pickAndSortAndPlaceBack(arr, sr, sc):
#             temp = []
#             valid = lambda arr, r, c: True if 0 <= r < len(arr) and 0 <= c < len(arr[0]) else False
#             r = sr
#             c = sc
#             while valid(arr, r, c):
#                 temp.append(arr[r][c])
#                 r += 1
#                 c += 1
#             temp.sort()
#             while valid(arr, sr, sc):
#                 arr[sr][sc] = temp.pop(0)
#                 sr += 1
#                 sc += 1

#         for r in range(len(mat) - 1, -1, -1):
#             pickAndSortAndPlaceBack(mat, r, 0)
#         for c in range(1, len(mat[0])):
#             pickAndSortAndPlaceBack(mat, 0, c)

#         return mat





# previous approach

# class Solution:
#     def diagonalSort(self, mat: 'List[List[int]]') -> 'List[List[int]]':
#         check = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]  # to see if current cell has been sorted
#         r = 0
#         while r < len(mat):  # go thru each cell, and find the next cells. sort them and put them back
#             c = 0
#             while c < len(mat[0]):
#                 if check[r][c] == 0:
#                     temp_co = []
#                     temp_value = []
#                     sr = r
#                     sc = c
#                     while sr < len(mat) and sc < len(mat[0]):
#                         temp_co.append([sr, sc])
#                         temp_value.append(mat[sr][sc])
#                         check[sr][sc] = 1
#                         sr += 1
#                         sc += 1
#                     temp_value.sort()
#                     i = 0
#                     while i < len(temp_value):
#                         mat[temp_co[i][0]][temp_co[i][1]] = temp_value[i]
#                         i += 1
#                 c += 1
#             r += 1
#         return mat
