class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(" ")
        if s == "":
            return 0
        curr = ""
        i = 0
        sign = 1
        if s[i] in "+-":
            sign = -1 if s[i] == "-" else 1
            i+=1

        while i < len(s) and 48<=ord(s[i])<=57: # read the digits from the left 
            curr += s[i]
            i+=1
        
        if curr == "": #no digits founded
            return 0
        else:
            t = int(curr) * sign
            if t <= 0:
                return max(-2**31, t)
            else:
                return min(2**31-1, t)

        

# previous approach

# def myAtoi(str: str):
#     #1. trim
#     temp = ""

#     if len(str)==0:
#         return 0
#     else:
#         for i in range(len(str)):
#             if str[i] != " ":
#                 break
#         if i<=len(str)-1:
#             temp = str[i:]

#         else :
#             return 0
#     #2. the first character is letter?

#     if ord(temp[0]) not in range(48,58) and temp[0]!="-" and temp[0]!="+":
#         return 0

#     output = ""

#     if temp[0] == "-":
#         output += "-"
#         temp = temp[1:]
#     elif temp[0] == "+":
#         temp = temp[1:]


#     if len(temp)==0:
#         return 0
#     else:

#         if ord(temp[0]) not in range(48,58):
#             return 0

#         #3. generate the number
#         for i in temp:
#             if ord(i) in range(48,58):
#                 output += i
#             else:
#                 break
#         if int(output) < -2**31:
#             return -2**31
#         elif int(output) >2**31:
#             return 2**31
#         else:
#             return int(output)

# print(myAtoi("42"))
# print(myAtoi("   -42"))
# print(myAtoi("4193 with words"))
# print(myAtoi("-91283472332 with words"))
# print(myAtoi("-+1"))
# print(myAtoi("1"))
# print(myAtoi("+"))
# print(myAtoi("-2147483647"))

