class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int: # O( 1 | 1 )
        def overlap(left, right): #[lowerLeftX, lowereftY, upperRightX, upperRightY] 
            if right[0] >= left[2] or right[1] >= left[3] or left[1] >= right[3]: # no overlapping at all
                return 0
            else:
                X_overlap = abs( max(left[0], right[0]) - min(left[2], right[2]) ) # X overlapped length
                Y_overlap = abs( max(left[1], right[1]) - min(left[3], right[3]) ) # Y overlapped length
                return X_overlap*Y_overlap
        
        baseArea = (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1) # areas both rectangles covers
        if ax1 <= bx1:
            return baseArea - overlap([ax1, ay1, ax2, ay2], [bx1, by1, bx2, by2])
        else:
            return baseArea - overlap([bx1, by1, bx2, by2], [ax1, ay1, ax2, ay2]) 
  



# previous solution

# class Solution:
#     def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
#         r1 = [[A, B], [C, D]]
#         r2 = [[E, F], [G, H]]
#         s1 = abs(r1[1][0] - r1[0][0]) * abs(r1[1][1] - r1[0][1])
#         s2 = abs(r2[1][0] - r2[0][0]) * abs(r2[1][1] - r2[0][1])
#         if r2[0][0] >= r1[1][0] or r2[1][0] <= r1[0][0] or r2[0][1] >= r1[1][1] or r2[1][1] <= r1[0][
#             1]:  # no overlapping
#             return s1 + s2
#         elif (r1[0][0] <= r2[0][0] <= r2[1][0] <= r1[1][0] and r1[0][1] <= r2[0][1] <= r2[1][1] <= r1[1][1]) \
#                 or (r2[0][0] <= r1[0][0] <= r1[1][0] <= r2[1][0] and r2[0][1] <= r1[0][1] <= r1[1][1] <= r2[1][
#             1]):  # complete overlapping
#             return max(s1, s2)
#         else:  # partial overlapping
#             x1 = max(r1[0][0], r2[0][0])  # for the left X, which is the max
#             x2 = min(r1[1][0], r2[1][0])  # for the right X, which is the min
#             x = abs(x2 - x1)
#             y1 = max(r1[0][1], r2[0][1])  # for the lower y, which is the max
#             y2 = min(r1[1][1], r2[1][1])  # for the upper y, which is the min
#             y = abs(y2 - y1)
#             return s1 + s2 - x * y

