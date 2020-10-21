class Solution:
    def asteroidCollision(self, asteroids: 'List[int]') -> 'List[int]':
        if not asteroids: return []
        left = []
        right = []
        for a in asteroids:
            exploded = 0
            if a > 0:
                right.append(a)
            if a < 0:
                while right and right[-1] <= abs(a):
                    r = right.pop()
                    if abs(r) == abs(a):
                        exploded = 1
                        break
                if right == [] and exploded == 0:
                    left.append(a)
            # print(left, right, a )
        return left + right


# Previous approach
# def asteroidCollision(asteroids: 'List[int]'):
#     neg_left = []
#     pos_right = []
#     for i in asteroids[::-1]:
#         crash = 0
#         if i < 0:
#             neg_left.append(i)
#
#         elif i > 0:
#             while neg_left != []:
#                 if abs(neg_left[-1]) < abs(i):
#                     neg_left.pop()
#                 elif abs(neg_left[-1]) == abs(i):
#                     neg_left.pop()
#                     crash = 1
#                     break
#                 elif abs(neg_left[-1]) > abs(i):
#                     break
#
#             if len(neg_left) == 0 and crash == 0:
#                 pos_right.append(i)
#
#     return neg_left[::-1] + pos_right[::-1]
#
