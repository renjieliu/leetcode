class Solution:
    def removeStars(self, s: str) -> str: # O( N | N )
        stk = []
        for c in s: #check if current character is "*"
            if c == "*": # pop from the stack
                stk.pop()
            else:
                stk.append(c)
        return "".join(stk)
    

