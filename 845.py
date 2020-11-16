class Solution:
    def longestMountain(self, A: 'List[int]') -> int:
        if len(A) < 3: return 0
        output = 0
        if A[1] > A[0]:
            up = 2
            down = 1
        elif A[1] == A[0] or A[1] < A[0] :
            up = down = 1
        prev = A[1]
        for a in A[2:]:
            if a > prev: # up hill
                if down >=2: #starting up the hill
                    up = 2
                else:
                    up += 1
                down = 1 #set current as the down point
            elif a < prev: #down hill
                down += 1
                if up >= 2:
                    output = max(output, up+down-1) #the peak is counted twice
            elif a == prev:
                up = 1
                down = 1
            prev = a
            #print(a, output, up, down)
        return output


# previous approach
# class Solution:
#     def longestMountain(A: 'List[int]'):
#         if len(A) < 3:
#             return 0
#         else:
#             r = 1
#             prev_up, output = 0, 0
#             up = 0
#             down = 0
#             while r < len(A):
#                 if A[r] > A[r - 1]:
#                     if up > 0:  # it's upping
#                         up += 1
#                     elif up == 0:  # it was down, now it's up
#                         # output = max(prev_up+down, output)
#                         down = 0
#                         up = 2
#
#                 elif A[r] < A[r - 1]:
#                     if down > 0:  # it's downing
#                         down += 1
#                         output = max(prev_up + down, output)
#                     elif down == 0 and up > 0:
#                         prev_up = up
#                         up = 0  # it was up, now it's down
#                         down = 1  # start downing, the peak point has been counted in the up, don't need to double count
#                         output = max(prev_up + down, output)
#
#                 elif A[r] == A[r - 1]:
#                     up = 0
#                     down = 0
#
#                 r += 1
#
#         return output
