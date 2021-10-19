class Solution:
    def customSortString(self, order: str, str: str) -> str:
        hmp = {}
        for i, c in enumerate(order):
            hmp[c] = i
        s = list(str)
        s.sort(key = lambda x: hmp[x] if x in hmp else 99999)
        return ''.join(s)


# previous approach
# def customSortString(S: str, T: str):
#     map = {}
#     for i in  T:
#         if i not in map:
#             map[i] =0
#
#         map[i] +=1
#
#     output=""
#     for i in S:
#         if i in map:
#             output+= i * map[i]
#
#     for k,v in map.items():
#         if k not in S:
#             output+=str(k)*v
#
#     return output
#
#
# print(customSortString("cba", "abcd"))
# print(customSortString("", ""))
# print(customSortString("", "asasdlfkjsaf"))
# print(customSortString("cbafg", "abcd"))
#


