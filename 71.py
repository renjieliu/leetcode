class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = path.split('/')
        arr = []
        while stk:
            curr = stk.pop(0)
            if curr == "..":
                if arr: arr.pop()
            elif curr == ".":
                continue
            elif len(curr) > 0:
                arr.append(curr)
        #print(arr)
        output = '/' + '/'.join(arr)
        return output