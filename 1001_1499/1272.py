class Solution:
    def removeInterval(self, intervals: 'List[List[int]]', toBeRemoved: 'List[int]') -> 'List[List[int]]':
        output = []
        for start, end in intervals:
            if end <= toBeRemoved[0] or start >= toBeRemoved[1]:
                output.append([start, end])
            else:
                if toBeRemoved[0] <= start <= toBeRemoved[1] and toBeRemoved[0] <= end <= toBeRemoved[1]:
                    continue

                elif start <= toBeRemoved[0] and end >= toBeRemoved[1]:
                    if start != toBeRemoved[0]:
                        output.append([start, toBeRemoved[0]])
                    if end != toBeRemoved[1]:
                        output.append([toBeRemoved[1], end])

                elif toBeRemoved[0] <= start <= toBeRemoved[1]:
                    s = toBeRemoved[1]
                    if s != end:
                        output.append([s, end])

                elif toBeRemoved[0] <= end <= toBeRemoved[1]:
                    e = toBeRemoved[0]
                    if start != e:
                        output.append([start, e])
        return output


#previous approach
# class Solution:
#     def removeInterval(self, intervals: 'List[List[int]]', toBeRemoved: 'List[int]') -> 'List[List[int]]':
#         stk = []
#         r = toBeRemoved
#         for i in intervals:
#             if i[0] <= r[0] <= i[1] and i[0] <= r[1] <= i[1]:  # the entire removal is within the current range
#                 stk.append([i[0], r[0]])
#                 stk.append([r[1], i[1]])
#
#             elif r[0] <= i[0] <= r[1] and r[0] <= i[1] <= r[1]:  # current i need to be removed
#                 continue
#
#             elif i[0] <= r[0] <= i[1]:  # the removal start point is within the curret range
#                 stk.append([i[0], r[0]])
#
#             elif i[0] <= r[1] <= i[1]:  # the removal end point is within the curret range
#                 stk.append([r[1], i[1]])
#
#             else:  # current I is outside the removal range
#                 stk.append(i)
#
#         output = []
#         for s in stk:
#             if s[0] == s[1]:
#                 continue
#             else:
#                 output.append(s)
#         return output
