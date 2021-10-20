class Solution:
    def reverseWords(self, s: str) -> str:
        arr = [""]
        for c in s:
            if c == " ":
                if arr and arr[-1] != "":
                    arr.append("")
            else:
                arr[-1] += c
        
        output = ""
        for a in arr[::-1]:
            output += (a+" ") if a else ""
        
        return output[:-1] #take out the last space
        
        
        
#         arr = s.split(" ")[::-1]
#         output = ""
#         for a in arr:
#             if a: 
#                 output+=a + " "
#         return output.rstrip(" ") #remove the last space from the output
    


# previous approach
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         arr = s.split(' ')
#         words = []
#         for a in arr:
#             if len(a) > 0:
#                 words.append(a)
#         return ' '.join(words[::-1])

# previous approach
# def reverseWords(s: str):
#     if len(s)==0:
#         return s
#     temp = ""
#     output = []
#     currnt_space_cnt = 0
#     start = 0
#     end = 0
#     for i in range(len(s)):
#         if s[i] != ' ':
#             start = i
#             break
#     for i in range(len(s)-1, -1, -1):
#         if s[i]!= ' ':
#             end = i
#             break
#
#     if start == end: #if it only 1 character, return it, as long as it's not a blank space
#         return s.replace(" ","")
#     for i in range(end, start-1, -1):
#         temp +=''
#         if s[i] == " ":
#             output.append(temp[::-1])
#             temp = ""
#             currnt_space_cnt += 1
#             if currnt_space_cnt ==1:
#                 output.append(" ")
#         else:
#             currnt_space_cnt = 0
#             temp+=s[i]
#     if temp != "":
#         output.append(temp[::-1])
#
#     return "".join(output)
#
#
#
#
#
#
# print(reverseWords("the sky is blue"))
# print(reverseWords("  hello world!  "))
# print(reverseWords("a good   example"))
# print(reverseWords("a"))
# print(reverseWords(""))
# print(reverseWords("    "))