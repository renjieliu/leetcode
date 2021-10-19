class Solution:
    def frequencySort(self, s: str) -> str:
        hmp = {}
        for c in s:
            if c not in hmp:
                hmp[c] = 0
            hmp[c] += 1
        for_sort = []
        for k, v in hmp.items():
            for_sort.append([k, v])
        output = ""
        for s in sorted(for_sort, key=lambda x: x[1], reverse=True):
            output += s[0] * s[1]
        return output

# OLD Solution
# def frequencySort(s: str):
#     if len(s) ==0:
#         return ""
#     map = {}
#     for i in s:
#         if i not in map:
#             map[i] = 0
#         map[i]+=1
#     output = ""
#     t = [None]*(max(map.values())+1) #bucket sort
#     for i in map.values():
#         t[i] = i
#
#
#     for i in t[::-1]:
#         if i!= None:
#             for k,v in map.items():
#                 if v == i:
#                     output+= k*v
#                     map[k] = -1
#
#
#     return output
#
#
# print(frequencySort("tree"))
# print(frequencySort("cccaaa"))
# print(frequencySort("Aabb"))
# print(frequencySort(""))
# print(frequencySort("AA"))
# print(frequencySort("A"))

