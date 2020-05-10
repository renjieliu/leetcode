class Solution:
    def findJudge(self, N: int, trust: 'List[List[int]]') -> int:
        if trust == []:
            return 1 if N == 1 else -1
        hmp = {}
        hmp_trust = {}
        for t in trust:
            if t[1] not in hmp:
                hmp[t[1]] = []
            hmp[t[1]].append(t[0])
            if t[0] not in hmp_trust:
                hmp_trust[t[0]] = []
            hmp_trust[t[0]].append(t[1])
        for k, v in hmp.items():
            if len(v) == N - 1 and k not in hmp_trust:
                return k
        return -1



#OLD APPROACH
# def findJudge(N: 'int', trust: 'List[List[int]]'):
#     if N == 1 and len(trust) == 0:
#         return 1
#
#
#     dict = {}
#     max = 0
#     for i in trust:
#         if i[1] not in dict.keys():
#             dict[i[1]] = 1
#         else:
#             dict[i[1]] +=1
#
#         if dict[i[1]] > max:
#             max = dict[i[1]]
#
#     if max != N-1:
#         return -1
#     else:
#         output = []
#         for k,v in dict.items():
#             if v==max:
#                 output.append(k)
#
#         if len(output) != 1 :
#             return -1
#
#
#     for i in trust:
#         if i[0]==output[0]:
#             return -1
#
#     return output[0]
#
#
# print(findJudge(2, [[1,2]]))
# print(findJudge(3, [[1,3],[2,3]]))
# print(findJudge(3, [[1,3],[2,3],[3,1]]))
# print(findJudge(3, [[1,2],[2,3]]))
# print(findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))
# print(findJudge(1, [])) #the judge does not trust any one, and every one else trusts the judge
#
#
