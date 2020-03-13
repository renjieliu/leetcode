class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace("//","/").replace("/./", "/")
        stk = path.split('/')
        output = "/"
        arr = []
        for i in stk:
            if i == "..":
                if len(arr)> 0:
                    arr.pop()
            elif i not in ['','.']:
                arr.append(i)
        for a in arr:
            output+=a+"/"
        if len(output) > 1: #for the ones like '/a/b/c/'. remove the last /
            return output[:-1]
        return output