class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5
        else:
            pa = pe = pi = po = pu = 1  # preva,e,i,o,u
            curr = sum([pa, pe, pi, po, pu])
            for i in range(2, n + 1):
                a = curr
                e = a - pa
                i = e - pe
                o = i - pi
                u = 1
                curr = sum([a, e, i, o, u])
                pa = a
                pe = e
                pi = i
                po = o
                pu = u
            return curr

# previous approach
# class Solution:
#     def countVowelStrings(self, n: int) -> int:
#         if n == 1:
#             return 5
#         elif n == 2:
#             return 15
#         else:
#             curr = 15
#             prevA = 5
#             prevE = 4
#             prevI = 3
#             prevO = 2
#             for l in range(3, n + 1):
#                 a = curr
#                 e = a - prevA
#                 i = e - prevE
#                 o = i - prevI
#                 u = 1
#                 # print(a,e,i,o,u)
#                 prevA = a
#                 prevE = e
#                 prevI = i
#                 prevO = o
#                 curr = sum([a, e, i, o, u])
#
#             return curr
