class Solution:
    def maximum69Number (self, num: int) -> int: # O( N | N )
        n = str(num) 
        for i, c in enumerate(n): # find the first 6, and change it to 9 
            if c =="6":
                return int(n[:i] + "9" + n[i+1:])
        return num # all the digits are 9
    



# previous solution

# class Solution:
#     def maximum69Number (self, num: int) -> int:
#         s = str(num)
#         output = ""
#         i = 0
#         while i < len(s):
#             if s[i] == '6':
#                 output+='9'
#                 return int(output+s[i+1:])
#             else:
#                 output+=s[i]
#             i+=1
#         return int(output)


