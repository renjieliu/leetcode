class Solution:
    def modifyString(self, s: str) -> str:
        full = set([chr(i) for i in range(97, 123)])  # all the lowercase letters
        output = ""
        stk = []
        i = 0
        while i < len(s):
            c = s[i]
            if c != "?":
                if stk:
                    cannotbe = {c} if output == "" else {c, output[-1]}
                    candidates = list(full - cannotbe)
                    while stk:
                        output += candidates[len(stk) % 2]
                        stk.pop(0)
                output += c
            else:
                stk.append(c)
            i += 1

        if stk:
            cannotbe = set() if output == "" else {output[-1]}
            candidates = list(full - cannotbe)
            while stk:
                output += candidates[len(stk) % 2]
                stk.pop(0)

        return output

