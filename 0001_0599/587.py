# https://leetcode.com/problems/erect-the-fence/discuss/1442027/Python-short-Graham-scan-%2B-follow-up-explained
# What we actually need to find is convex hull of given points. There are different ways how to do it: the simplest is Jarvis Algorithm with O(mn) complexity, where n is total number of points and m is number of points in convex hull. I prefer Graham scan, which use the idea of angle sweep. We need to choose the most left point as starting point. Then we need to sort points with respect to its angle, and if we have the same angle, then we need to sort points by (-p[1], p[0]) - in this way we can be sure that we traverse points in correct order. Then we keep stack with points and check orientation of triangle, using cross function and if orientation is negative, then we pop the point ans[-2]. Please go to wikipedia for more details.

# Note, that in this problem our convex hull contains point on border, if we do not need it we need to use cross(*ans[-3:]) <= 0 instead and points.sort(key=lambda p: (atan2(p[1]-start[1], p[0]-start[0]), p[0])), I am not 100 sure though, I did not test it a lot.

# Complexity
# Time complexity is O(n log n), space complexity is O(n).


class Solution:
    def outerTrees(self, trees: 'List[List[int]]') -> 'List[List[int]]':
        def cross(p1, p2, p3):
            return (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])

        start = min(trees)
        trees.pop(trees.index(start))
        trees.sort(key=lambda p: (atan2(p[1]-start[1], p[0]-start[0]), -p[1], p[0]))

        ans = [start]
        for p in trees:
            ans.append(p)
            while len(ans) > 2 and cross(*ans[-3:]) < 0:
                ans.pop(-2)
        return ans


# class Solution: # my approach, failed test cases.
#     def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
#         #find 4 points for up, left, bottom and right
#         #form 4 lines, upleft, leftbottom, bottomright, upright
#         #check if the point are in the area formed by the 4 lines
#         #if not, then add the point
#         if len(trees) < 4:
#             return trees
#         trees.sort(key = lambda x: x[1])
#         trees.sort(key = lambda x: x[0])

#         left = trees[0]
#         down = trees[1]
#         up = trees[-1]
#         right = trees[-2]

#         line_k = lambda p1, p2: 0 if 0==(p1[0] - p2[0]) else (p1[1] - p2[1]) / (p1[0] - p2[0])
#         line_b = lambda p1, k: p1[1] - k*p1[0]
#         upleft_k = line_k(up, left)
#         upleft_b = line_b(left, upleft_k)
#         #print(up, left,upleft_k,upleft_b  )
#         leftdown_k = line_k(left, down)
#         leftdown_b = line_b(down, leftdown_k)
#         downright_k  = line_k(down, right)
#         downright_b = line_b(right, downright_k)
#         upright_k = line_k(up, right)
#         upright_b = line_b(right,upright_k)
#         output = []
#         # print(upright_k, upright_b)
#         for a , b in trees:

#             if b >=a*upleft_k+upleft_b \
#             or b <= a*leftdown_k+leftdown_b \
#             or b <=a*downright_k+downright_b \
#             or b >= a*upright_k+upright_b:
#                   output.append([a,b])

#         return output
