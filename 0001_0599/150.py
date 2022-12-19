class Solution:
    def evalRPN(self, tokens: 'List[str]') -> int: # O( N | N )
        def calc(a, b, op): # calc for a op b
            if op == "+":
                return a+b
            elif op == "-":
                return a-b
            elif op == "*":
                return a*b
            elif op == "/":
                return int(a/b) # truncate towards 0
            
            
        stk = []
        for t in tokens: # go through the tokens, calculate the local result, and push back to the stack
            if t not in "+-*/":
                stk.append(int(t))
            else:
                A = stk.pop() # pop the first operator 
                B = stk.pop() # pop the second operator
                stk.append( calc(B, A , t) )
        return stk[0]
    

    





# previous solution

# class Solution:
#     def evalRPN(self, tokens: 'List[str]') -> int:
#         stk = []
#         for t in tokens:
#             if t not in "+-*/":
#                 stk.append(int(t))
#             else:
#                 a = stk.pop()
#                 b = stk.pop()
#                 if t == "+":
#                     stk.append(b+a)
#                 elif t == "-":
#                     stk.append(b-a)
#                 elif t == "*":
#                     stk.append(b*a)
#                 elif t == "/":
#                     stk.append(int(b/a))
#             #print(stk)
#         return stk[0]



# previous solution

# class Solution:
#     def evalRPN(self, tokens: 'List[str]') -> int:
#         stk  = []
#         for i in tokens:
#             if i not in "+-*/":
#                 stk.append(i)
#             else:
#                 if len(stk) < 2:
#                     return 'Error'
#                 else:
#                     a = int(stk.pop(-2))
#                     b = int(stk.pop(-1))
#                     if i =="+":
#                         stk.append(int(a+b))
#                     elif i == "-":
#                         stk.append(int(a - b))
#                     elif i == "*":
#                         stk.append(int(a * b))
#                     elif i == "/":
#                         stk.append(int(a / b))

#         return int(stk[-1])






# previous solution

# class Solution:
#     def evalRPN(self, tokens: 'List[str]') -> int:
#         stk  = []
#         for i in tokens:
#             if i not in "+-*/":
#                 stk.append(i)
#             else:
#                 if len(stk) < 2:
#                     return 'Error'
#                 else:
#                     a = stk.pop(-2)
#                     b = stk.pop(-1)
#                     stk.append(int(eval(str(a) + i + str(b))))

#         return int(stk[-1])
