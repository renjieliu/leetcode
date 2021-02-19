class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left  = [] #the left ones to remove
        right = [] #the right ones to remove
        for i , c in enumerate(s):
            if c == "(":
                left.append(i)
            elif c==")":
                if left == []:
                    right.append(i)
                else:
                    left.pop()
        output = ""
        for i, c in enumerate(s) :
            if left and i == left[0]:
                left.pop(0)
            elif right and i == right[0]:
                right.pop(0)
            else:
                output+=c
        return output

