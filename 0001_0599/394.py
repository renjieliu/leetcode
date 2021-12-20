class Solution:
    def decodeString(self, s: str) -> str:
        num_stk = [] # times stack
        stk = [[]] # string stack
        num = ""
        for c in s:
            if 48<=ord(c) <= 57: 
                num += c
            elif c == "[":
                num_stk.append(int(num)) #add the number to the num_stk
                num = ""
                stk.append([])
            elif c == "]":
                t = ( "".join(stk.pop()) ) * num_stk.pop()
                if stk:
                    stk[-1].append(t)
                else:
                    stk = [[t]]
            else:
                stk[-1].append(c)
            # print(stk, num_stk, num)
        output = ""
        for s in stk:
            output += "".join(s)
        return output
        


# previous approach
# class Solution:
#     def decodeString(self, s: str) -> str:
#         output = ""
#         stk_str = []
#         stk_num = []
#         nums = [str(_) for _ in range(10)]
#         in_num = 0  # the number needs to be appended to the previous
#         for c in s:
#             if c in nums:
#                 if in_num == 0:
#                     stk_num.append("")
#                     in_num = 1
#                 stk_num[-1] += c

#             elif c == "[":
#                 in_num = 0
#                 stk_str.append("")

#             elif c == "]":
#                 curr = stk_str.pop() * int(stk_num.pop())
#                 if stk_str:
#                     stk_str[-1] += curr
#                 else:
#                     output += curr
#             else:
#                 if stk_str:
#                     stk_str[-1] += c
#                 else:
#                     output += c

#         output += stk_str[-1] if stk_str else ""
#         return output



# previous approach
# class Solution:
#     def decodeString(self, s: str) -> str:
#         nums =  [str(_) for _ in range(10)]
#         str_stk = []
#         left_pos = [] #position of [
#         str_pos = [] #end of string
#         repeat = ""
#         repeat_stk = []
#         output= ""
#         curr = ""
#         for i in range(len(s)):
#             #print(i,str_stk, repeat_stk)
#             #print(s[i],str_stk)
#             if s[i] in nums:
#                 repeat += s[i]  # if find a number
#                 if curr != "":
#                     str_stk.append(curr)
#                     str_pos.append(i-1)
#                     curr = ""
#             elif s[i] == "[":
#                 left_pos.append(i)
#                 repeat_stk.append(int(repeat))  # the number should be stacked
#                 repeat = ""

#             elif s[i] == "]":
#                 if len(curr) > 0:
#                     str_stk.append(curr)
#                     str_pos.append(i-1)
#                     curr = ""

#                 r = repeat_stk.pop()
#                 if len(repeat_stk) == 0:
#                     output+= r*(''.join(str_stk))
#                     str_stk = []
#                     repeat_stk = []
#                     left_pos = []
#                     str_pos = []

#                 else:
#                     x = ""
#                     # print(str_stk , str_pos, left_pos)
#                     while str_pos[-1] > left_pos[-1]:
#                         x = str_stk.pop()+x
#                         str_pos.pop()
#                         if len(str_pos) == 0:
#                             break

#                     x = r*x
#                     str_stk.append(x)
#                     str_pos.append(i)
#                     left_pos.pop()


#             else: #if it's characters
#                 if repeat_stk ==[]:
#                     output+= s[i]
#                     curr = ""
#                 else:
#                     curr+=s[i]

#         return output





