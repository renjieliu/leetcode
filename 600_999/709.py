class Solution:
    def toLowerCase(self, s: str) -> str:
        output = ""
        for c in s:
            output += chr(ord(c)+32) if 65 <= ord(c) <=90 else c
        return output

