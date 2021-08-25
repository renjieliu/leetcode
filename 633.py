class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        arr = []
        for a in range(2**16):
            if a**2 < c:
                arr.append(a**2)
            elif a**2 == c:
                return True
            else:
                break

        for a in arr:
            b = (c-a)**0.5
            if b == int(b):
                return True
        return False




# previous approach
# def judgeSquareSum(c):
#     """
#     :type c: int
#     :rtype: bool
#     """
#     for i in range(0,int(c**0.5)+1):
#         if int((c-i**2)**0.5) ==(c-i**2)**0.5:
#             return True
#     return False
#
#
# print(judgeSquareSum(5))
# print(judgeSquareSum(0))
# print(judgeSquareSum(3))
# print(judgeSquareSum(4294967296))
#
#
