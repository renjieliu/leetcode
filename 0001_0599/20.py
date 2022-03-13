class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in "({[":  # add the left side to the stack 
                stk.append(c)
            else:
                if stk == [] or stk.pop()+c not in ("{}", "[]","()"):  # take out last from the stk, and see if it's valid
                    return False
        return stk == []




# previous approach

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stk_c = [-float('inf')] # record the location of {
#         stk_p = [-float('inf')] # record the location of [
#         stk_b = [-float('inf')] # record the location of (
#         for i, c in enumerate(s):
#             if c == "(":
#                 stk_p.append(i)
#             elif c == "[":
#                 stk_b.append(i)
#             elif c == "{":
#                 stk_c.append(i)
            
#             elif c == "}": #check if there is any { in the front, and no ( or [ in between
#                 if stk_c[-1] == -float('inf') or stk_p[-1] > stk_c[-1] or stk_b[-1] > stk_c[-1]:
#                     return False
#                 else:
#                     stk_c.pop()
            
#             elif c == "]": #check if there is any [ in the front, and no { or ( in between
#                 if stk_b[-1] == -float('inf') or stk_p[-1] > stk_b[-1] or stk_c[-1] > stk_b[-1]:
#                     return False
#                 else:
#                     stk_b.pop()
                    
#             elif c == ")": #check if there is any ( in the front, and no [ or { in between
#                 if stk_p[-1] == -float('inf') or stk_b[-1] > stk_p[-1] or stk_c[-1] > stk_p[-1]:
#                     return False
#                 else:
#                     stk_p.pop()
                    
#         return stk_c == [-float('inf')] and stk_p == [-float('inf')] and stk_b == [-float('inf')]
                    
        
     

                
# previous approach

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stk = []
#         left = ['(', '[', '{']
#         for c in s:
#             if c in left:
#                 stk.append(c)
#             else:
#                 if stk:
#                     if  stk.pop() + c not in ['()', '[]', '{}']:
#                         return False
#                 else:
#                     return False
#             #print(c, 'stk' ,stk)
#         return stk == []


# previous approach

# class Solution:
#     def isValid(self, s: str) -> bool:
#         if len(s) ==0:
#             return True
#         map  = {}
#         c = 0
#         for i in s:
#             if i =="{":
#                 if "{" not in map:
#                     map["{"] = []
#                 map["{"].append(c)

#             elif i == "[":
#                 if "[" not in map:
#                     map["["] = []
#                 map["["].append(c)

#             elif i == "(":
#                 if "(" not in map:
#                     map["("] = []
#                 map["("].append(c)

#             elif i == "}":
#                 if "{" not in map or len(map["{"])<1 or c - map["{"][-1] >1 :
#                     return False
#                 else:
#                     map["{"].pop()
#                     c -= 2

#             elif i == "]":
#                 if "[" not in map or len(map["["])<1 or c - map["["][-1] >1 :
#                     return False
#                 else:
#                     map["["].pop()
#                     c -= 2

#             elif i == ")":
#                 if "(" not in map or len(map["("]) < 1 or c - map["("][-1] >1 :
#                     return False
#                 else:
#                     map["("].pop()
#                     c-=2

#             c+=1

#         summ = 0
#         for v in map.values():
#             summ+=len(v)
#         if summ !=0 :
#             return False
#         else:
#             return True

