class Solution:
    def isAlienSorted(self, words: 'List[str]', order: str) -> bool:
        hmp = {}
        for i, o in enumerate(order):
            hmp[o] = i
        arr = []
        for w in words:
            arr.append([])
            for c in w:
                arr[-1].append(hmp[c])
        return arr == sorted(arr)



# previous approach
# def isAlienSorted(words: 'List[str]', order: 'str'):
#     cnt =1
#     map = {}
#
#     for i in order:
#         map[i] = cnt
#         cnt +=1
#
#     for i in range(1, len(words)):
#         commonStart = 0
#         for j in range(0,  len(words[i-1])):
#             if commonStart == len(words[i]):
#                 return False
#
#             if map[words[i-1][j]] < map[words[i][j]]:
#                 break
#
#             elif map[words[i-1][j]] > map[words[i][j] ]:
#                 return False
#
#             elif map[words[i-1][j]] == map[words[i][j] ]:
#                 commonStart +=1
#                 continue
#
#             if len(words[i-1]) > len(words[i]):
#                 return False
#
#     return True
#
# print(isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
# print(isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))
# print(isAlienSorted(["ubg","kwh"], "qcipyamwvdjtesbghlorufnkzx"))
# print(isAlienSorted(["kuvp","q"], "ngxlkthsjuoqcpavbfdermiywz"))
# print(isAlienSorted(["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"], "zkgwaverfimqxbnctdplsjyohu"))
#
#
