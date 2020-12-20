class Solution:
    def reformatNumber(self, number: str) -> str:
        output = [""]
        for n in number:
            if 48 <= ord(n) <= 57:
                if len(output[-1]) == 3:
                    output.append(n)
                else:
                    output[-1] += n
        if len(output[-1]) == 1:  # the final 2 groups xxx-x to xx-xx
            output[-1] = output[-2][-1] + output[-1]
            output[-2] = output[-2][:-1]
        return "-".join(output)

# previous approach
# class Solution:
#     def reformatNumber(self, number: str) -> str:
#         output = [""]
#         number = number.replace(".", "").replace("-", "").replace(" ", "")
#         if len(number) in (2, 3):
#             return number
#         elif len(number) == 4:
#             return number[:2] + "-" + number[2:]
#         else:
#             number = list(number)
#             if len(number) % 3 == 0:
#                 for n in number:
#                     if len(output[-1]) < 3:
#                         output[-1] += n
#                     else:
#                         output.append(n)
#             elif len(number) % 3 == 1:
#                 for n in number[:-4]:
#                     if len(output[-1]) < 3:
#                         output[-1] += n
#                     else:
#                         output.append(n)
#                 for n in number[-4:]:
#                     if len(output[-1]) < 2:
#                         output[-1] += n
#                     else:
#                         output.append(n)
#
#             elif len(number) % 3 == 2:
#                 for n in number[:-2]:
#                     if len(output[-1]) < 3:
#                         output[-1] += n
#                     else:
#                         output.append(n)
#                 for n in number[-2:]:
#                     if len(output[-1]) < 2:
#                         output[-1] += n
#                     else:
#                         output.append(n)
#             return "-".join(output)
#
#
#
#
#
#
