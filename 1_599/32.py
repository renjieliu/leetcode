class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        arr = []
        output = 0
        for i, c in enumerate(s):
            if c == "(":
                stk.append(i)
            elif c == ")":
                if stk:
                    arr.append([stk.pop(), i])
        if arr == []:
            return 0
        else:
            arr.sort(key=lambda x: x[0])
            s = arr[0][0]
            e = arr[0][1]
            curr = output = e - s + 1
            arr.pop(0)
            for a, b in arr:
                if a > e + 1:
                    s = a
                    e = b
                else:
                    e = max(b, e)
                curr = e - s + 1
                output = max(curr, output)
            return output
