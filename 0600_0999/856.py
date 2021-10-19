class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stk = [0] #total score from curr (, assuimg the whole S is within a huge (), the last ) will never be met
        for c in S:
            if c == "(":
                stk.append(0)
            else:
                prev = stk.pop()
                stk[-1] += max(prev*2, 1)
        return stk.pop()

#previous approach
# class Solution:
#     def scoreOfParentheses(self, S: str) -> int:
#        left = []
#         calc = []
#         calc_pos = []
#         for i, c in enumerate(S): #when meet ), check the closest (, and add everything in between
#             if c == "(":
#                 left.append(i)
#             else:
#                 if left[-1] == i-1:
#                     calc.append(1)
#                     calc_pos.append(i)
#                     left.pop()
#                 else:
#                     curr = 0
#                     while calc_pos and calc_pos[-1] > left[-1]:
#                         curr+=calc.pop()
#                         calc_pos.pop()
#                     calc.append(curr*2)
#                     calc_pos.append(i)
#                     left.pop()
#         return sum(calc)


#previous approach
# def scoreOfParentheses( S: str):
#     calc_stk = []
#     left_pos = []
#     calc_stk_pos = []
#     for i in range(len(S)):
#         t = S[i]
#         if t == "(":
#             left_pos.append(i) #add current loc to the stack
#         elif t == ")":
#             if left_pos[-1] == i-1: #the last "(" is right before the curr ")"
#                 calc_stk.append(1)
#                 calc_stk_pos.append(i)
#                 left_pos.pop()
#             else:
#                 #find all the stk[x] between last ( and current i
#                 x = 0
#                 while calc_stk_pos[-1] > left_pos[-1]:
#                     x+=calc_stk[-1]
#                     calc_stk_pos.pop()
#                     calc_stk.pop()
#                     if len(calc_stk_pos) * len(left_pos) ==  0:
#                         break
#
#                 left_pos.pop()
#                 calc_stk.append(2*x)
#                 calc_stk_pos.append(i)
#
#
#     return sum(calc_stk)
#
# #
# print(scoreOfParentheses("()"))
# print(scoreOfParentheses("(()())"))
# print(scoreOfParentheses("()()"))
# print(scoreOfParentheses("(()())()(())()"))
# print(scoreOfParentheses("((()()((()()))))()(())(())(())((()))")) #40
