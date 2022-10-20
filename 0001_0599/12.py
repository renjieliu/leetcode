class Solution:
    def intToRoman(self, num: int) -> str: # O( logN | 1 )
        roman = [[1000, 'M'] ,[900, 'CM'] ,[500, 'D'] ,[400, 'CD'] ,[100, 'C'] ,[90, 'XC'] ,[50, 'L'] ,[40, 'XL'] ,[10, 'X'] ,[9, 'IX'] ,[5, 'V'] ,[4, 'IV'] ,[1, 'I']]
        output = ""
        for rm, c in roman: # go through the number from the arr from the largest
            if num >= rm :
                output += c * (num // rm ) #find the roman number, and repeat times
                num %= rm # mod the current number by roman number
        return output
    




# previous solution 

# class Solution:
#     def intToRoman(self, num: int) -> str:
#         lkp = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
#         output = ""
#         for k in sorted(lkp.keys(), reverse = True):
#             output += lkp[k] * (num//k)
#             num %= k
#         return output

# previous approach
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         output = ""
#         output += "M" * (num // 1000)
#         num %= 1000
#         output += "CM" * (num // 900)
#         num %= 900
#         output += "D" * (num // 500)
#         num %= 500
#         output += "CD" * (num // 400)
#         num %= 400
#         output += "C" * (num // 100)
#         num %= 100
#         output += "XC" * (num // 90)
#         num %= 90
#         output += "L" * (num // 50)
#         num %= 50
#         output += "XL" * (num // 40)
#         num %= 40
#         output += "X" * (num // 10)
#         num %= 10
#         output += "IX" * (num // 9)
#         num %= 9
#         output += "V" * (num // 5)
#         num %= 5
#         output += "IV" * (num // 4)
#         num %= 4
#         output += "I" * num
#
#         return output

# previous approach
# def intToRoman(num: 'int'):
#     map = { 1: "I",
#             4: "IV",
#             5: "V",
#             9: "IX",
#             10: "X",
#             40: "XL",
#             50: "L",
#             90: "XC",
#             100: "C",
#             400: "CD",
#             500: "D",
#             900: "CM",
#             1000: "M"
#            }
#     map_key =[1000,900,500,400,100,90,50,40,10,9,5,4,1]
#     output = ""
#     while num >0:
#         for i in map_key:
#             if num//i != 0:
#                 output+= map[i]*(num//i)
#                 num-= i * (num//i)
#
#     return output
#
# print(intToRoman(10))
# print(intToRoman(99))
# print(intToRoman(3999))
# print(intToRoman(2019))
# print(intToRoman(1231))
#











