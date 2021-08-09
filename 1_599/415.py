class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        a = list(num1 if len(num1) <= len(num2) else num2)
        b = list(num1 if len(num1) > len(num2) else num2)
        output = ""
        while a or b or carry:
            res = (int(a.pop()) if a else 0) + (int(b.pop()) if b else 0) + carry
            carry= 1 if res >=10 else 0
            res -= 10 if res >= 10 else 0
            output = str(res) + output
        return output

#         while b:
#             res = int(b.pop()) + carry
#             carry= 1 if res >=10 else 0
#             res -= 10 if res >= 10 else 0
#             output = str(res) + output

#         if carry == 1:
#             output = "1" + output
#         return output



# previous approach
# def addStrings(num1, num2):
#     """
#     :type num1: str
#     :type num2: str
#     :rtype: str
#     """
#     n1 = num1
#     n2 = num2
#
#     if len(num1) > len(num2):
#         n2 = str("0") * (len(num1) - len(num2)) + num2
#
#     if len(num2) > len(num1):
#         n1 = str("0") * (len(num2) - len(num1)) + num1
#     sum = ""
#     reg = 0
#     for i in range(len(n1)-1, -1, -1):
#         if int(n1[i])+int(n2[i])+reg >9:
#             sum = str(int(n1[i])+int(n2[i])+reg-10) + str(sum)
#             reg = 1
#         else:
#             sum = str(int(n1[i])+int(n2[i])+reg) + str(sum)
#             reg = 0
#
#     return sum if reg==0 else "1" + sum
#
# print(addStrings("10", "0"))
#
# print(addStrings("9", "21"))
# print(addStrings("0", "1000"))
# print(addStrings("1", "9"))
