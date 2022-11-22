class Solution:
    def isStrobogrammatic(self, num: str) -> bool: # O( N | N )
        ref = ""
        for n in num:
            if n in "23457":
                return False
            
            elif n == "6":
                ref += "9"
            elif n == "9":
                ref += "6"
            else:
                ref += n # "018" no change
        return ref[::-1] == num # rotate ==> change 6 to 9, and 9 to 6, and reverse
    



# previous solution 

# class Solution:
#     def isStrobogrammatic(self, num: str) -> bool:
#         lkp = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
#         curr = ""
#         for n in num[::-1]:
#             if n not in lkp:
#                 return False
#             curr+=lkp[n]
#         return curr == num


# previous approach
# class Solution:
#     def isStrobogrammatic(self, num: str) -> bool:
#         temp = ""
#         for n in num:
#             if n in ['0','1','8']:
#                 temp+=n
#             elif n == '6':
#                 temp+='9'
#             elif n == '9':
#                 temp+='6'
#             else:
#                 return False
#         return True if temp[::-1] == num else False
