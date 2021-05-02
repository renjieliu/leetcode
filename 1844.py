class Solution:
    def replaceDigits(self, s: str) -> str:
        output = ""
        for i, c in enumerate(s):
            output+=c if 97<=ord(c)<=122 else chr(ord(s[i-1])+int(c))
        return output

