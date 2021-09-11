class Solution:
    def calculate(self, s: str) -> int:
        def helper(txt):  # calculate current txt
            return sum(int(_) for _ in txt.replace('--', '+').replace('-', '+-').split('+') if _)

        full = ""
        s = s.replace(' ', '')
        stk = []
        for i, c in enumerate(s):  # once meet a (, add a stk, once meet a ), calc the current, and add back
            if c == "(":
                stk.append("")
            elif c == ")":
                res = helper(stk.pop())
                if stk:
                    stk[-1] += str(res)
                else:
                    full += str(res)
            else:
                if stk:
                    stk[-1] += c
                else:  # if no stack, just add to the full string.
                    full += c
        # print(full)
        return helper(full)

# previous approach
# class Solution:
#     def calculate(self, s: str) -> int:
#         def calc(txt):
#             a = txt.replace('--','+').replace('-','+-').split('+')
#             return sum([int(x) for x in a if x != ""]) #for (-1), it will be split to ["", "-1"]
#         s = s.replace(' ', '')
#         cook = "" #the outer string
#         stk = []
#         for i,c in enumerate(s):
#             if c == "(":
#                 stk.append("") #put following to a stk
#             elif c== ")":
#                 localRes= str(calc(stk.pop())) #compute the current string
#                 if stk: #add current to the previous
#                     stk[-1]+=localRes
#                 else:
#                     cook+=localRes
#             else:
#                 if stk == []:
#                     cook += c
#                 else:
#                     stk[-1] += c
#         return calc(cook)
#
#
