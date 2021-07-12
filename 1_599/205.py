class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hmp = {} #If it appears in the earlier mapping, check if they are same with current counterpart.
        count = {}
        for i, c in enumerate(s):
            if c not in hmp:
                hmp[c] = t[i]
                if t[i] not in count: # check how many letters mapped to the same letter
                    count[t[i]] = 0
                count[t[i]] += 1
                if count[t[i]] > 1:
                    return False

            elif hmp[c] != t[i]:
                return False

        return True


# previous approach
# def isIsomorphic(s, t):
#     """
#     :type s: str
#     :type t: str
#     :rtype: bool
#     """
#     map = {}
#     map_2 = {}
#     for i in range(len(s)):
#         if s[i] not in map:
#             map[s[i]]= t[i]
#         else:
#             if t[i]!=map[s[i]]:
#                 return False
#
#     for i in range(len(t)):
#         if t[i] not in map_2:
#             map_2[t[i]]= s[i]
#         else:
#             if s[i]!=map_2[t[i]]:
#                 return False
#
#     return True
#
# print(isIsomorphic("egg", "add"))
# print(isIsomorphic("foo", "bar"))
# print(isIsomorphic("paper", "title"))
# print(isIsomorphic("", ""))
# print(isIsomorphic("ab", "aa"))



