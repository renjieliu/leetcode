class Solution:
    def canFormArray(self, arr: 'List[int]', pieces: 'List[List[int]]') -> bool:
        for p in pieces:
            i = 0
            while i < len(arr) + 1 - len(p):
                if arr[i: i + len(p)] == p:
                    arr = arr[:i] + arr[i + len(p):]
                i += 1
        if arr == []:
            return True
        else:
            return False

#previous approach
# class Solution:
#     def canFormArray(self, arr: 'List[int]', pieces:' List[List[int]]') -> bool:
#         for p in pieces:
#             i = 0
#             while i < len(arr) + 1 - len(p):
#                 if arr[i: i + len(p)] == p:
#                     arr = arr[:i] + arr[i + len(p):]
#                 i += 1
#         if arr == []:
#             return True
#         else:
#             return False
