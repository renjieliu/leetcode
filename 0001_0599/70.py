class Solution:
    def climbStairs(self, n: int) -> int: #fib, with a =1, b = 2, c = a+b, to n
        if n == 1 or n == 2:
            return n
        else:
            a = 1
            b = 2
            for i in range(3, n+1):
                c = a+b
                a = b
                b = c
            return c



# previous approach
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n in [1, 2]:
#             return n
#         else:
#             c1 = 1
#             c2 = 2
#             for i in range (3, n+1):
#                 c3 = c1+c2
#                 c1 = c2
#                 c2 = c3
#             return c3
#

# previous approach
# def climbStairs(n):
#     """
#     :type n: int
#     :rtype: int
#     """
#     # if n == 1:
#     #     return 1
#     # elif n == 2 :
#     #     return 2
#     # else:
#     #     return climbStairs(n-1) + climbStairs(n-2)
#     # using loop to calculate fibonacci
#     if n == 1 :
#         return 1
#     elif n == 2 :
#         return 2
#     else:
#         first = 1
#         second = 2
#         for n in range(3, n+1):
#             result = first+second
#             first = second
#             second = result
#         return result
#
# print (climbStairs(4))
