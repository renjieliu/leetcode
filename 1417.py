class Solution:
    def reformat(self, s: str) -> str:
        digi, char = [], []
        for c in s:
            if 48 <= ord(c) <= 57:
                digi.append(c)
            else:
                char.append(c)
        if abs(len(digi) - len(char)) > 1:
            return ""
        else:
            A = digi if len(digi) > len(char) else char
            B = char if A == digi else digi
            output = A.pop(0)
            while A and B:
                output += B.pop(0)
                output += A.pop(0)
            if A:
                output += A.pop()
            if B:
                output += B.pop()
            return output
