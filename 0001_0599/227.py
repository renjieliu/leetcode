class Solution:
    def calculate(self, s: str) -> int:
        def calc(s): #this will only calc the string with * or /
            output = None 
            curr = ""
            op = ""
            for c in s:
                # print(s, 'curr:#',  curr, op, 'output#', output)
                if c not in "*/": 
                    curr += c 
                else:
                    if output == None:
                        output = int(curr)
                    else:
                        if op == "*":
                            output *= int(curr) 
                        elif op == "/":
                            output = int(output/int(curr)) #-10//3 = 4 , need to use int function to truncate toward zero
                    op = c
                    curr = ""
            # print('--', op, curr, output)
            if op == "*":
                output *= int(curr) 
            elif op == "/":
                output = int(output/int(curr))
            # print('output', output)
            return output if output != None else int(curr)
        
        s = s.replace(" ", "").replace("-", "+-")
        arr = s.split("+")
        output = 0
        for a in arr:
            # print(a, calc(a))
            output += calc(a)

        return output
            
                
                

                    



# previous approach

# class Solution:
#     def calculate(self, s: str) -> int:
#         def calc(txt):
#             stk = []
#             curr = ""
#             operator = ""
#             for t in txt:
#                 if t not in ['*', '/']:  # it's a number
#                     curr += t
#                 else:
#                     if len(stk) < 2:
#                         stk.append(int(curr))
#                         if len(stk) == 2:
#                             res = int(stk[0] / stk[1]) if operator == '/' else (stk[0] * stk[1])
#                             stk = [res]
#                     operator = t
#                     curr = ""

#             if curr == "":
#                 return stk[0]
#             else:
#                 curr = int(curr)
#                 # print(curr,operator)
#                 return int(stk[0] / curr) if operator == '/' else (stk[0] * curr)

#         s = s.replace(' ', '').replace('-', '+-')
#         arr = s.split('+')  # each part can be added
#         # print(arr)
#         i = 0
#         while i < len(arr):
#             if '*' in arr[i] or '/' in arr[i]:
#                 arr[i] = calc(arr[i])
#             else:
#                 arr[i] = int(arr[i])
#             i += 1
#         # print(arr)
#         return sum(arr)


