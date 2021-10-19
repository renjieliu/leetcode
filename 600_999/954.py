class Solution:
    def canReorderDoubled(self, arr: 'List[int]') -> bool:
        hmp = {}
        for a in arr:
            if a not in hmp:
                hmp[a] = 0
            hmp[a]+=1
        # print(hmp)
        for v in sorted(arr):
            if v == 0:
                if v in hmp:
                    if hmp[v] % 2 != 0:
                        return False
                    else:
                        del hmp[v]
            else:
                if v in hmp: #it's possible v has been iterated
                    if 2*v in hmp:
                        hmp[v] -= 1
                        hmp[2*v] -= 1
                        if hmp[v] < 0 or hmp[2*v] < 0 :
                            return False
                        if hmp[v] == 0:
                            del hmp[v]
                        if hmp[2*v] == 0:
                            del hmp[2*v]
            if hmp == {}:
                return True

            # print(hmp)
        return hmp == {}


# previous approach
# class Solution:
#     def canReorderDoubled(self, A: 'List[int]') -> bool:
#         if A == []: return True
#
#         hmp = {}
#         for a in A:
#             if a not in hmp:  # count the occurrance of each number
#                 hmp[a] = 0
#             hmp[a] += 1
#         arr = []
#         A.sort(key=lambda x: abs(x))
#         for k in A:
#             if k in hmp:  # if k is still in the hashmap
#                 if 2 * k in hmp:  # if 2*k is there, then we find a pair
#                     hmp[k] -= 1
#                     hmp[2 * k] -= 1
#                     if hmp[k] == 0:
#                         del hmp[k]
#                     if 2 * k in hmp and hmp[2 * k] == 0:
#                         del hmp[2 * k]
#                 # elif k/2 in hmp: #or if k/2 is there, then we find a pair as well
#                 #     hmp[k]-=1
#                 #     hmp[k/2]-=1
#                 #     if hmp[k] == 0:
#                 #         del hmp[k]
#                 #     if k/2 in hmp and hmp[k/2] == 0:
#                 #         del hmp[k/2]
#                 else:  # cannot find a match, then it cannot be arranged
#                     return False
#
#                 if hmp == {}:  # every number of the list can be paired
#                     return True
#


