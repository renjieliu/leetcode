class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        output = ""
        total = len(bin(left)) - 2  # 0bxxx
        for i in range(total):  # if there are 2**i number b/w left and right, current bit will turn 0
            if right - left >= 2 ** i or bin(left)[-i - 1] == "0" or bin(right)[-i - 1] == "0":
                output = "0" + output
            else:
                output = "1" + output
        return int(output, 2)

# previous approach
# class Solution:
#     def rangeBitwiseAnd(self, m: int, n: int) -> int:
#         if m * n == 0:
#             return 0
#         else:
#             m_bin = str(bin(m)).replace('0b', '')
#             n_bin = str(bin(n)).replace('0b', '')
#             output = ""
#             for i in range(len(m_bin)):
#                 if m_bin[-(i + 1)] == "0" or n_bin[-(i + 1)] == "0":
#                     output = "0" + output
#                 else:
#                     if n - m >= 2 ** i:  # as long as there's 0 (power of 2) in between, the result will be 0.
#                         output = "0" + output
#                     else:
#                         output = "1" + output
#             return int(output, 2)
#
#
#
