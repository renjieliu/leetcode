class Solution:
    def removeDuplicates(self, s: str, k: int) -> str: #O(N | N)
        stk = [[s[0], 1]]  # character, occurrence
        
        for i in range(1, len(s)):
            c = s[i]
            if stk and c == stk[-1][0]: # curr is same as the last in the stack
                stk[-1][1] += 1 
                if stk[-1][1] == k: # it reached the k
                    stk.pop()
            else: # stack is empty or curr is not same as last in the stack
                stk.append([c, 1])
        
        output = ""
        for c, times in stk: #concat the result
            output += c*times
        return output
    

    


# previous solution

# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
#         arr = [chr(_)*k for _ in range(97, 123)]
#         while True:
#             find = 0
#             for a in arr:
#                 if a in s:
#                     find = 1
#                     s = s.replace(a, '')
#             if find == 0:
#                 return s

# previous approach
# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
#         stk= [{s[0]:1}]
#         for i in range(1, len(s)):
#             if len(stk) > 0:
#                 if s[i] in stk[-1]:
#                     if stk[-1][s[i]] +1 == k:
#                         stk.pop()
#                     else:
#                         stk[-1][s[i]] += 1
#                 else:
#                     stk.append({s[i]: 1})
#             else:
#                 stk.append({s[i]:1})
#         output = ""
#         for i in stk:
#             for k, v in i.items():
#                 output+= k*v
#
#         return output
#