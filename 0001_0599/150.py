class Solution:
    def evalRPN(self, tokens: 'List[str]') -> int:
        stk = []
        for t in tokens:
            if t not in "+-*/":
                stk.append(int(t))
            else:
                a = stk.pop()
                b = stk.pop()
                if t == "+":
                    stk.append(b+a)
                elif t == "-":
                    stk.append(b-a)
                elif t == "*":
                    stk.append(b*a)
                elif t == "/":
                    stk.append(int(b/a))
            #print(stk)
        return stk[0]

