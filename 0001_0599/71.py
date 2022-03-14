class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        output = ["/"]
        for p in path:
            if p == "." or p == "":  # no need to add anything
                continue
            elif p == "..": #pop to the prev folder
                if len(output) > 1:
                    output.pop()
                else:
                    output = ["/"]
            else:
                output.append(p)
        
        return "/".join(output)[1:] or "/" #take out the leading "/" or if the output == "/", just return 


    
    


# previous approach

# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         stk = path.split('/')
#         arr = []
#         while stk:
#             curr = stk.pop(0)
#             if curr == "..":
#                 if arr: arr.pop()
#             elif curr == ".":
#                 continue
#             elif len(curr) > 0:
#                 arr.append(curr)
#         #print(arr)
#         output = '/' + '/'.join(arr)
#         return output




# previous approach

# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         path = path.replace("//","/").replace("/./", "/") 
#         stk = path.split('/') 
#         output = "/"
#         arr = []
#         for i in stk:
#             if i == "..":
#                 if len(arr)> 0:
#                     arr.pop()
#             elif i not in ['','.']:
#                 arr.append(i)
#         for a in arr:
#             output+=a+"/"
#         if len(output) > 1: #for the ones like '/a/b/c/'. remove the last /
#             return output[:-1]
#         return output



