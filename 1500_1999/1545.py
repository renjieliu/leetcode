class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reinvert(s):
            output = ""
            for c in s[::-1]:
                output += "1" if c == "0" else "0"
            return output
        curr = "0"
        for i in range(1, n+1):
            curr = curr + "1" + reinvert(curr)
        return curr [k-1]