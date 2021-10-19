class Solution:
    def makeFancyString(self, s: str) -> str:
        output = ""
        for c in s:
            if len(output) >= 2:
                if c != output[-1] or c != output[-2]:
                    output+=c
            else:
                output+=c
        return output
