class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            a = 0
            b = c = 1
            for i in range(3, n+1):
                d = a+b+c
                a = b
                b = c
                c = d
            return d


# previous approach
# def tribonacci(n: int):
#     a1 = 0
#     a2 = 1
#     a3 = 1
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         for i in range(3, n + 1):
#             curr = a1 + a2 + a3
#             a1 = a2
#             a2 = a3
#             a3 = curr
#     return curr
#
#
# print(tribonacci(4))
# print(tribonacci(25))
#
#
