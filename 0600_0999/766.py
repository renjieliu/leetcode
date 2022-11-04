class Solution:
    def isToeplitzMatrix(self, matrix: 'List[List[int]]') -> bool: # O( MN | 1 )
        for r in range(len(matrix)-1): # go through each cell, and check if current == (r+1, c+1)
            for c in range(len(matrix[0])-1):
                if matrix[r][c] != matrix[r+1][c+1]:
                    return False
        return True 




# previous solution

# class Solution:
#     def isToeplitzMatrix(self, matrix: 'List[List[int]]') -> bool: # O( MN | 1 )
#         for i in range(len(matrix)+len(matrix[0])-1, -1, -1): # start from the left lower corner
#             r = max(0, i - len(matrix[0])) # if it reaches the first row
#             if i - len(matrix[0]) >= 0: # first row, first element
#                 c = 0 
#             else:
#                 c = len(matrix[0])-i-1 #iterate on the first row
#             #print(r, c)
#             ref = matrix[r][c] # current element as reference
#             while r < len(matrix) and c < len(matrix[0]):  #check if the diagonal has the same element.
#                 if matrix[r][c] != ref:
#                     return False
#                 r+=1
#                 c+=1
       
#         return True 
    

            

# previous solution

# def isToeplitzMatrix(matrix):
#     """
#     :type matrix: List[List[int]]
#     :rtype: bool
#     """
#     checkLength = len(matrix[0])-1
#     for i in range(0, checkLength):
#         for j in range(0, len(matrix)-1):
#             if matrix[j][i] != matrix[j+1][i+1]:
#                 return False

#     return True



# print(isToeplitzMatrix(  [[1,2,3,4],[5,1,2,3],[9,5,1,2]] ))
# print(isToeplitzMatrix(  [[1,2],[2,2]] ))





