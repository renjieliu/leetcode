class Solution: # RL 20210807: Copied solution
    def minCut(self, s: str) -> int:
        # acceleration
        if s == s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        # algorithm
        cut = [x for x in range(-1,len(s))]  # cut numbers in worst case (no palindrome)
        for i in range(len(s)):
            r1, r2 = 0, 0
            # use i as origin, and gradually enlarge radius if a palindrome exists
            # odd palindrome
            while i-r1 >= 0 and i+r1 < len(s) and s[i-r1] == s[i+r1]:
                cut[i+r1+1] = min(cut[i+r1+1], cut[i-r1]+1)
                r1 += 1
            # even palindrome
            while i-r2 >= 0 and i+r2+1 < len(s) and s[i-r2] == s[i+r2+1]:
                cut[i+r2+2] = min(cut[i+r2+2], cut[i-r2]+1)
                r2 += 1
        return cut[-1]


# my approach greedy, does not work for the case:
#"adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece"

# class Solution:
#     def minCut(self, s: str) -> int:
#         def helper(s):
#             hmp = {}
#             for i, c in enumerate(s):
#                 if c not in hmp:
#                     hmp[c] = []
#                 hmp[c].append(i)
#             # print(hmp)
#             cut = 0
#             i = 0
#             while i < len(s):
#                 curr = s[i]
#                 if len(hmp[curr]) == 1:
#                     cut += 1
#                     i += 1
#                 else:
#                     for j in hmp[curr][::-1]:
#                         # print(j, i,s[i:j+1], s[i:j+1][::-1])
#                         if j <= i:
#                             cut += 1
#                             i += 1
#                             break
#                         elif s[i:j + 1] == s[i:j + 1][::-1]:
#                             cut += 1
#                             i = j + 1
#                             break
#
#             return cut - 1  # minus the last cut
#
#         A = helper(s)
#         B = helper(s[::-1])
#         return min(A, B)

