class Solution:
    def numMatchingSubseq(self, s: str, words: 'List[str]') -> int:
        def isSub(a, b):
            i = 0
            while True:
                t = a.find(b[i])
                if t == -1:
                    return 0
                a = a[t+1:]
                i += 1
                if i == len(b):
                    return 1
            return 0

        output = 0
        for w in words:
            output += 1 if isSub(s, w) else 0
        return output


# previous approach
# def numMatchingSubseq(S: str, words: 'List[str]'):
#     cnt = 0
#     for i in words:
#         t = S
#         ok = 0
#         for w in i:
#             if t.find(w) == -1:
#                 break
#             else:
#                 t = t[t.index(w) + 1:]
#                 ok += 1
#
#         if ok == len(i):
#             cnt += 1
#
#     return cnt
#
#
# print(numMatchingSubseq("abcde",  ["a", "bb", "acd", "ace"]))


