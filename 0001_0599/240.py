class Solution:
    def searchMatrix(self, matrix: 'List[List[int]]', target: int) -> bool:
        def bin(arr,n):
            s = 0
            e = len(arr)-1
            while s <=e:
                mid = s - (s-e)//2
                if arr[mid] == n:
                    return True
                else:
                    if arr[mid] < n:
                        s = mid +1
                    elif arr[mid] > n:
                        e = mid -1
            return False

        for r in matrix:
            if bin(r,target)==True:
                return True
        return False



# previous approach
# class Solution:
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         if len(matrix) == 0 or len(matrix[0]) == 0:
#             return False
#         r = 0
#         while r < len(matrix):
#             if matrix[r][0] == target:
#                 return True
#             elif matrix[r][0] > target:
#                 return False
#             else:  # binary search in the current row
#                 s = 0
#                 e = len(matrix[0]) - 1
#                 while s <= e:
#                     mid = s - (s - e) // 2
#                     if matrix[r][mid] == target:
#                         return True
#                     elif matrix[r][mid] > target:
#                         e = mid - 1
#                     else:
#                         s = mid + 1
#             r += 1
#         return False

