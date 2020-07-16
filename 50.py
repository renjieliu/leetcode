class Solution:
    def myPow(self, x: float, n: int) -> float: # X**4 = X**2 * X**2,  X**5 = X**2 * X**2 * X
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1
            else:
                if n < 0: return helper(1/x, -n)
                else:
                    nxt = self.myPow(x, n//2)
                    if n % 2 == 0 :return nxt**2
                    else:
                        return nxt**2*x
        return helper(x,n)



# previous approach
# def myPow(x: float, n: int):
#
#     if n==0:
#         return 1
#
#     elif x in [0,1]:
#         return x
#
#     elif x==-1:
#         return -1 if n%2 ==1 else 1
#
#
#     elif n > 0:
#         output = x
#         for i in range(1,n):
#             output *= x
#             if abs(output) <0.00001:
#                 return 0
#     elif n<0 :
#         output = x
#         for i in range(1, -n):
#             output *= x
#             if output > 100000:
#                 return 0
#         output = 1/output
#
#     return round(output,5)
#
# print(myPow(2,10))
# print(myPow(2.1,3))
# print(myPow( 2.00000, -2))
# print(myPow( 0, 0))