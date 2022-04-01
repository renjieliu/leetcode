class Solution:
    def expand(self, s: str) -> 'List[str]': #O(n^2 | n)
        def prod(a1, a2):
            output = []
            for c in a1:
                for d in a2:
                    output.append(c+d)
            return output        
        
        arr = [[""]]
        i = 0 
        while i < len(s): #break the string into groups, and multiple each group
            if s[i] == "{":
                j = i+1 
                while s[j] != "}":
                    j += 1
                arr.append(s[i+1:j].split(",")) 
                i = j+1
                arr.append([""])
            else:
                arr[-1][0] += s[i]
                i += 1

        if len(arr) < 2:
            return ["".join(arr[0])]
        else:
            output = ["".join(arr[0])]
            for i in range(1, len(arr)): 
                output = prod(output, arr[i])
            return sorted(output)
            
            
           

# previous solution

# class Solution:
#     def expand(self, S: str) -> 'List[str]':
#         def expand(A, B):  # cross join A with B
#             if A == []:
#                 A.append("")
#             if B == []:
#                 B.append("")
#             output = []
#             for a in A:
#                 for b in B:
#                     output.append(a + b)
#             return output

#         stk = 0
#         pool = []
#         for s in S:  # push all the character to the pool, if standalone,  [x], if optional, [a,b,c], then cartesian join all.
#             if s != ",":
#                 if s == "{":
#                     stk = 1
#                     pool.append([])
#                 elif s == "}":
#                     stk = 0
#                 else:
#                     if stk == 1:
#                         pool[-1].append(s)
#                     else:
#                         pool.append([s])

#         while len(pool) > 1:
#             t = expand(pool[0], pool[1])
#             pool.pop(0)
#             pool.pop(0)
#             pool.insert(0, t)

#         return sorted(pool[0])




