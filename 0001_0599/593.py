class Solution:
    def validSquare(self, p1: 'List[int]', p2: 'List[int]', p3: 'List[int]', p4: 'List[int]') -> bool:
        dist = lambda x, y: ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)
        arr = []
        arr.append(dist(p1, p2))
        arr.append(dist(p1, p3))
        arr.append(dist(p1, p4))
        arr.append(dist(p2, p3))
        arr.append(dist(p2, p4))
        arr.append(dist(p3, p4))
        arr.sort()  # first 4 edges equal, last 2 should be equal, and a2+b2=c2 (diagnal2 = edge1**2 + edge2**2 )
        # print(arr)
        if arr[0] != 0 and arr[0] == arr[1] == arr[2] == arr[3]:  # the shortest edge should not be 0
            if arr[4] == arr[5] and arr[4] == (arr[0] + arr[1]):
                return True
        return False

# previous approach
# def distance(p1, p2):
#     return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
#
#
# def validSquare(p1: 'List[int]', p2: 'List[int]', p3: 'List[int]', p4: 'List[int]'):
#     # to check if duplicated points
#     sp1 = str(p1[0]) + '-' + str(p1[1])
#     sp2 = str(p2[0]) + '-' + str(p2[1])
#     sp3 = str(p3[0]) + '-' + str(p3[1])
#     sp4 = str(p4[0]) + '-' + str(p4[1])
#
#     if len(set([sp1, sp2, sp3, sp4])) != 4:
#         return False
#
#     # sc 1. check if the points is standup rectangle.
#
#     # for each point, there should be exactly another 1 point with x= current[x] and 1 point with y = current[y]
#     sc_1 = 1
#     # 1. for P1
#     cnt_x = 0
#     cnt_y = 0
#     for i in [p2, p3, p4]:
#         if i[0] == p1[0]:
#             cnt_x += 1
#         if i[1] == p1[1]:
#             cnt_y += 1
#     # 2. for P2
#     if cnt_x == cnt_y == 1:
#         cnt_x = 0
#         cnt_y = 0
#         for i in [p1, p3, p4]:
#             if i[0] == p2[0]:
#                 cnt_x += 1
#             if i[1] == p2[1]:
#                 cnt_y += 1
#     else:
#         sc_1 = 0
#
#     # 3. for P3
#     if cnt_x == cnt_y == 1:
#         cnt_x = 0
#         cnt_y = 0
#         for i in [p1, p2, p4]:
#             if i[0] == p3[0]:
#                 cnt_x += 1
#             if i[1] == p3[1]:
#                 cnt_y += 1
#     else:
#         sc_1 = 0
#
#     # 4. for P4
#     if cnt_x == cnt_y == 1:
#         cnt_x = 0
#         cnt_y = 0
#         for i in [p1, p2, p3]:
#             if i[0] == p4[0]:
#                 cnt_x += 1
#             if i[1] == p4[1]:
#                 cnt_y += 1
#
#     if cnt_x == cnt_y == 1:
#         sc_1 = 1
#     else:
#         sc_1 = 0
#
#     if sc_1 ==1:
#         #find lowerleft corner and check if edge length is same
#         points = sorted([p1, p2, p3, p4])
#         if distance(points[0],points[1]) == distance(points[0],points[2]):
#             return True
#         else:
#             return False
#
#     # sc 2. If the shape is tilted
#     sc_2 = 1
#     # 1 find the left most point
#     minX = float('inf')
#     for i in [p1, p2, p3, p4]:
#         if i[0] < minX:
#             leftMost = i
#             minX = i[0]
#
#     # 2 find the right most point
#     maxX = -float('inf')
#     for i in [p1, p2, p3, p4]:
#         if i[0] > maxX:
#             rightMost = i
#             maxX = i[0]
#
#     other2 = []
#
#     for i in [p1, p2, p3, p4]:
#         if i != leftMost and i != rightMost:
#             other2.append(i)
#
#     if distance(leftMost, other2[0]) == distance(leftMost, other2[1]) == distance(rightMost, other2[1]) == distance(
#             rightMost, other2[0]):
#         if distance(other2[0], other2[1]) == distance(leftMost, other2[0]) + distance(leftMost, other2[
#             1]):  # a2+b2 =c2 --> to check if the angle is 90 degree
#             return True
#
#     return False
#
#
# # 2
# print(validSquare(p1=[0, 0], p2=[1, 1], p3=[1, 0], p4=[0, 1]))
# print(validSquare(p1=[0, 0], p2=[1, 1], p3=[1, 0], p4=[1, 1]))
# print(validSquare([1, 0],
#                   [-1, 0],
#                   [0, 1],
#                   [0, -1]))
# print(validSquare([0,0],
#                 [5,0],
#                 [5,4],
#                 [0,4]))
