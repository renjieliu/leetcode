class Solution:
    def maxDistToClosest(self, seats: 'List[int]') -> int:
        one_pos=-float('inf') 
        left = []
        for i, c in enumerate(seats): # record the closest 1 on the left
            if c == 1 :
                one_pos = i
            left.append(i-one_pos)
        
        one_pos=float('inf')
        output = -float('inf')
        
        for i in range(len(seats)-1, -1, -1): #record the closest 1 on the right, and compare with left
            if seats[i] == 1:
                one_pos = i
            curr = min(left[i], one_pos-i) # if sit here, what's the distance
            output = max(output, curr) #compare with global output
        return output

    


# previous approach

# class Solution:
#     def maxDistToClosest(self, seats: 'List[int]') -> int:
#         left_arr = []
#         right_arr = [0] * len(seats)
#         left = 0
#         for i in range(len(seats)):
#             if seats[i] == 1:
#                 left = i
#             left_arr.append(i - left)

#         right = len(seats) - 1
#         for i in range(len(seats) - 1, -1, -1):
#             if seats[i] == 1:
#                 right = i
#             right_arr[i] = (right - i)

#         if seats[0] == 0:
#             left_arr[0] = float('inf')
#         if seats[-1] == 0:
#             right_arr[-1] = float('inf')

#         output = 0
#         # print(left_arr)
#         # print(right_arr)
#         for i in range(len(seats)):
#             if seats[i] != 1:
#                 output = max(output, min(left_arr[i], right_arr[i]))
#         return output

# # Previous approach
# # def maxDistToClosest(seats: 'List[int]'):
# #     cnt = 0
# #     max = 0
# #
# #     if seats[0] == 0:
# #         for i in seats:
# #             if i == 0:
# #                 max += 1
# #             else:
# #                 break
# #
# #     for i in seats:
# #         if i == 0:
# #             cnt += 1
# #         else:
# #
# #             distance = cnt // 2 if cnt % 2 == 0 else cnt // 2 + 1
# #
# #             if max < distance:
# #                 max = distance
# #
# #             cnt = 0
# #     if i == 0 and max < cnt:  # the last seat is 0
# #         max = cnt
# #
# #     return max
# #
# #
# # print(maxDistToClosest( [1,0,0,0,1,0,1]))
# # print(maxDistToClosest(  [1,0,0,0]))
# # print(maxDistToClosest(  [0,0,0,1]))
# # print(maxDistToClosest(  [0,0,0,0,1,0,0,1,1,1,0]))
# #
# #
