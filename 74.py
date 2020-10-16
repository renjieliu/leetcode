class Solution:
    def searchMatrix(self, matrix: 'List[List[int]]', target: int) -> bool:
        def bin(arr, val):
            s = 0
            e = len(arr) - 1
            while s <= e:
                mid = s - (s - e) // 2
                if arr[mid] == val:
                    return mid
                elif arr[mid] > val:
                    e = mid - 1
                elif arr[mid] < val:
                    s = mid + 1
            return -1

        for arr in matrix:
            if arr and arr[0] <= target <= arr[-1]:
                if bin(arr, target) != -1:
                    return True
            else:
                continue
        return False


# previous approach
# class Solution:
#     def searchMatrix(self, matrix: 'List[List[int]]', target: int) -> bool:
#         if len(matrix) == 0 or len(matrix[0]) == 0:
#             return False
#         for r in range(len(matrix)):
#             if matrix[r][0] == target:
#                 return True
#             elif matrix[r][0] > target:
#                 if r == 0:
#                     return False
#                 else:
#                     for c in range(len(matrix[0])):
#                         if matrix[r - 1][c] == target:  # check in the previous row
#                             return True
#                     return False  # if cannot be found in the previous row, then return false
#
#         if matrix[-1][0] <= target:  # Check last line of the matrix
#             for i in matrix[-1]:
#                 if i == target:
#                     return True
#
#         return False
