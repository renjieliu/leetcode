class Solution:
    def evaluate(self, s: str, knowledge: 'List[List[str]]') -> str:
        hmp = {}
        for k, v in knowledge:
            if k not in hmp:
                hmp[k] = v

        output = ""
        stk = None
        for c in s:
            if c == "(":
                stk = ""
            elif c == ")":
                output += hmp[stk] if stk in hmp else "?"
                stk = None
            else:
                if stk != None:
                    stk+=c
                else:
                    output+=c
        return output

