class Solution:
    def parseTernary(self, expression: str) -> str:  # "T?T?F:5:3"
        result = ""
        exp = expression
        stk = []
        i = 0
        while i < len(exp):
            if exp[i:i + 2] in ['T?',
                                'F?']:  # in Python, need to check if i+2 is beyond the index, it will take all the remaining element
                stk.append([exp[i]])
            elif exp[i] not in [":", "?"]:  # it's [0-9], T, or F
                stk[-1].append(exp[i])

            while len(stk[-1]) == 3:  # it's ready to get the result
                result = stk[-1][1] if stk[-1][0] == 'T' else stk[-1][2]
                if len(stk) > 1:
                    stk.pop()
                    stk[-1].append(result)
                else:
                    break
            i += 1

        return result
