# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int: # O( NlogN | 1 )
        rows, cols = binaryMatrix.dimensions() # get dimensions
        def binFind(arr): # find the first 1 in arr 
            if arr[-1] == 0:
                return float('inf')
            elif arr[0] == 1:
                return 0
            else:
                s = 0 
                e = len(arr)-1 
                output = float('inf')
                while s <= e:
                    mid = s - (s-e)//2
                    if arr[mid] == 1:
                        output = mid 
                        e = mid - 1 
                    else:
                        s = mid + 1
                return output
        
        output = float('inf')
        for r in range(rows): # go through each row, with binary search to find first 1 in each row
            s = 0 
            e = cols-1
            while s <= e:
                mid = s - (s-e) // 2
                if binaryMatrix.get(r, mid) == 1:
                    output = min(output, mid)
                    if output == 0: # no need to continue, this is the leftmost column
                        return 0 
                    e = mid - 1
                else:
                    s = mid + 1 
        
        return output if output != float('inf') else -1 
    
    
    


    
    


# previous solution

# # """
# # This is BinaryMatrix's API interface.
# # You should not implement it, or speculate about its implementation
# # """
# #class BinaryMatrix(object):
# #    def get(self, row: int, col: int) -> int:
# #    def dimensions(self) -> list[]:

# class Solution:
#     def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
#         totalR, totalC = binaryMatrix.dimensions()
#         row_pool = []
#         for r in range(totalR):
#             if binaryMatrix.get(r, totalC-1) == 1 :
#                 row_pool.append(r)
#         if row_pool == []:
#             return -1
#         else:
#             output = float('inf')
#             for r in row_pool:
#                 s = 0
#                 e = totalC-1
#                 while s<=e:
#                     mid = (s+e)//2
#                     if binaryMatrix.get(r, mid) == 1:
#                         e = mid-1
#                         output = min(mid, output)
#                     else:
#                         s = mid + 1
#             return output





# previous approach
# # """
# # This is BinaryMatrix's API interface.
# # You should not implement it, or speculate about its implementation
# # """
# #class BinaryMatrix(object):
# #    def get(self, x: int, y: int) -> int:
# #    def dimensions(self) -> list[]:
#
# class Solution:
#     def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
#         dim = binaryMatrix.dimensions()
#         rows, cols = dim[0], dim[1]
#         output = float('inf')
#         for r in range(rows):
#             if binaryMatrix.get(r,cols-1) == 0:
#                 continue
#             else:
#                 s = 0
#                 e = cols - 1
#                 loc = -1
#                 while s<=e: # bin search find the first non-zero element
#                     mid = (s+e)//2
#                     if binaryMatrix.get(r,mid) == 0:
#                         s = mid +1
#                     else:
#                         loc = mid
#                         e = mid -1
#                 output = min(output,loc)
#         return output if output != float('inf') else -1
#
#