class Solution:
    def shortestToChar(self, s: str, c: str) -> 'List[int]':
        distance = []
        loc = [i for i in range(len(s)) if s[i] == c]
        ptr = 0
        for i in range(len(s)):  # for each character, find the previous c and next c, and find the abs distance
            if s[i] == c:
                distance.append([i, i])
                ptr += 1
            else:
                if 0 < ptr < len(loc):
                    distance.append([loc[ptr - 1], loc[ptr]])
                elif ptr == 0:
                    distance.append([-float('inf'), loc[ptr]])
                elif ptr >= len(loc):
                    distance.append([loc[-1], float('inf')])
        # print(distance)
        return [min(abs(i - distance[i][0]), abs(i - distance[i][1])) for i in range(len(s))]

# previous approach
# def shortestToChar(S, C):
#     """
#     :type S: str
#     :type C: str
#     :rtype: List[int]
#     """
#
#     output = list()
#     position = [i for i in range(0, len(S)) if S[i] == C ]
#
#     for i in range(0, len(S)):
#         if S[i] ==C:
#             output.append(0)
#         else:
#             min = abs(i-position[0])
#             for j in position:
#                 if abs(i-j)<min:
#                     min = abs(i-j)
#             output.append(min)
#
#     return  output
#
# print(shortestToChar("loveleetcode", "e"))
#
