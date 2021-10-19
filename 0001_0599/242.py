class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmp_s = defaultdict(int)
        hmp_t = defaultdict(int)
        for c in s:
            hmp_s[c]+=1
        for c in t:
            hmp_t[c]+=1
        return hmp_s==hmp_t

        #return sorted(list(s)) == sorted(list(t))


# previous approach
# def isAnagram(s, t):
#     s1 = list(str(s))
#     t1 = list(str(t))
#
#     s1.sort()
#     t1.sort()
#
#     if len(s1) != len(t1):
#         return False
#     else:
#         output = True
#         for i in range(0, len(s1)):
#             if s1[i]!=t1[i]:
#                 output = False
#                 break
#     return output
#
#
# print(isAnagram("anagram", "nagaram"))
#
#
#
