class Solution:
    def validMountainArray(self, arr: 'List[int]') -> bool:
        if len(arr) < 3: return False
        up = down = 0
        prev = arr[0]
        for i in range(1, len(arr)):
            curr = arr[i]
            if curr == prev:
                return False
            else:
                if curr > prev:  # up the hill
                    if down != 0:
                        return False
                    else:
                        up = 1
                elif curr < prev:  # down the hill
                    if up != 1:
                        return False
                    else:
                        down = 1
            prev = curr

        return True if down * up != 0 else False



# previous approach
# def validMountainArray(A: 'List[int]'):
#     if len(A) < 3:
#         return False
#
#     max = A[0]
#     pos = 0
#     for i in range(len(A)):
#         if A[i]> max:
#             max = A[i]
#             pos = i
#
#     if pos ==0 or pos == len(A)-1:
#         return False
#
#
#     for i in range(len(A)-1):
#         if i < pos and A[i]>=A[i+1]:
#             return False
#         if i>=pos and A[i+1]>=A[i]:
#             return False
#
#     return True
#
# print(validMountainArray([2,1]))
# print(validMountainArray([3,5,5]))
# print(validMountainArray( [0,3,2,1]))
#
