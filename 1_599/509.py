class Solution:
    def fib(self, n: int) -> int:
        if n in (0,1):
            return n
        else:
            n1 = 0
            n2 = 1
            for i in range(2, n+1):
                n3 = n1+n2
                n1 = n2
                n2 = n3
            return n3


        # previous approach
# def fib( N: 'int'):
#     if N==0:
#         return 0
#     if N == 1 or N == 2:
#         return 1
#     else:
#         list = []
#         list.append(1)
#         list.append(1)
#         for i in range(2, N):
#             list.append(list[i - 2] + list[i - 1])
#
#         return list[-1]
#
# print(fib(30))