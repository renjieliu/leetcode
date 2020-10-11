class Solution:
    def maxDepth(self, s: str) -> int:
        depth = output = 0
        for c in s:
            if c == "(":
                depth +=1
            elif c == ")":
                depth -=1
            output = max(output, depth)
        return output