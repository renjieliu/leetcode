class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        a = list(word1)
        b = list(word2)
        while a and b:
            output+=a.pop(0)
            output+=b.pop(0)
        return output+ ("".join(a) if len(a) > 0 else "".join(b))


