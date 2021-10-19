class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a,b = num1[:-1].split('+') #take out the last i, and split into 2 parts
        c,d = num2[:-1].split('+')
        real = int(a) * int(c) + -1 * int(b)*int(d)
        imag = int(a) * int(d) + int(b) * int(c)
        return str(real) + "+" + str(imag) + "i"





# previous approach
# def complexNumberMultiply(a: str, b: str):
#     add_1 = a.split('+')
#     add_2 = b.split('+')
#     part_1 = int(add_1[0])*int(add_2[0])
#     part_2 = int(add_1[0])*int(add_2[1].replace("i",""))
#     part_3 = int(add_1[1].replace("i",""))*int(add_2[0])
#     part_4 = int(add_1[1].replace("i",""))*int(add_2[1].replace("i","")) * (-1)
#     return  str(part_1+part_4) + '+' + str(part_2+part_3) +  "i"
#
#
# print(complexNumberMultiply("1+-1i", "1+-1i"))
#
#
